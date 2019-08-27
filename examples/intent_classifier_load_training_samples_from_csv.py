""" Example: Shows how to create & train an Intent classifier from a CSV file. """

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

api_instance = feersum_nlu.IntentClassifiersApi(feersum_nlu.ApiClient(configuration))

instance_name = 'intent-model'

create_details = feersum_nlu.IntentClassifierCreateDetails(name=instance_name,
                                                           desc="Intent model for demos to ....",
                                                           long_name="Intent Model",
                                                           lid_model_file="lid_za",
                                                           load_from_store=False)

# The training samples.
text_sample_list = []
# labelled_text_sample_list.append(feersum_nlu.LabelledTextSample(text="Hoe eis?", label="claim", lang_code="afr"))

with open('training_samples.csv',
          'r', newline='') as csvfile:
    csv_reader = csv.reader(csvfile,
                            delimiter=',',
                            quotechar='"',
                            quoting=csv.QUOTE_MINIMAL)

    for row in csv_reader:
        text_sample_list.append(feersum_nlu.LabelledTextSample(text=row[1],
                                                               label=row[0],
                                                               lang_code=None))

offline_batch_size = 10

word_manifold_list = [feersum_nlu.LabelledWordManifold('eng', 'feers_wm_eng'),
                      feersum_nlu.LabelledWordManifold('afr', 'feers_wm_afr'),
                      # feersum_nlu.LabelledWordManifold('nbl', 'feers_wm_xho'),
                      # feersum_nlu.LabelledWordManifold('xho', 'feers_wm_xho'),
                      # feersum_nlu.LabelledWordManifold('zul', 'feers_wm_zul'),
                      # feersum_nlu.LabelledWordManifold('ssw', 'feers_wm_ssw'),
                      # feersum_nlu.LabelledWordManifold('nso', 'feers_wm_nso'),
                      # feersum_nlu.LabelledWordManifold('sot', 'feers_wm_sot'),
                      # feersum_nlu.LabelledWordManifold('tsn', 'feers_wm_tsn'),
                      # feersum_nlu.LabelledWordManifold('ven', 'feers_wm_ven'),
                      # eersum_nlu.LabelledWordManifold('tso', 'feers_wm_tso')
                      ]

# The playground's pre-loaded embeddings include:
# "feers_wm_afr", "feers_wm_eng", "feers_wm_nbl", "feers_wm_xho",
# "feers_wm_zul", "feers_wm_ssw", "feers_wm_nso", "feers_wm_sot",
# "feers_wm_tsn", "feers_wm_ven", "feers_wm_tso"
# and "glove6B50D_trimmed"


caller_name = 'example_caller'

print()

try:
    print("Create the Intent classifier:")
    api_response = api_instance.intent_classifier_create(create_details, x_caller=caller_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Add training samples to the Intent classifier:")
    api_response = api_instance.intent_classifier_add_training_samples(instance_name,
                                                                       text_sample_list[:offline_batch_size])
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    immediate_mode = True  # Set to True to do a blocking train operation.

    train_details = feersum_nlu.TrainDetails(threshold=0.85,
                                             word_manifold_list=word_manifold_list,
                                             immediate_mode=immediate_mode)

    print("Train the Intent classifier:")
    instance_detail = api_instance.intent_classifier_train(instance_name, train_details)
    print(" type(api_response)", type(instance_detail))
    print(" api_response", instance_detail)
    print()

    # TRAINING:
    # If timestamp begins with 'ASYNC...' the the training is running in the background and you need to poll until the
    # model ID has updated.
    # if timestamp doesn't begin with ASYNC then the training has completed synchronously and you may continue.
    # In the near future webhooks will be supported to let you know when async training has finished.

    if instance_detail.training_stamp.startswith('ASYNC'):
        # Background training in progress. We'll poll and wait for it to complete.
        print("Background training in progress...", flush=True, end='')
        previous_id = instance_detail.id

        while True:
            print('.', end='', flush=True)
            time.sleep(1)
            inst_det = api_instance.intent_classifier_get_details(instance_name)
            if inst_det.id != previous_id:
                # ToDo: Stop if details indicate that training failed.
                break  # break from while-loop when ID updated which indicates training done.

        print('Done.')
        print()

    print("Get the details of specific named loaded Intent classifier:")
    api_response = api_instance.intent_classifier_get_details(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    cm_labels = api_response.cm_labels
    print()

    print("Get the parameters:")
    api_response = api_instance.intent_classifier_get_params(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    # Make the model smarter by providing more training example and training online.
    # Note: The training happens automatically after online samples provided.
    online_batch_size = 100
    for i in range(offline_batch_size, len(text_sample_list), online_batch_size):
        api_response = \
            api_instance.intent_classifier_online_training_samples(instance_name,
                                                                   text_sample_list[i:min(i + online_batch_size,
                                                                                          len(text_sample_list))])
        print(f"{i}/{len(text_sample_list)}")

    # print("Delete specific named loaded Intent classifier:")
    # api_response = api_instance.intent_classifier_del(instance_name)
    # print(" type(api_response)", type(api_response))
    # print(" api_response", api_response)
    # print()
    #
    # print("Vaporise specific named loaded Intent classifier:")
    # api_response = api_instance.intent_classifier_vaporise(instance_name)
    # print(" type(api_response)", type(api_response))
    # print(" api_response", api_response)
    # print()

except ApiException as e:
    print("Exception when calling an Intent classifier operation: %s\n" % e)
except urllib3.exceptions.HTTPError as e:
    print("Connection HTTPError! %s\n" % e)
