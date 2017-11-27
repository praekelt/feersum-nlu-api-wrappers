# coding: utf-8

from __future__ import absolute_import

import os
import urllib3
import unittest

import feersum_nlu
from feersum_nlu.rest import ApiException


class TestDucklingExtractor(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_duckling_extractor(self):
        # Try to get the API key from your OS environment, else use 'YOUR_API_KEY' as the default value in the code below.
        # You may use any environment variable you want, it doesn't have to be 'FEERSUM_NLU_AUTH_TOKEN'.
        feersum_nlu_auth_token = os.environ.get('FEERSUM_NLU_AUTH_TOKEN', 'YOUR_API_KEY')
        print('feersum_nlu_auth_token = ', feersum_nlu_auth_token)

        # Configure API key authorization: APIKeyHeader
        feersum_nlu.configuration.api_key['AUTH_TOKEN'] = feersum_nlu_auth_token

        # feersum_nlu.configuration.host = "http://127.0.0.1:8100/nlu/v2"
        feersum_nlu.configuration.host = "https://nlu.playground.feersum.io:443/nlu/v2"

        api_instance = feersum_nlu.DucklingEntityExtractorsApi()

        instance_name = 'test_duckling_extr'

        duckling_ent_create_details = \
            feersum_nlu.DucklingEntCreateDetails(name=instance_name, desc="Test duckling extractor.",
                                                 load_from_store=False)

        text_input = feersum_nlu.TextInput("I was 3 weeks pregnant one month ago.")

        print()

        try:
            print("Create the entity extractor:")
            api_response = api_instance.duckling_entity_extractor_create(duckling_ent_create_details)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Get the details of all loaded entity extractors:")
            api_response = api_instance.duckling_entity_extractor_get_details_all()
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Get the details of specific named loaded entity extractor:")
            api_response = api_instance.duckling_entity_extractor_get_details(instance_name)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Extract entities:")
            api_response = api_instance.duckling_entity_extractor_retrieve(instance_name, text_input)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            entity_list = api_response
            if len(entity_list) > 0:
                entity = entity_list[0]
                self.assertTrue(entity.get('value', '') == '2017-10-27T00:00:00.000+02:00')
            else:
                self.assertTrue(False)

        except ApiException as e:
            print("Exception when calling a entity extractor operation: %s\n" % e)
            self.assertTrue(False)
        except urllib3.exceptions.MaxRetryError:
            print("Connection MaxRetryError!")
            self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
