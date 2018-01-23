""" Example: Shows how to identify the language a piece of text is written in. """

import urllib3

import feersum_nlu
from feersum_nlu.rest import ApiException
from examples import feersumnlu_host, feersum_nlu_auth_token

# Configure API key authorization: APIKeyHeader
configuration = feersum_nlu.Configuration()

# configuration.api_key['AUTH_TOKEN'] = feersum_nlu_auth_token
configuration.api_key['X-Auth-Token'] = feersum_nlu_auth_token  # Alternative auth key header!

configuration.host = feersumnlu_host

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

    print("Delete specific named loaded lr4 instance:")
    api_response = api_instance.lr4_language_recogniser_get_details(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

except ApiException as e:
    print("Exception when calling an lr4 operation: %s\n" % e)
except urllib3.exceptions.MaxRetryError:
    print("Connection MaxRetryError!")
