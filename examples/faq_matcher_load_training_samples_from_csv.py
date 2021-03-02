""" Example: Shows how to create & train an FAQ matcher from a CSV file. """

import urllib3
import time
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

create_details = feersum_nlu.FaqMatcherCreateDetails(name=instance_name,
                                                     desc="Longer desc of model.",
                                                     long_name=instance_name,
                                                     lid_model_file="lid_za",
                                                     load_from_store=False)

# The training samples.
text_sample_list = []

with open('training_samples.csv',
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
                                                               lang_code=None))

word_manifold_list = [feersum_nlu.LabelledWordManifold('eng', 'feers_wm_eng'),
                      feersum_nlu.LabelledWordManifold('afr', 'feers_wm_afr'),
                      feersum_nlu.LabelledWordManifold('nbl', 'feers_wm_nbl'),
                      feersum_nlu.LabelledWordManifold('xho', 'feers_wm_xho'),
                      feersum_nlu.LabelledWordManifold('zul', 'feers_wm_zul'),
                      feersum_nlu.LabelledWordManifold('ssw', 'feers_wm_ssw'),
                      feersum_nlu.LabelledWordManifold('nso', 'feers_wm_nso'),
                      feersum_nlu.LabelledWordManifold('sot', 'feers_wm_sot'),
                      feersum_nlu.LabelledWordManifold('tsn', 'feers_wm_tsn'),
                      feersum_nlu.LabelledWordManifold('ven', 'feers_wm_ven'),
                      feersum_nlu.LabelledWordManifold('tso', 'feers_wm_tso')
                      ]

# The playground's pre-loaded embeddings include:
# "feers_wm_afr", "feers_wm_eng", "feers_wm_nbl", "feers_wm_xho",
# "feers_wm_zul", "feers_wm_ssw", "feers_wm_nso", "feers_wm_sot",
# "feers_wm_tsn", "feers_wm_ven", "feers_wm_tso"
# and "glove6B50D_trimmed"


caller_name = 'example_caller'

print()

try:
    print("Create the FAQ matcher:")
    api_response = api_instance.faq_matcher_create(create_details, x_caller=caller_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Add training samples to the FAQ matcher:")
    api_response = api_instance.faq_matcher_add_training_samples(instance_name,
                                                                 text_sample_list)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    immediate_mode = True  # Set to True to do a blocking train operation.

    train_details = feersum_nlu.TrainDetails(threshold=0.85,
                                             word_manifold_list=word_manifold_list,
                                             immediate_mode=immediate_mode)

    print("Train the FAQ matcher:")
    instance_detail = api_instance.faq_matcher_train(instance_name, train_details)
    print(" type(api_response)", type(instance_detail))
    print(" api_response", instance_detail)
    print()

    # TRAINING:
    # If there is no timestamp then the training is running in the background and you need to poll until the
    # model ID has updated else the training has completed synchronously and you may continue.
    # In the near future webhooks will be supported to let you know when async training has finished.

    if instance_detail.training_stamp is None:
        # Background training in progress. We'll poll and wait for it to complete.
        print("Background training in progress...", flush=True, end='')
        previous_id = instance_detail.id

        while True:
            print('.', end='', flush=True)
            time.sleep(1)
            inst_det = api_instance.faq_matcher_get_details(instance_name)
            if inst_det.id != previous_id:
                # ToDo: Stop if details indicate that training failed.
                break  # break from while-loop when ID updated which indicates training done.

        print('Done.')
        print()

    print("Get the details of specific named loaded FAQ matcher:")
    api_response = api_instance.faq_matcher_get_details(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    cm_labels = api_response.cm_labels
    print()

    print("Get the parameters:")
    api_response = api_instance.faq_matcher_get_params(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    # print("Delete specific named loaded FAQ matcher:")
    # api_response = api_instance.faq_matcher_del(instance_name)
    # print(" type(api_response)", type(api_response))
    # print(" api_response", api_response)
    # print()
    #
    # print("Vaporise specific named loaded FAQ matcher:")
    # api_response = api_instance.faq_matcher_vaporise(instance_name)
    # print(" type(api_response)", type(api_response))
    # print(" api_response", api_response)
    # print()

except ApiException as e:
    print("Exception when calling an FAQ matcher operation: %s\n" % e)
except urllib3.exceptions.HTTPError as e:
    print("Connection HTTPError! %s\n" % e)
