""" Example: Shows how to create, train and use an intent classifier. """

import urllib3

import feersum_nlu
from feersum_nlu.rest import ApiException
from examples import feersumnlu_host, feersum_nlu_auth_token

# Configure API key authorization: APIKeyHeader
configuration = feersum_nlu.Configuration()

# configuration.api_key['AUTH_TOKEN'] = feersum_nlu_auth_token
configuration.api_key['X-Auth-Token'] = feersum_nlu_auth_token  # Alternative auth key header!

configuration.host = feersumnlu_host

api_client = feersum_nlu.ApiClient(configuration)

# Example of how to setup request retries!
api_client.rest_client.pool_manager.connection_pool_kw['retries'] = 3
api_instance = feersum_nlu.IntentClassifiersApi(api_client)

instance_name = 'test_intent_clsfr'

word_manifold_list = [feersum_nlu.LabelledWordManifold('eng', 'feers_wm_eng')]
# The playground's pre-loaded embeddings include:
# "feers_wm_afr", "feers_wm_eng", "feers_wm_nbl", "feers_wm_xho",
# "feers_wm_zul", "feers_wm_ssw", "feers_wm_nso", "feers_wm_sot",
# "feers_wm_tsn", "feers_wm_ven", "feers_wm_tso"
# and "glove6B50D_trimmed"

create_details = feersum_nlu.IntentClassifierCreateDetails(name=instance_name,
                                                           desc="Test intent classifier.",
                                                           long_name=instance_name,
                                                           lid_model_file="lid_za",
                                                           load_from_store=False)
# load_from_store=True,
# revision_uuid='e514126d-39f3-411a-8a65-6283bfa465ab')

# The training samples.
labelled_text_sample_list = []
labelled_text_sample_list.append(feersum_nlu.LabelledTextSample(text="I would like to fill in a claim form.",
                                                                label="claim"))
labelled_text_sample_list.append(feersum_nlu.LabelledTextSample(text="How should I claim?",
                                                                label="claim"))
labelled_text_sample_list.append(feersum_nlu.LabelledTextSample(text="I would like to get a quote.",
                                                                label="quote"))
labelled_text_sample_list.append(feersum_nlu.LabelledTextSample(text="Where can I get a quote?",
                                                                label="quote"))

# train_details = feersum_nlu.TrainDetails(immediate_mode=True)
train_details = feersum_nlu.TrainDetails(threshold=1.0,
                                         temperature=0.9,
                                         word_manifold_list=word_manifold_list,
                                         immediate_mode=True)

text_input = feersum_nlu.TextInput("How do I get a quote?")

caller_name = 'example_caller'

print()

try:
    print("Create the intent classifier:")
    api_response = api_instance.intent_classifier_create(create_details, x_caller=caller_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Add training samples to the intent classifier:")
    api_response = api_instance.intent_classifier_add_training_samples(instance_name, labelled_text_sample_list)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the training samples of the intent classifier:")
    api_response = api_instance.intent_classifier_get_training_samples(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Del the training samples of the intent classifier:")
    api_response = api_instance.intent_classifier_del_training_samples_all(instance_name)
    # api_response = api_instance.intent_classifier_del_training_samples(instance_name,
    #                                                                    labelled_text_sample_list=[])
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Add training samples to the intent classifier:")
    api_response = api_instance.intent_classifier_add_training_samples(instance_name, labelled_text_sample_list)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    # print("Del testing samples of the intent classifier:")
    # api_response = api_instance.intent_classifier_del_testing_samples_all(instance_name)
    # # api_response = api_instance.intent_classifier_del_testing_samples(instance_name,
    # #                                                             labelled_text_sample_list=
    # #                                                             labelled_text_sample_testing_list)
    # print(" type(api_response)", type(api_response))
    # print(" api_response", api_response)
    # print()

    print("Train the intent classifier:")
    api_response = api_instance.intent_classifier_train(instance_name, train_details)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the details of all loaded intent classifiers:")
    api_response = api_instance.intent_classifier_get_details_all()
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the details of specific named loaded intent classifiers:")
    api_response = api_instance.intent_classifier_get_details(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    # Get the classifier's possible labels. Might be inferred from the training data, but guaranteed to be available
    # after training.
    print("Get the labels of named loaded intent classifiers:")
    api_response = api_instance.intent_classifier_get_labels(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get some curate details of specific named loaded intent classifier:")
    # Use the same labels as returned in the confusion matrix.
    label_pair = feersum_nlu.ClassLabelPair(matrix_name='train', true_label='1', predicted_label='1')
    api_response = api_instance.intent_classifier_curate(instance_name, label_pair)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the model params:")
    api_response = api_instance.intent_classifier_get_params(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Update the model params:")
    model_params = feersum_nlu.ModelParams(threshold=0.7, desc="Examples: Test classifier.",
                                           long_name='Test Classifier')
    api_response = api_instance.intent_classifier_set_params(instance_name, model_params)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the details of specific named loaded intent classifiers:")
    api_response = api_instance.intent_classifier_get_details(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Classify intent:")
    api_response = api_instance.intent_classifier_retrieve(instance_name, text_input, x_caller=caller_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Delete specific named loaded intent classifiers:")
    api_response = api_instance.intent_classifier_del(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Vaporise specific named loaded intent classifiers:")
    api_response = api_instance.intent_classifier_vaporise(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

except ApiException as e:
    print("Exception when calling an intent classifier operation: %s\n" % e)
except urllib3.exceptions.HTTPError as e:
    print("Connection HTTPError! %s\n" % e)
