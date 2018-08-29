# coding: utf-8

from __future__ import absolute_import

import urllib3
import unittest

import feersum_nlu
from feersum_nlu.rest import ApiException
from test import feersumnlu_host, feersum_nlu_auth_token


class TestSentiment(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_sentiment(self):
        # Configure API key authorization: APIKeyHeader
        configuration = feersum_nlu.Configuration()

        # configuration.api_key['AUTH_TOKEN'] = feersum_nlu_auth_token
        configuration.api_key['X-Auth-Token'] = feersum_nlu_auth_token  # Alternative auth key header!

        configuration.host = feersumnlu_host

        api_instance = feersum_nlu.SentimentDetectorsApi(feersum_nlu.ApiClient(configuration))

        model_instance_name = 'generic'
        text_input = feersum_nlu.TextInput("I am very happy. Why are you unhappy?")  # TextInput | The input text.

        print()

        try:
            print("Detect sentiment:")
            api_response = api_instance.sentiment_detector_retrieve(model_instance_name, text_input)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            self.assertTrue(0.25 < api_response.value < 0.35)

        except ApiException as e:
            print("Exception when calling SentimentDetectorsApi->sentiment_detector_retrieve: %s\n" % e)
            self.assertTrue(False)
        except urllib3.exceptions.MaxRetryError:
            print("Connection MaxRetryError!")
            self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
