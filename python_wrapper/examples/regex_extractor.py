import urllib3

import feersum_nlu
from feersum_nlu.rest import ApiException

# Configure API key authorization: APIKeyHeader
feersum_nlu.configuration.api_key['AUTH_TOKEN'] = 'YOUR_API_KEY'

# feersum_nlu.configuration.host = "http://127.0.0.1:443/nlu/v2"
feersum_nlu.configuration.host = "http://nlu.playground.feersum.io:443/nlu/v2"

api_instance = feersum_nlu.RegexEntityExtractorsApi()

instance_name = 'test_regex_extr'

# Try both the year, make and model  &  the make, model, year regular expressions below.
# ToDo: Jeep Grand Cherokee !!!
# vehicle_make_reg_ex = "(Suzuki|Honda|Ford|VW|Jeep|Toyota|Fiat|Porsche|Nissan|Chev|Chevrolet|Datsun|Mitsubishi|Subaru)"
# regex_str = r"(?P<year>[0-9]{4})[.,\s]+(?P<make>" + vehicle_make_reg_ex + r")[.,\s]+(?P<model>\w+)"
# regex_str = r"(?P<make>" + vehicle_make_reg_ex + r")[.,\s]+(?P<model>\w+)[.,\s]+[.,\s\w]*?(?P<year>[0-9]{4})"

regex_str = (r"(?P<license>"
             r"([A-Z]{3}[ ]?[0-9]{3}[ ]?(GP|NW|MP|EC|L|NC|NW))|"
             r"([A-Z]{2}[ ]?[0-9]{2}[ ]?[A-Z]{2}[ ]?(GP|NW|MP|EC|L|NC|NW)))")

regex_ent_create_details = \
    feersum_nlu.RegexEntCreateDetails(name=instance_name, desc="Test regex extractor.",
                                      regex=regex_str,
                                      load_from_store=False)

# text_input = feersum_nlu.TextInput("My car has license number JMS 007 GP.")
text_input = feersum_nlu.TextInput("My car is a 2007 Jeep Wrangler with plate ZNX 450 GP")

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
