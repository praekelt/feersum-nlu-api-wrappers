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
from feersum_nlu.api.dashboard_api import DashboardApi  # noqa: E501
from feersum_nlu.rest import ApiException


class TestDashboardApi(unittest.TestCase):
    """DashboardApi unit test stubs"""

    def setUp(self):
        self.api = feersum_nlu.api.dashboard_api.DashboardApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_dashboard_audio_get_details(self):
        """Test case for dashboard_audio_get_details

        Your audio service dashboard. Same as POST endpoint, but doesn't allow params to be supplied to the operation.  # noqa: E501
        """
        pass

    def test_dashboard_audio_get_details_with_params(self):
        """Test case for dashboard_audio_get_details_with_params

        Your audio service dashboard. Same as GET endpoint, but allows params to be supplied to the operation.  # noqa: E501
        """
        pass

    def test_dashboard_get_details(self):
        """Test case for dashboard_get_details

        Your root service dashboard. Same as POST endpoint, but doesn't allow params to be supplied to the operation.  # noqa: E501
        """
        pass

    def test_dashboard_get_details_with_params(self):
        """Test case for dashboard_get_details_with_params

        Your root service dashboard. Same as GET endpoint, but allows params to be supplied to the operation.  # noqa: E501
        """
        pass

    def test_dashboard_nlu_get_details(self):
        """Test case for dashboard_nlu_get_details

        Your nlu service dashboard. Same as POST endpoint, but doesn't allow params to be supplied to the operation.  # noqa: E501
        """
        pass

    def test_dashboard_nlu_get_details_with_params(self):
        """Test case for dashboard_nlu_get_details_with_params

        Your nlu service dashboard. Same as GET endpoint, but allows params to be supplied to the operation.  # noqa: E501
        """
        pass

    def test_dashboard_vision_get_details(self):
        """Test case for dashboard_vision_get_details

        Your vision service dashboard. Same as POST endpoint, but doesn't allow params to be supplied to the operation.  # noqa: E501
        """
        pass

    def test_dashboard_vision_get_details_with_params(self):
        """Test case for dashboard_vision_get_details_with_params

        Your vision service dashboard. Same as GET endpoint, but allows params to be supplied to the operation.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
