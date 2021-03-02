# coding: utf-8

from __future__ import absolute_import

import urllib3
import unittest

import feersum_nlu
from feersum_nlu.rest import ApiException
from test import feersumnlu_host, feersum_nlu_auth_token


class TestDashboard(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_dashboard(self):
        # Configure API key authorization: APIKeyHeader
        configuration = feersum_nlu.Configuration()

        # configuration.api_key['AUTH_TOKEN'] = feersum_nlu_auth_token
        configuration.api_key['X-Auth-Token'] = feersum_nlu_auth_token  # Alternative auth key header!

        configuration.host = feersumnlu_host

        api_instance = feersum_nlu.DashboardApi(feersum_nlu.ApiClient(configuration))

        print()

        try:
            print("Get dashboard content:")
            api_response, api_response_code, api_response_header = \
                api_instance.dashboard_nlu_get_details_with_http_info(x_caller='feersum_nlu_api_wrapper_test')

            print(api_response)

            print("api_response.api_version =", api_response.api_version)
            self.assertTrue(api_response.api_version == "2.0.54.dev1")

            print(" api_response_header", api_response_header)
            print(" calls remaining in this cycle ('-1' means no limit) =", api_response_header.get("X-RateLimit-Remaining"))

            self.assertTrue(api_response_header.get("X-Ratelimit-Remaining") == "-1")

        except ApiException as e:
            print("Exception when calling a entity extractor operation: %s\n" % e)
            self.assertTrue(False)
        except urllib3.exceptions.MaxRetryError:
            print("Connection MaxRetryError!")
            self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
