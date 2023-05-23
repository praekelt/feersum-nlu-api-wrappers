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
from feersum_nlu.api.language_recognisers_api import LanguageRecognisersApi  # noqa: E501
from feersum_nlu.rest import ApiException


class TestLanguageRecognisersApi(unittest.TestCase):
    """LanguageRecognisersApi unit test stubs"""

    def setUp(self):
        self.api = feersum_nlu.api.language_recognisers_api.LanguageRecognisersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_language_recogniser_create(self):
        """Test case for language_recogniser_create

        Create a text language detector.  # noqa: E501
        """
        pass

    def test_language_recogniser_del(self):
        """Test case for language_recogniser_del

        Delete named instance.  # noqa: E501
        """
        pass

    def test_language_recogniser_get_details(self):
        """Test case for language_recogniser_get_details

        Get details of named instance.  # noqa: E501
        """
        pass

    def test_language_recogniser_get_details_all(self):
        """Test case for language_recogniser_get_details_all

        Get list of text language detectors.  # noqa: E501
        """
        pass

    def test_language_recogniser_get_labels(self):
        """Test case for language_recogniser_get_labels

        Get list of possible labels.  # noqa: E501
        """
        pass

    def test_language_recogniser_get_params(self):
        """Test case for language_recogniser_get_params

        Get the editable model parameters of named language recogniser.  # noqa: E501
        """
        pass

    def test_language_recogniser_retrieve(self):
        """Test case for language_recogniser_retrieve

        Recognise the language the text is written in.  # noqa: E501
        """
        pass

    def test_language_recogniser_set_params(self):
        """Test case for language_recogniser_set_params

        Set the model parameters of named language recogniser.  # noqa: E501
        """
        pass

    def test_language_recogniser_vaporise(self):
        """Test case for language_recogniser_vaporise

        Vaporise the named model.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
