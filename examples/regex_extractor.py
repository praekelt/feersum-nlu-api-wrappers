""" Example: Shows how the RegEx entity extractor may be used. """

import urllib3

import feersum_nlu
from feersum_nlu.rest import ApiException
from examples import feersumnlu_host, feersum_nlu_auth_token

# Configure API key authorization: APIKeyHeader
configuration = feersum_nlu.Configuration()

# configuration.api_key['AUTH_TOKEN'] = feersum_nlu_auth_token
configuration.api_key['X-Auth-Token'] = feersum_nlu_auth_token  # Alternative auth key header!

configuration.host = feersumnlu_host

api_instance = feersum_nlu.RegexEntityExtractorsApi(feersum_nlu.ApiClient(configuration))

instance_name = 'test_regex_extr'

# Try both the year, make and model  &  the make, model, year regular expressions below.
# ToDo: Jeep Grand Cherokee !!!
vehicle_make_reg_ex = "(Suzuki|Honda|Ford|VW|Jeep|Toyota|Fiat|Porsche|Nissan|Chev|Chevrolet|Datsun|Mitsubishi|Subaru)"
# regex_str = r"(?P<year>[0-9]{4})[.,\s]+(?P<make>" + vehicle_make_reg_ex + r")[.,\s]+(?P<model>\w+)"
# regex_str = r"(?P<make>" + vehicle_make_reg_ex + r")[.,\s]+(?P<model>\w+)[.,\s]+[.,\s\w]*?(?P<year>[0-9]{4})"

regex_str = r"(?P<ID>(\b[0-9]{13}\b))"
# regex_str = (r"(?P<license>"
#              r"([A-Z]{3}[ ]?[0-9]{3}[ ]?(GP|NW|MP|EC|L|NC|NW))|"
#              r"([A-Z]{2}[ ]?[0-9]{2}[ ]?[A-Z]{2}[ ]?(GP|NW|MP|EC|L|NC|NW)))")

regex_ent_create_details = \
    feersum_nlu.RegexEntityExtractorCreateDetails(name=instance_name,
                                                  desc="Test ID extractor.",
                                                  regex=regex_str,
                                                  load_from_store=False)

text_input = feersum_nlu.TextInput("My ID number is 1234567890123.")
# text_input = feersum_nlu.TextInput("My car has license number JMS 007 GP.")
#    api_response [{'_all_groups': 'JMS 007 GP', 'license': 'JMS 007 GP'}]
# text_input = feersum_nlu.TextInput("My car is a 2007 Jeep Wrangler with plate AB 34 EF GP")
#    api_response [{'_all_groups': 'AB 34 EF GP', 'license': 'AB 34 EF GP'}]

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

    print("Get the parameters:")
    api_response = api_instance.regex_entity_extractor_get_params(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Update the parameters:")
    model_params = \
        feersum_nlu.ModelParams(regex=r"(?P<ID>(\b[0-9]{12}\b))")
    api_response = api_instance.regex_entity_extractor_set_params(instance_name, model_params)
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

    print("Delete named loaded entity extractor:")
    api_response = api_instance.regex_entity_extractor_del(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Vaporise named loaded entity extractor:")
    api_response = api_instance.regex_entity_extractor_vaporise(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

except ApiException as e:
    print("Exception when calling a entity extractor operation: %s\n" % e)
except urllib3.exceptions.HTTPError as e:
    print("Connection HTTPError! %s\n" % e)
