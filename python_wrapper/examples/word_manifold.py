import urllib3

import feersum_nlu
from feersum_nlu.rest import ApiException

# Configure API key authorization: APIKeyHeader
feersum_nlu.configuration.api_key['AUTH_TOKEN'] = 'YOUR_API_KEY'

feersum_nlu.configuration.host = "http://127.0.0.1:8000/nlu/v2"
# feersum_nlu.configuration.host = "http://dev-bernardt.za.prk.hosting:8000/nlu/v2"

api_instance = feersum_nlu.WordManifoldsApi()

instance_name = 'test_wm'

create_details = feersum_nlu.CreateDetails(name=instance_name, desc="Test word manifold.",
                                           load_from_store=False, input_file="glove.6B.200d.txt")
# create_details = feersum_nlu.CreateDetails(name=instance_name, load_from_store=True)

print()

try:
    print("Create the word manifold model:")
    api_response = api_instance.word_manifold_create(create_details)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()
except ApiException as e:
    print("Exception when calling a word manifold operation: %s\n" % e)
except urllib3.exceptions.MaxRetryError:
    print("Connection MaxRetryError!")

