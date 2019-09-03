""" Example: Shows how to create, train and use a Synonym entity extractor. """

import urllib3

import feersum_nlu
from feersum_nlu.rest import ApiException
from examples import feersumnlu_host, feersum_nlu_auth_token

# Configure API key authorization: APIKeyHeader
configuration = feersum_nlu.Configuration()

# configuration.api_key['AUTH_TOKEN'] = feersum_nlu_auth_token
configuration.api_key['X-Auth-Token'] = feersum_nlu_auth_token  # Alternative auth key header!

configuration.host = feersumnlu_host

api_instance = feersum_nlu.SynonymEntityExtractorsApi(feersum_nlu.ApiClient(configuration))

instance_name = 'genres'

text_input_0 = feersum_nlu.TextInput("Do you have comedy shows?",
                                     lang_code="eng")  # optional language hint.

caller_name = 'example_caller'

print()

try:
    # print("Get the training samples of the synonym entity extractor:")
    # api_response = api_instance.synonym_entity_extractor_get_training_samples(instance_name)
    # print(" type(api_response)", type(api_response))
    # print(" api_response", api_response)
    # print()
    #
    # print("Get the details of specific named loaded synonym entity extractor:")
    # api_response = api_instance.synonym_entity_extractor_get_details(instance_name)
    # print(" type(api_response)", type(api_response))
    # print(" api_response", api_response)
    # print()
    #
    # # Get the classifier's possible labels. Might be inferred from the training data, but guaranteed to be available
    # # after training.
    # print("Get the labels of named loaded synonym entity extractor:")
    # api_response = api_instance.synonym_entity_extractor_get_labels(instance_name)
    # print(" type(api_response)", type(api_response))
    # print(" api_response", api_response)
    # print()
    #
    print("Extract some entities::")
    api_response = api_instance.synonym_entity_extractor_retrieve(instance_name, text_input_0)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    # print("Get the parameters:")
    # api_response = api_instance.synonym_entity_extractor_get_params(instance_name)
    # print(" type(api_response)", type(api_response))
    # print(" api_response", api_response)
    # print()

except ApiException as e:
    print("Exception when calling an synonym Entity Extractor operation: %s\n" % e)
except urllib3.exceptions.HTTPError as e:
    print("Connection HTTPError! %s\n" % e)
