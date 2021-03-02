# coding: utf-8

from __future__ import absolute_import

import urllib3
import unittest

import feersum_nlu
from feersum_nlu.rest import ApiException
from test import feersumnlu_host, feersum_nlu_auth_token


class TestAPIKeyManagement(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_api_key_management(self):
        # Configure API key authorization: APIKeyHeader
        configuration = feersum_nlu.Configuration()

        # configuration.api_key['AUTH_TOKEN'] = feersum_nlu_auth_token
        configuration.api_key['X-Auth-Token'] = feersum_nlu_auth_token  # Alternative auth key header!

        configuration.host = feersumnlu_host

        api_instance = feersum_nlu.ApiKeysApi(feersum_nlu.ApiClient(configuration))

        print()

        api_key = feersum_nlu_auth_token
        print("api_key =", api_key)
        print()

        try:
            print("Get the details of specific named API key:")
            api_response = api_instance.api_key_get_details(api_key, x_caller='feersum_nlu_api_wrapper_test')
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            call_count_breakdown = api_response.call_count_breakdown

            api_key_get_details_call_count_0 = call_count_breakdown.get('api_key_get_details', 0)

            print("Get the details of specific named API key:")
            api_response = api_instance.api_key_get_details(api_key, x_caller='feersum_nlu_api_wrapper_test')
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            call_count_breakdown = api_response.call_count_breakdown
            api_key_get_details_call_count_1 = call_count_breakdown.get('api_key_get_details', 0)

            self.assertTrue((api_key_get_details_call_count_1 - api_key_get_details_call_count_0) >= 1)  # At least one call later.

        except ApiException as e:
            print("Exception when calling an api key operation: %s\n" % e)
            self.assertTrue(False)
        except urllib3.exceptions.HTTPError as e:
            print("Connection HTTPError! %s\n" % e)
            self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
