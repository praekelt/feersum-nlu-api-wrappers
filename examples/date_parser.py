""" Example: Shows how to use the simple date parser. """

import urllib3

import feersum_nlu
from feersum_nlu.rest import ApiException
from examples import feersumnlu_host, feersum_nlu_auth_token

# Configure API key authorization: APIKeyHeader
configuration = feersum_nlu.Configuration()

# configuration.api_key['AUTH_TOKEN'] = feersum_nlu_auth_token
configuration.api_key['X-Auth-Token'] = feersum_nlu_auth_token  # Alternative auth key header!

configuration.host = feersumnlu_host

api_instance = feersum_nlu.DateParsersApi(feersum_nlu.ApiClient(configuration))

model_instance_name = 'generic'
text_input = feersum_nlu.TextInput("The day after tomorrow at 11:00 in the evening.")  # TextInput | The input text.

print()

try:
    print("Extract dates:")
    api_response = api_instance.date_parser_retrieve(model_instance_name, text_input)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()
except ApiException as e:
    print("Exception when calling DateParsersApi->date_parser_retrieve: %s\n" % e)
except urllib3.exceptions.HTTPError as e:
    print("Connection HTTPError! %s\n" % e)
