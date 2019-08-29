""" Test the RegEx entity extractor. """

# coding: utf-8

from __future__ import absolute_import

import unittest
import urllib3

from examples import feersumnlu_host, feersum_nlu_auth_token
import feersum_nlu
from feersum_nlu.rest import ApiException
from test import feersumnlu_host, feersum_nlu_auth_token

import uuid


class TestRegex(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_regex(self):
        # Configure API key authorization: APIKeyHeader
        configuration = feersum_nlu.Configuration()

        # configuration.api_key['AUTH_TOKEN'] = feersum_nlu_auth_token
        configuration.api_key['X-Auth-Token'] = feersum_nlu_auth_token  # Alternative auth key header!

        configuration.host = feersumnlu_host

        api_instance = feersum_nlu.RegexEntityExtractorsApi(feersum_nlu.ApiClient(configuration))

        instance_name = 'test_regex_extr_' + str(uuid.uuid4())

        regex_str = r"(?P<ID>(\b[0-9]{13}\b))"

        regex_ent_create_details = \
            feersum_nlu.RegexEntityExtractorCreateDetails(name=instance_name,
                                                          desc="Test ID extractor.",
                                                          regex=regex_str,
                                                          load_from_store=False)

        text_input = feersum_nlu.TextInput("My ID number is 1234567890123.")

        print()

        try:
            print("Create the entity extractor:")
            api_response = api_instance.regex_entity_extractor_create(regex_ent_create_details)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Get the details of all loaded entity extractors:")
            api_response = api_instance.regex_entity_extractor_get_details_all()
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Get the details of specific named loaded entity extractor:")
            api_response = api_instance.regex_entity_extractor_get_details(instance_name)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Extract entities:")
            api_response = api_instance.regex_entity_extractor_retrieve(instance_name, text_input)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            self.assertTrue(api_response == [{'ID': '1234567890123', '_all_groups': '1234567890123'}])

            print("Delete named loaded entity extractor:")
            api_response = api_instance.regex_entity_extractor_del(instance_name)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Vaporise named loaded entity extractor:")
            api_response = api_instance.regex_entity_extractor_vaporise(instance_name)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

        except ApiException as e:
            print("Exception when calling a entity extractor operation: %s\n" % e)
            self.assertTrue(False)
        except urllib3.exceptions.HTTPError as e:
            print("Connection HTTPError! %s\n" % e)
            self.assertTrue(False)
