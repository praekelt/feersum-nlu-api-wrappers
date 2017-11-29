# coding: utf-8

from __future__ import absolute_import

import os
import urllib3
import unittest

import feersum_nlu
from feersum_nlu.rest import ApiException


class TestWordManifold(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_word_manifold_use(self):
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

        try:
            print("Find words similar to:")
            api_response = api_instance.word_manifold_get_similar_words(instance_name, word_and_threshold)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            similar_words = []  # type: List[str]
            for word_dict in api_response:
                word = word_dict.get('word')
                if word is not None:
                    similar_words.append(word)

            self.assertTrue(similar_words == ['cat', 'dog', 'cats', 'pet'])

        except ApiException as e:
            print("Exception when calling a word manifold operation: %s\n" % e)
            self.assertTrue(False)
        except urllib3.exceptions.MaxRetryError:
            print("Connection MaxRetryError!")
            self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
