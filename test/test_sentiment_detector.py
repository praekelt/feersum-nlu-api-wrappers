# coding: utf-8

from __future__ import absolute_import

import os
import urllib3
import unittest

import feersum_nlu
from feersum_nlu.rest import ApiException


class TestSentiment(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_sentiment(self):
        # Try to get the API key from your OS environment, else use 'YOUR_API_KEY' as the default value in the code below.
        # You may use any environment variable you want, it doesn't have to be 'FEERSUM_NLU_AUTH_TOKEN'.
        feersum_nlu_auth_token = os.environ.get('FEERSUM_NLU_AUTH_TOKEN', 'YOUR_API_KEY')
        print('feersum_nlu_auth_token = ', feersum_nlu_auth_token)

        # Configure API key authorization: APIKeyHeader
        feersum_nlu.configuration.api_key['AUTH_TOKEN'] = feersum_nlu_auth_token

        # feersum_nlu.configuration.host = "http://127.0.0.1:8100/nlu/v2"
        feersum_nlu.configuration.host = "https://nlu.playground.feersum.io:443/nlu/v2"

        api_instance = feersum_nlu.SentimentDetectorsApi()

        model_instance_name = 'generic'
        text_input = feersum_nlu.TextInput("I am very happy.")  # TextInput | The input text.

        print()

        try:
            print("Detect sentiment:")
            api_response = api_instance.sentiment_detector_retrieve(model_instance_name, text_input)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            self.assertTrue(0.5 < api_response.value < 0.75)

        except ApiException as e:
            print("Exception when calling SentimentDetectorsApi->sentiment_detector_retrieve: %s\n" % e)
            self.assertTrue(False)
        except urllib3.exceptions.MaxRetryError:
            print("Connection MaxRetryError!")
            self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
