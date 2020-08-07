# coding: utf-8

from __future__ import absolute_import

import urllib3
import unittest

import feersum_nlu
from feersum_nlu.rest import ApiException
from test import feersumnlu_host, feersum_nlu_auth_token

import uuid


@unittest.skip("skipping while GCP model on earlier version of PyTorch")
class TestEmotion(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_emotion(self):
        # Configure API key authorization: APIKeyHeader
        configuration = feersum_nlu.Configuration()

        # configuration.api_key['AUTH_TOKEN'] = feersum_nlu_auth_token
        configuration.api_key['X-Auth-Token'] = feersum_nlu_auth_token  # Alternative auth key header!

        configuration.host = feersumnlu_host

        api_instance = feersum_nlu.EmotionClassifiersApi(feersum_nlu.ApiClient(configuration))

        model_instance_name = 'generic_' + str(uuid.uuid4())
        text_input = feersum_nlu.TextInput("I am very happy to hear that?")  # TextInput | The input text.

        print()

        try:
            print("Classify emotion:")
            api_response = api_instance.emotion_classifier_retrieve(model_instance_name, text_input)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            self.assertTrue(api_response[0].label == 'joy')
            self.assertTrue(api_response[0].probability > 0.5)

        except ApiException as e:
            print("Exception when calling EmotionClassifiersApi->emotion_classifier_retrieve: %s\n" % e)
            self.assertTrue(False)
        except urllib3.exceptions.MaxRetryError:
            print("Connection MaxRetryError!")
            self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
