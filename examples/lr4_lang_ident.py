""" Example: Shows how to identify the language a piece of text is written in. """

import os
import urllib3

import feersum_nlu
from feersum_nlu.rest import ApiException

# Try to get the API key from your OS environment, else use 'YOUR_API_KEY' as the default value in the code below.
# You may use any environment variable you want, it doesn't have to be 'FEERSUM_NLU_AUTH_TOKEN'.
feersum_nlu_auth_token = os.environ.get('FEERSUM_NLU_AUTH_TOKEN', 'YOUR_API_KEY')
print('feersum_nlu_auth_token = ', feersum_nlu_auth_token)

# Configure API key authorization: APIKeyHeader
configuration = feersum_nlu.Configuration()
configuration.api_key['AUTH_TOKEN'] = feersum_nlu_auth_token

# configuration.host = "http://127.0.0.1:8100/nlu/v2"
configuration.host = "https://nlu.playground.feersum.io:443/nlu/v2"

api_instance = feersum_nlu.Lr4LanguageRecognisersApi(feersum_nlu.ApiClient(configuration))

instance_name = 'test_lr4'

lr4_create_details = \
    feersum_nlu.Lr4CreateDetails(name=instance_name,
                                 desc="Test LR4 lang ident model.",
                                 lid_model_file='lid_za')

text_input = feersum_nlu.TextInput("Isakhiwo sami sebiwe?")

print()

try:
    print("Create the lr4 instance:")
    api_response = api_instance.lr4_language_recogniser_create(lr4_create_details)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the details of all loaded lr4 instances:")
    api_response = api_instance.lr4_language_recogniser_get_details_all()
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the details of specific named loaded lr4 instance:")
    api_response = api_instance.lr4_language_recogniser_get_details(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    # Get the classifier's possible labels. Might be inferred from the training data, but guaranteed to be available
    # after training.
    print("Get the labels of named loaded lr4 instance:")
    api_response = api_instance.lr4_language_recogniser_get_labels(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Identify the language of the text:")
    api_response = api_instance.lr4_language_recogniser_retrieve(instance_name, text_input)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()
except ApiException as e:
    print("Exception when calling an lr4 operation: %s\n" % e)
except urllib3.exceptions.MaxRetryError:
    print("Connection MaxRetryError!")
