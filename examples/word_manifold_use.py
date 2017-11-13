""" Example: Shows how to create and use word manifolds. """

import os
import urllib3

import feersum_nlu
from feersum_nlu.rest import ApiException

# Try to get the API key from your OS environment, else use 'YOUR_API_KEY' as the default value in the code below.
# You may use any environment variable you want, it doesn't have to be 'FEERSUM_NLU_AUTH_TOKEN'.
feersum_nlu_auth_token = os.environ.get('FEERSUM_NLU_AUTH_TOKEN', 'YOUR_API_KEY')
print('feersum_nlu_auth_token = ', feersum_nlu_auth_token)

# Configure API key authorization: APIKeyHeader
feersum_nlu.configuration.api_key['AUTH_TOKEN'] = feersum_nlu_auth_token

# feersum_nlu.configuration.host = "http://127.0.0.1:8100/nlu/v2"
feersum_nlu.configuration.host = "https://nlu.playground.feersum.io:443/nlu/v2"

api_instance = feersum_nlu.WordManifoldsApi()

# The already loaded word embedding to use.
instance_name = 'feers_wm_eng'
# The playground's pre-loaded embeddings include:
# "feers_wm_afr", "feers_wm_eng", "feers_wm_nbl", "feers_wm_xho",
# "feers_wm_zul", "feers_wm_ssw", "feers_wm_nso", "feers_wm_sot",
# "feers_wm_tsn", "feers_wm_ven", "feers_wm_tso"

word_and_threshold = feersum_nlu.WordAndThreshold('cat', 0.65)
misspelt_word = feersum_nlu.TextInput('hospitle')

try:
    print("Find words similar to:")
    api_response = api_instance.word_manifold_get_similar_words(instance_name, word_and_threshold)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Spell correct:")
    api_response = api_instance.word_manifold_spell_correct(instance_name, misspelt_word)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

except ApiException as e:
    print("Exception when calling a word manifold operation: %s\n" % e)
except urllib3.exceptions.MaxRetryError:
    print("Connection MaxRetryError!")
