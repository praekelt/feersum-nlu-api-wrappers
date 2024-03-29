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
from feersum_nlu.api.health_api import HealthApi  # noqa: E501
from feersum_nlu.rest import ApiException


class TestHealthApi(unittest.TestCase):
    """HealthApi unit test stubs"""

    def setUp(self):
        self.api = feersum_nlu.api.health_api.HealthApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_health_get_status(self):
        """Test case for health_get_status

        An endpoint to check if the service is alive and well.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
