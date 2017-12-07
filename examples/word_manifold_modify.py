""" Example: Shows how to create & modify (requires special permission) as well as use word manifolds. """

import os
import urllib3

import feersum_nlu
from feersum_nlu.rest import ApiException

# Try to get the API key from your OS environment, else use 'YOUR_API_KEY' as the default value in the code below.
# You may use any environment variable you want, it doesn't have to be 'FEERSUM_NLU_AUTH_TOKEN'.
feersum_nlu_auth_token = os.environ.get('FEERSUM_NLU_AUTH_TOKEN', 'YOUR_API_KEY')
print('feersum_nlu_auth_token = ', feersum_nlu_auth_token)

# Configure API key authorization: APIKeyHeader
configuration = feersum_nlu.Configuration()
configuration.api_key['AUTH_TOKEN'] = feersum_nlu_auth_token

# configuration.host = "http://127.0.0.1:8100/nlu/v2"
configuration.host = "https://nlu.playground.feersum.io:443/nlu/v2"

api_instance = feersum_nlu.WordManifoldsApi(feersum_nlu.ApiClient(configuration))

instance_name = 'test_wm'
new_word_list = [{'new_word': 'chatbot', 'similar_to': 'robot'}]  # NewWordList | List of new words.

new_word_list_b = [{'new_word': 'chatbots', 'similar_to': 'robots'},
                   {'new_word': 'shaki', 'similar_to': 'brown'}]  # NewWordList | List of new words.

create_details = feersum_nlu.WmCreateDetails(name=instance_name,
                                             desc="Test word manifold.",
                                             word_vectors_file="glove.6B.50d.trimmed.txt",
                                             load_from_store=False)  # file present on server

# create_details = feersum_nlu.WmCreateDetails(name=instance_name, load_from_store=True)

print()

try:
    print("Create the word manifold model:")
    api_response = api_instance.word_manifold_create(create_details)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Add some new words to the manifold and save the updated version:")
    api_response = api_instance.word_manifold_add_similar_words(instance_name, new_word_list)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Add some new words to the manifold and save the updated version:")
    api_response = api_instance.word_manifold_add_similar_words(instance_name, new_word_list_b)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

except ApiException as e:
    print("Exception when calling a word manifold operation: %s\n" % e)
except urllib3.exceptions.MaxRetryError:
    print("Connection MaxRetryError!")
