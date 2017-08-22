import urllib3

import feersum_nlu
from feersum_nlu.rest import ApiException

# Configure API key authorization: APIKeyHeader
feersum_nlu.configuration.api_key['AUTH_TOKEN'] = 'YOUR_API_KEY'

feersum_nlu.configuration.host = "http://127.0.0.1:8000/nlu/v2"
# feersum_nlu.configuration.host = "http://dev-bernardt.za.prk.hosting:8000/nlu/v2"

api_instance = feersum_nlu.DateParsersApi()

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
except urllib3.exceptions.MaxRetryError:
    print("Connection MaxRetryError!")

