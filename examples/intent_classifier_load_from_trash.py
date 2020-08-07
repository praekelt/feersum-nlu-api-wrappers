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

instance_name = 'bd_mainrouter'

create_details = feersum_nlu.IntentClassifierCreateDetails(name=instance_name,
                                                           load_from_store=True)

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

    # Get the classifier's possible labels. Might be inferred from the training data, but guaranteed to be available
    # after training.
    print("Get the labels of named loaded intent classifier:")
    api_response = api_instance.intent_classifier_get_labels(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get some curate details of specific named loaded intent classifier:")
    # Use the same labels as returned in the confusion matrix.
    label_pair = feersum_nlu.ClassLabelPair(matrix_name='train', true_label='0', predicted_label='0')
    api_response = api_instance.intent_classifier_curate(instance_name, label_pair)
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
