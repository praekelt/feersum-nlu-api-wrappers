import urllib3

import feersum_nlu
from feersum_nlu.rest import ApiException

# Configure API key authorization: APIKeyHeader
feersum_nlu.configuration.api_key['AUTH_TOKEN'] = 'FEERSUM-NLU-f9b-bdc0-455e-a3b1-7c761'  # 'YOUR_API_KEY'

# feersum_nlu.configuration.host = "http://127.0.0.1:8100/nlu/v2"
feersum_nlu.configuration.host = "http://nlu.playground.feersum.io:8000/nlu/v2"


# === Word manifold to use ===
print("Create the word manifold model:")
wm_api_instance = feersum_nlu.WordManifoldsApi()
wm_instance_name = 'test_wm'
wm_create_details = feersum_nlu.CreateDetails(name=wm_instance_name, desc="Test word manifold.",
                                              load_from_store=False, input_file="glove.6B.50d.trimmed.txt")
# wm_create_details = feersum_nlu.CreateDetails(name=wm_instance_name, load_from_store=True)
wm_api_response = wm_api_instance.word_manifold_create(wm_create_details)
print(" type(wm_api_response)", type(wm_api_response))
print(" wm_api_response", wm_api_response)
print()
# === ===


api_instance = feersum_nlu.SimilarityEntityExtractorsApi()

instance_name = 'test_similarity_extr'

similarity_ent_create_details = \
    feersum_nlu.SimilarityEntCreateDetails(name=instance_name, desc="Test similarity extractor.",
                                           similar_words=["red", "green", "blue"],
                                           threshold=0.65,
                                           word_manifold="test_wm",
                                           load_from_store=False)

text_input = feersum_nlu.TextInput("I have an orange car.")

print()

try:
    print("Create the entity extractor:")
    api_response = api_instance.similarity_entity_extractor_create(similarity_ent_create_details)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the details of all loaded entity extractors:")
    api_response = api_instance.similarity_entity_extractor_get_details_all()
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the details of specific named loaded entity extractor:")
    api_response = api_instance.similarity_entity_extractor_get_details(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Extract entities:")
    api_response = api_instance.similarity_entity_extractor_retrieve(instance_name, text_input)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()
except ApiException as e:
    print("Exception when calling a entity extractor operation: %s\n" % e)
except urllib3.exceptions.MaxRetryError:
    print("Connection MaxRetryError!")
