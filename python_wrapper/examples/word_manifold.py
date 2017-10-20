import urllib3

import feersum_nlu
from feersum_nlu.rest import ApiException

# Configure API key authorization: APIKeyHeader
feersum_nlu.configuration.api_key['AUTH_TOKEN'] = 'YOUR_API_KEY'

# feersum_nlu.configuration.host = "http://127.0.0.1:443/nlu/v2"
feersum_nlu.configuration.host = "http://nlu.playground.feersum.io:443/nlu/v2"

api_instance = feersum_nlu.WordManifoldsApi()

instance_name = 'test_wm'
new_word_list = [{'new_word': 'chatbot', 'similar_to': 'robot'},
                 {'new_word': 'kapoen', 'similar_to': 'brown'}]  # NewWordList | List of new words.

new_word_list_b = [{'new_word': 'chatbots', 'similar_to': 'robots'},
                   {'new_word': 'shaki', 'similar_to': 'browb'}]  # NewWordList | List of new words.

create_details = feersum_nlu.CreateDetails(name=instance_name, desc="Test word manifold.",
                                           load_from_store=False, input_file="glove.6B.50d.trimmed.txt")
# create_details = feersum_nlu.CreateDetails(name=instance_name, load_from_store=True)

print()

try:
    print("Create the word manifold model:")
    api_response = api_instance.word_manifold_create(create_details)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    # print("Add some new words to the manifold and save the updated version:")
    # api_response = api_instance.word_manifold_add_similar_words(instance_name, new_word_list)
    # print(" type(api_response)", type(api_response))
    # print(" api_response", api_response)
    # print()
    #
    # print("Add some new words to the manifold and save the updated version:")
    # api_response = api_instance.word_manifold_add_similar_words(instance_name, new_word_list_b)
    # print(" type(api_response)", type(api_response))
    # print(" api_response", api_response)
    # print()

except ApiException as e:
    print("Exception when calling a word manifold operation: %s\n" % e)
except urllib3.exceptions.MaxRetryError:
    print("Connection MaxRetryError!")
