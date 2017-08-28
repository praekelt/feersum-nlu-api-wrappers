import urllib3

import feersum_nlu
from feersum_nlu.rest import ApiException

# Configure API key authorization: APIKeyHeader
feersum_nlu.configuration.api_key['AUTH_TOKEN'] = 'YOUR_API_KEY'

# feersum_nlu.configuration.host = "http://127.0.0.1:8000/nlu/v2"
feersum_nlu.configuration.host = "http://dev-bernardt.za.prk.hosting:8000/nlu/v2"

api_instance = feersum_nlu.RegexEntityExtractorsApi()

instance_name = 'test_regex_extr'

regex_ent_create_details = \
    feersum_nlu.RegexEntCreateDetails(name=instance_name, desc="Test regex extractor.",
                                      regex=r"(?P<license>"
                                            r"([A-Z]{3}[ ]?[0-9]{3}[ ]?(GP|NW|MP|EC|L|NC|NW))|"
                                            r"([A-Z]{2}[ ]?[0-9]{2}[ ]?[A-Z]{2}[ ]?(GP|NW|MP|EC|L|NC|NW)))",
                                      load_from_store=False)

text_input = feersum_nlu.TextInput("My car has license number JMS 007 GP.")

print()

try:
    print("Create the entity extractor:")
    api_response = api_instance.regex_entity_extractor_create(regex_ent_create_details)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the details of all loaded entity extractors:")
    api_response = api_instance.regex_entity_extractor_get_details_all()
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the details of specific named loaded entity extractor:")
    api_response = api_instance.regex_entity_extractor_get_details(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Extract entities:")
    api_response = api_instance.regex_entity_extractor_retrieve(instance_name, text_input)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()
except ApiException as e:
    print("Exception when calling a entity extractor operation: %s\n" % e)
except urllib3.exceptions.MaxRetryError:
    print("Connection MaxRetryError!")
