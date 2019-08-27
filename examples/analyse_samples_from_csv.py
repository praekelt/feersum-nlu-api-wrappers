""" Example: Shows how to use the API to analyse samples from a CSV file. """

import urllib3
import time
import csv
import operator

import feersum_nlu
from feersum_nlu.rest import ApiException
from examples import feersumnlu_host, feersum_nlu_auth_token

# Configure API key authorization: APIKeyHeader
configuration = feersum_nlu.Configuration()

# configuration.api_key['AUTH_TOKEN'] = feersum_nlu_auth_token
configuration.api_key['X-Auth-Token'] = feersum_nlu_auth_token  # Alternative auth key header!

configuration.host = feersumnlu_host


def update_LID(sample_list_name: str = 'training_samples'):
    # The training samples.
    text_sample_list = []
    # labelled_text_sample_list.append(feersum_nlu.LabelledTextSample(text="Hoe eis?", label="claim", lang_code="afr"))

    with open(sample_list_name + '.csv', 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile,
                                delimiter=',',
                                quotechar='"',
                                quoting=csv.QUOTE_MINIMAL)

        for row in csv_reader:
            text_sample_list.append(feersum_nlu.LabelledTextSample(text=row[1],
                                                                   label=row[0],
                                                                   lang_code=None))

    caller_name = 'example_caller'

    print()

    try:
        lid_api_instance = feersum_nlu.LanguageRecognisersApi(feersum_nlu.ApiClient(configuration))
        lid_instance_name = 'language_recogniser'

        language_recogniser_create_details = \
            feersum_nlu.LanguageRecogniserCreateDetails(name=lid_instance_name,
                                                        desc=lid_instance_name,
                                                        long_name=lid_instance_name,
                                                        lid_model_file='lid_za',
                                                        load_from_store=False)

        print("Create the language recogniser instance:")
        api_response = lid_api_instance.language_recogniser_create(language_recogniser_create_details)
        print(" type(api_response)", type(api_response))
        print(" api_response", api_response)
        print()

        print("Get the labels of named loaded language recogniser instance:")
        api_response = lid_api_instance.language_recogniser_get_labels(lid_instance_name)
        print(" type(api_response)", type(api_response))
        print(" api_response", api_response)
        print()

        print("Add language to samples.")
        for i in range(len(text_sample_list)):
            scored_label_list = lid_api_instance.language_recogniser_retrieve(lid_instance_name, text_sample_list[i])
            text_sample_list[i].lang_code = scored_label_list[0].label
            if i % 1000 == 0:
                print(i / len(text_sample_list))

        print("Write the training samples to a csv file:")
        with open(sample_list_name + '_plus_lang.csv', 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile,
                                    delimiter=',',
                                    quotechar='"',
                                    quoting=csv.QUOTE_MINIMAL)

            for sample in text_sample_list:
                label = sample.label
                text = sample.text
                lang_code = sample.lang_code

                if (label is not None) and (text is not None):
                    csv_writer.writerow([label, text, lang_code])

    except ApiException as e:
        print("Exception when calling an FAQ matcher operation: %s\n" % e)
    except urllib3.exceptions.HTTPError as e:
        print("Connection HTTPError! %s\n" % e)


def count_language_breakdown(sample_list_name: str = 'training_samples'):
    print('count_language_breakdown:')

    text_sample_list = []
    # labelled_text_sample_list.append(feersum_nlu.LabelledTextSample(text="Hoe eis?", label="claim", lang_code="afr"))

    with open(sample_list_name + '.csv', 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile,
                                delimiter=',',
                                quotechar='"',
                                quoting=csv.QUOTE_MINIMAL)

        for row in csv_reader:
            text_sample_list.append(feersum_nlu.LabelledTextSample(text=row[1],
                                                                   label=row[0],
                                                                   lang_code=row[2]))

    breakdown_dict = {}  # type: Dict[str, int]

    for sample in text_sample_list:
        label = sample.lang_code
        count = breakdown_dict.get(label, 0)
        breakdown_dict[label] = count + 1

    # for key, value in breakdown_dict.items():
    #     print("  ", value, ":", key)

    sorted_breakdown = sorted(breakdown_dict.items(), key=operator.itemgetter(1), reverse=True)

    for key, value in sorted_breakdown:
        print("  ", value, ":", key)

    print()


def count_response_breakdown(sample_list_name: str = 'training_samples'):
    print('count_response_breakdown:')

    text_sample_list = []
    # labelled_text_sample_list.append(feersum_nlu.LabelledTextSample(text="Hoe eis?", label="claim", lang_code="afr"))

    with open(sample_list_name + '.csv', 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile,
                                delimiter=',',
                                quotechar='"',
                                quoting=csv.QUOTE_MINIMAL)

        for row in csv_reader:
            text_sample_list.append(feersum_nlu.LabelledTextSample(text=row[1],
                                                                   label=row[0],
                                                                   lang_code=row[2]))

    breakdown_dict = {}  # type: Dict[str, int]

    for sample in text_sample_list:
        label = sample.label[:min(100, len(sample.label))]
        count = breakdown_dict.get(label, 0)
        breakdown_dict[label] = count + 1

    # for key, value in breakdown_dict.items():
    #     print("  ", value, ":", key)

    sorted_breakdown = sorted(breakdown_dict.items(), key=operator.itemgetter(1), reverse=True)

    for key, value in sorted_breakdown:
        print("  ", value, ":", key)

    print()


# update_LID('training_samples_momconnect_2019-08-27')
count_language_breakdown('training_samples_xxx_2019-08-27_plus_lang')
count_response_breakdown('training_samples_xxx_2019-08-27_plus_lang')
