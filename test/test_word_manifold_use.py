# coding: utf-8

from __future__ import absolute_import

from typing import List

import urllib3
import unittest

import feersum_nlu
from feersum_nlu.rest import ApiException
from test import feersumnlu_host, feersum_nlu_auth_token


class TestWordManifold(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_word_manifold_use(self):
        # Configure API key authorization: APIKeyHeader
        configuration = feersum_nlu.Configuration()

        # configuration.api_key['AUTH_TOKEN'] = feersum_nlu_auth_token
        configuration.api_key['X-Auth-Token'] = feersum_nlu_auth_token  # Alternative auth key header!

        configuration.host = feersumnlu_host

        api_instance = feersum_nlu.WordManifoldsApi(feersum_nlu.ApiClient(configuration))

        # The already loaded word embedding to use.
        instance_name = 'feers_wm_eng'
        # The playground's pre-loaded embeddings include:
        # "feers_wm_afr", "feers_wm_eng", "feers_wm_nbl", "feers_wm_xho",
        # "feers_wm_zul", "feers_wm_ssw", "feers_wm_nso", "feers_wm_sot",
        # "feers_wm_tsn", "feers_wm_ven", "feers_wm_tso"
        # and "glove6B50D_trimmed"

        word_and_threshold = feersum_nlu.WordAndThreshold('cat', 0.65)

        try:
            print("Find words similar to:")
            api_response = api_instance.word_manifold_get_similar_words(instance_name, word_and_threshold)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            similar_words = []  # type: List[str]
            for word_dict in api_response:
                word = word_dict.word
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
