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
from feersum_nlu.api.regex_entity_extractors_api import RegexEntityExtractorsApi  # noqa: E501
from feersum_nlu.rest import ApiException


class TestRegexEntityExtractorsApi(unittest.TestCase):
    """RegexEntityExtractorsApi unit test stubs"""

    def setUp(self):
        self.api = feersum_nlu.api.regex_entity_extractors_api.RegexEntityExtractorsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_regex_entity_extractor_create(self):
        """Test case for regex_entity_extractor_create

        Create a regular expression entity extractor.  # noqa: E501
        """
        pass

    def test_regex_entity_extractor_del(self):
        """Test case for regex_entity_extractor_del

        Delete named instance.  # noqa: E501
        """
        pass

    def test_regex_entity_extractor_get_details(self):
        """Test case for regex_entity_extractor_get_details

        Get details of named instance.  # noqa: E501
        """
        pass

    def test_regex_entity_extractor_get_details_all(self):
        """Test case for regex_entity_extractor_get_details_all

        Get list of regular expression entity extractors.  # noqa: E501
        """
        pass

    def test_regex_entity_extractor_get_params(self):
        """Test case for regex_entity_extractor_get_params

        Get the editable model parameters of named regex entity extractor.  # noqa: E501
        """
        pass

    def test_regex_entity_extractor_retrieve(self):
        """Test case for regex_entity_extractor_retrieve

        Extract information based on the regular expression.  # noqa: E501
        """
        pass

    def test_regex_entity_extractor_set_params(self):
        """Test case for regex_entity_extractor_set_params

        Set the model parameters of named regex entity extractor.  # noqa: E501
        """
        pass

    def test_regex_entity_extractor_vaporise(self):
        """Test case for regex_entity_extractor_vaporise

        Vaporise the named model.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()