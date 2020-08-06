""" Example: Shows how to create, train and use an FAQ matcher. """

import urllib3
import csv

import feersum_nlu
from feersum_nlu.rest import ApiException
from examples import feersumnlu_host, feersum_nlu_auth_token

# Configure API key authorization: APIKeyHeader
configuration = feersum_nlu.Configuration()

# configuration.api_key['AUTH_TOKEN'] = feersum_nlu_auth_token
configuration.api_key['X-Auth-Token'] = feersum_nlu_auth_token  # Alternative auth key header!

configuration.host = feersumnlu_host

api_instance = feersum_nlu.FaqMatchersApi(feersum_nlu.ApiClient(configuration))

instance_name = 'test_faq'

# text_input_0 = feersum_nlu.TextInput("Can I give my baby tea?",
#                                      lang_code=None)  # optional language hint.

caller_name = 'example_caller'

print()

# The testing samples.
text_sample_list = []

with open('testing_samples.csv',
          'r', newline='') as csvfile:
    csv_reader = csv.reader(csvfile,
                            delimiter=',',
                            quotechar='"',
                            quoting=csv.QUOTE_MINIMAL)

    for row in csv_reader:
        if len(row) >= 3:
            lang_code = row[2] if row[2] != '' else None
        else:
            lang_code = None

        text_sample_list.append(feersum_nlu.LabelledTextSample(text=row[1],
                                                               label=row[0],
                                                               lang_code=lang_code))

try:
    # print("Get the parameters:")
    # api_response = api_instance.faq_matcher_get_params(instance_name)
    # print(" type(api_response)", type(api_response))
    # print(" api_response", api_response)
    # print()
    #
    # print("Update the parameters:")
    # model_params = \
    #     feersum_nlu.ModelParams(threshold=1.1)
    # api_response = api_instance.faq_matcher_set_params(instance_name, model_params)
    # print(" type(api_response)", type(api_response))
    # print(" api_response", api_response)
    # print()
    #
    # print("Get the details of specific named loaded FAQ matcher:")
    # api_response = api_instance.faq_matcher_get_details(instance_name)
    # print(" type(api_response)", type(api_response))
    # print(" api_response", api_response)
    # cm_labels = api_response.cm_labels
    # print()

    print("Match a question:")
    correct = 0
    total = 0
    for sample in text_sample_list:
        if True:  # sample.lang_code == 'eng':
            text_input = feersum_nlu.TextInput(sample.text,
                                               lang_code=None)  # optional language hint.

            api_response = api_instance.faq_matcher_retrieve(instance_name, text_input, x_caller=caller_name)

            top_k = 2
            response_label_set = set()
            for i in range(min(top_k, len(api_response))):
                response_label_set.add(api_response[i].label[:20])

            if sample.label[:20] in response_label_set:
                correct = correct + 1
                print('.', sample.text, ", ", sample.label)
            else:
                print('x', sample.text, ", ", sample.label)
            total = total + 1
        # print(" type(api_response)", type(api_response))
        # print(" api_response", api_response)
        # print()

    print("accuracy =", correct / total)

except ApiException as e:
    print("Exception when calling an FAQ matcher operation: %s\n" % e)
except urllib3.exceptions.HTTPError as e:
    print("Connection HTTPError! %s\n" % e)
