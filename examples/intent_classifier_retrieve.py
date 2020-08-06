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

api_instance = feersum_nlu.IntentClassifiersApi(feersum_nlu.ApiClient(configuration))

instance_name = 'navigation'


text_input = feersum_nlu.TextInput("How do I get a quote?")
caller_name = 'example_caller'

print()

try:
    print("Get the details of specific named loaded intent classifiers:")
    api_response = api_instance.intent_classifier_get_details(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the labels of named loaded intent classifiers:")
    api_response = api_instance.intent_classifier_get_labels(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Classify intent:")
    api_response = api_instance.intent_classifier_retrieve(instance_name, text_input, x_caller=caller_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

except ApiException as e:
    print("Exception when calling an intent classifier operation: %s\n" % e)
except urllib3.exceptions.HTTPError as e:
    print("Connection HTTPError! %s\n" % e)
