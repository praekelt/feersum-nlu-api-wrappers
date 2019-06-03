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

api_instance = feersum_nlu.LanguageRecognisersApi(feersum_nlu.ApiClient(configuration))

instance_name = 'test_language_recogniser'

language_recogniser_create_details = \
    feersum_nlu.LanguageRecogniserCreateDetails(name=instance_name,
                                                desc="Test lang ident model.",
                                                long_name="Test language recogniser.",
                                                lid_model_file='lid_za',
                                                load_from_store=False)

text_input = feersum_nlu.TextInput("Isakhiwo sami sebiwe?")

print()

try:
    print("Create the language recogniser instance:")
    api_response = api_instance.language_recogniser_create(language_recogniser_create_details)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the details of all loaded language recogniser instances:")
    api_response = api_instance.language_recogniser_get_details_all()
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the details of specific named loaded language recogniser instance:")
    api_response = api_instance.language_recogniser_get_details(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    # Get the classifier's possible labels. Might be inferred from the training data, but guaranteed to be available
    # after training.
    print("Get the labels of named loaded language recogniser instance:")
    api_response = api_instance.language_recogniser_get_labels(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Identify the language of the text:")
    api_response = api_instance.language_recogniser_retrieve(instance_name, text_input)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the parameters:")
    api_response = api_instance.language_recogniser_get_params(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Update the parameters:")
    model_params = \
        feersum_nlu.ModelParams(reference_time="2017-01-21 0:00+01:00")
    api_response = api_instance.language_recogniser_set_params(instance_name, model_params)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Delete specific named loaded language recogniser instance:")
    api_response = api_instance.language_recogniser_del(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Vaporise specific named loaded language recogniser instance:")
    api_response = api_instance.language_recogniser_vaporise(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

except ApiException as e:
    print("Exception when calling an language recogniser operation: %s\n" % e)
except urllib3.exceptions.HTTPError as e:
    print("Connection HTTPError! %s\n" % e)
