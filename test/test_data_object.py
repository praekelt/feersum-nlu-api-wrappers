# coding: utf-8

from __future__ import absolute_import

import urllib3
import unittest

import feersum_nlu
from feersum_nlu.rest import ApiException
from test import feersumnlu_host, feersum_nlu_auth_token

import uuid


# curl -XGET -is "https://nlu.playground.feersum.io:443/nlu/v2/data_objects" \
# -H "X-Auth-Token: 6847a0a3-169d-4f7a-8eb1-737c9f6e9ffd" \
# -H "accept: application/json" \
# -H "content-type: application/json"

# curl -XGET -is "https://nlu.playground.feersum.io:443/nlu/v2/data_objects/john@feersum.io" \
# -H "X-Auth-Token: 6847a0a3-169d-4f7a-8eb1-737c9f6e9ffd" \
# -H "accept: application/json" \
# -H "content-type: application/json"

class TestDataObject(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_data_object(self):
        # Configure API key authorization: APIKeyHeader
        configuration = feersum_nlu.Configuration()

        # configuration.api_key['AUTH_TOKEN'] = feersum_nlu_auth_token
        configuration.api_key['X-Auth-Token'] = feersum_nlu_auth_token  # Alternative auth key header!

        configuration.host = feersumnlu_host

        api_instance = feersum_nlu.DataObjectsApi(feersum_nlu.ApiClient(configuration))

        instance_name = 'test_data_object_' + str(uuid.uuid4())
        data = {"key0": [0, 1, 2], "key1": "value1"}

        print()

        try:
            print("Create the data_object:")
            api_response = api_instance.data_object_post(instance_name, data)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Get the names of all loaded data_objects:")
            api_response = api_instance.data_object_get_names_all()
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Get the details of specific named loaded data_object:")
            api_response = api_instance.data_object_get_details(instance_name)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Get the named data_object:")
            api_response = api_instance.data_object_get_details(instance_name)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Delete named loaded data_object:")
            api_response = api_instance.data_object_del(instance_name)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Vaporise named loaded data_object:")
            api_response = api_instance.data_object_vaporise(instance_name)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

        except ApiException as e:
            print("Exception when calling a entity extractor operation: %s\n" % e)
            self.assertTrue(False)
        except urllib3.exceptions.MaxRetryError:
            print("Connection MaxRetryError!")
            self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
