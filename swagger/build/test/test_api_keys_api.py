# coding: utf-8

"""
    FeersumNLU API

    This is the HTTP API for Feersum NLU. See https://github.com/praekelt/feersum-nlu-api-wrappers for examples of how to use the API.  # noqa: E501

    OpenAPI spec version: 2.0.54.dev2
    Contact: nlu@feersum.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import feersum_nlu
from feersum_nlu.api.api_keys_api import ApiKeysApi  # noqa: E501
from feersum_nlu.rest import ApiException


class TestApiKeysApi(unittest.TestCase):
    """ApiKeysApi unit test stubs"""

    def setUp(self):
        self.api = feersum_nlu.api.api_keys_api.ApiKeysApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_key_create(self):
        """Test case for api_key_create

        Create an API key.  # noqa: E501
        """
        pass

    def test_api_key_del(self):
        """Test case for api_key_del

        Delete named API key.  # noqa: E501
        """
        pass

    def test_api_key_get_details(self):
        """Test case for api_key_get_details

        Get details of named API key.  # noqa: E501
        """
        pass

    def test_api_key_get_details_all(self):
        """Test case for api_key_get_details_all

        Get list of API keys. Admin rights are required to get the full list of API keys.  # noqa: E501
        """
        pass

    def test_api_key_update_details(self):
        """Test case for api_key_update_details

        Update the details of named API key. Adds the key if not found. Admin rights are required to update details.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()