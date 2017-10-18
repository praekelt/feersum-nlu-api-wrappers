import urllib3

import feersum_nlu
from feersum_nlu.rest import ApiException

# Configure API key authorization: APIKeyHeader
feersum_nlu.configuration.api_key['AUTH_TOKEN'] = 'YOUR_API_KEY'

feersum_nlu.configuration.host = "http://127.0.0.1:8100/nlu/v2"
# feersum_nlu.configuration.host = "http://nlu.playground.feersum.io:8100/nlu/v2"

api_instance = feersum_nlu.Lr4LanguageRecognisersApi()

instance_name = 'test_lr4'

lr4_create_details = \
    feersum_nlu.Lr4CreateDetails(name=instance_name, desc="Test LR4 lang ident model.",
                                 model_file='lid_za')

text_input = feersum_nlu.TextInput("The day after tomorrow at 11:00 in the evening.")

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
