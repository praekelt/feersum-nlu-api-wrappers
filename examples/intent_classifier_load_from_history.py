""" Example: Shows how to load a pre-trained intent model from the store. """

import urllib3

import feersum_nlu
from feersum_nlu.rest import ApiException
from examples import feersumnlu_host, feersum_nlu_auth_token

# Configure API key authorization: APIKeyHeader
configuration = feersum_nlu.Configuration()

# configuration.api_key['AUTH_TOKEN'] = feersum_nlu_auth_token
configuration.api_key['X-Auth-Token'] = feersum_nlu_auth_token  # Alternative auth key header!

configuration.host = feersumnlu_host

api_instance = feersum_nlu.IntentClassifiersApi(feersum_nlu.ApiClient(configuration))

instance_name = 'test_intent_clsfr'

create_details = feersum_nlu.IntentClassifierCreateDetails(name=instance_name,
                                                           load_from_store=False,
                                                           revision_uuid='e514126d-39f3-411a-8a65-6283bfa465ab')

text_input = feersum_nlu.TextInput("Hi")

print()

try:
    print("Load the intent classifier:")
    api_response = api_instance.intent_classifier_create(create_details)  # load_from_store=True in create_details.
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the details of specific named loaded intent classifier:")
    api_response = api_instance.intent_classifier_get_details(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    # A model loaded from the history must be re-trained!
    threshold = api_response.threshold
    word_manifold_list = api_response.word_manifold_list

    train_details = feersum_nlu.TrainDetails(threshold=threshold,
                                             word_manifold_list=word_manifold_list,
                                             immediate_mode=True)

    print("Train the intent classifier:")
    api_response = api_instance.intent_classifier_train(instance_name, train_details)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the details of specific named loaded intent classifier:")
    api_response = api_instance.intent_classifier_get_details(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    # Get the classifier's possible labels. Might be inferred from the training data, but guaranteed to be available
    # after training.
    print("Get the labels of named loaded intent classifier:")
    api_response = api_instance.intent_classifier_get_labels(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Match a question:")
    api_response = api_instance.intent_classifier_retrieve(instance_name, text_input)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()
except ApiException as e:
    print("Exception when calling an intent classifier operation: %s\n" % e)
except urllib3.exceptions.HTTPError:
    print("Connection HTTPError!")
