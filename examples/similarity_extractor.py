""" Example: Shows how the similar word entity extractor may be used. """

import urllib3

import feersum_nlu
from feersum_nlu.rest import ApiException
from examples import feersumnlu_host, feersum_nlu_auth_token

# Configure API key authorization: APIKeyHeader
configuration = feersum_nlu.Configuration()

# configuration.api_key['AUTH_TOKEN'] = feersum_nlu_auth_token
configuration.api_key['X-Auth-Token'] = feersum_nlu_auth_token  # Alternative auth key header!

configuration.host = feersumnlu_host

api_instance = feersum_nlu.SimWordEntityExtractorsApi(feersum_nlu.ApiClient(configuration))

instance_name = 'sim-word-extractor-test'

similarity_ent_create_details = \
    feersum_nlu.SimWordEntityExtractorCreateDetails(name=instance_name,
                                                    desc="Test similarity extractor.",
                                                    similar_words=["red", "green", "blue", "purple",
                                                                   "white", "black", "grey"],
                                                    threshold=0.6,
                                                    # (0.0-1.0] - lower vals result in more false positives.
                                                    word_manifold="feers_wm_eng",
                                                    # This is one of the built-in word embeddings.
                                                    load_from_store=False)

text_input = feersum_nlu.TextInput("I have an orange car with pink stripes. And a green truck.")
# api_response [{'entity': 'orange', 'similarity': 0.6299035873841149},
#               {'entity': 'pink', 'similarity': 0.690814436389662}]

print()

try:
    print("Create the entity extractor:")
    api_response = api_instance.sim_word_entity_extractor_create(similarity_ent_create_details)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the details of all loaded entity extractors:")
    api_response = api_instance.sim_word_entity_extractor_get_details_all()
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the details of specific named loaded entity extractor:")
    api_response = api_instance.sim_word_entity_extractor_get_details(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Extract entities:")
    api_response = api_instance.sim_word_entity_extractor_retrieve(instance_name, text_input)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the parameters:")
    api_response = api_instance.sim_word_entity_extractor_get_params(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Update the parameters:")
    model_params = \
        feersum_nlu.ModelParams(similar_words=["car", "truck"])
    api_response = api_instance.sim_word_entity_extractor_set_params(instance_name, model_params)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Extract entities:")
    api_response = api_instance.sim_word_entity_extractor_retrieve(instance_name, text_input)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Delete named loaded entity extractor:")
    api_response = api_instance.sim_word_entity_extractor_del(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Vaporise named loaded entity extractor:")
    api_response = api_instance.sim_word_entity_extractor_vaporise(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

except ApiException as e:
    print("Exception when calling a entity extractor operation: %s\n" % e)
except urllib3.exceptions.HTTPError as e:
    print("Connection HTTPError! %s\n" % e)
