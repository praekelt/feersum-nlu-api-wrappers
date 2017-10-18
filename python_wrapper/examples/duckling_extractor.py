import urllib3

import feersum_nlu
from feersum_nlu.rest import ApiException

# Configure API key authorization: APIKeyHeader
feersum_nlu.configuration.api_key['AUTH_TOKEN'] = 'YOUR_API_KEY'

# feersum_nlu.configuration.host = "http://127.0.0.1:8100/nlu/v2"
feersum_nlu.configuration.host = "http://nlu.playground.feersum.io:8100/nlu/v2"

api_instance = feersum_nlu.DucklingEntityExtractorsApi()

instance_name = 'test_duckling_extr'

duckling_ent_create_details = \
    feersum_nlu.DucklingEntCreateDetails(name=instance_name, desc="Test duckling extractor.",
                                         load_from_store=False)

text_input = feersum_nlu.TextInput("I was 3 weeks pregnant one month ago.")

print()

try:
    print("Create the entity extractor:")
    api_response = api_instance.duckling_entity_extractor_create(duckling_ent_create_details)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the details of all loaded entity extractors:")
    api_response = api_instance.duckling_entity_extractor_get_details_all()
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the details of specific named loaded entity extractor:")
    api_response = api_instance.duckling_entity_extractor_get_details(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Extract entities:")
    api_response = api_instance.duckling_entity_extractor_retrieve(instance_name, text_input)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()
except ApiException as e:
    print("Exception when calling a entity extractor operation: %s\n" % e)
except urllib3.exceptions.MaxRetryError:
    print("Connection MaxRetryError!")
