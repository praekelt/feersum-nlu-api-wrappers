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
from feersum_nlu.api.synonym_entity_extractors_api import SynonymEntityExtractorsApi  # noqa: E501
from feersum_nlu.rest import ApiException


class TestSynonymEntityExtractorsApi(unittest.TestCase):
    """SynonymEntityExtractorsApi unit test stubs"""

    def setUp(self):
        self.api = feersum_nlu.api.synonym_entity_extractors_api.SynonymEntityExtractorsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_synonym_entity_extractor_add_testing_samples(self):
        """Test case for synonym_entity_extractor_add_testing_samples

        Add testing samples.  # noqa: E501
        """
        pass

    def test_synonym_entity_extractor_add_training_samples(self):
        """Test case for synonym_entity_extractor_add_training_samples

        Add training samples.  # noqa: E501
        """
        pass

    def test_synonym_entity_extractor_create(self):
        """Test case for synonym_entity_extractor_create

        Create a synonym entity extractor.  # noqa: E501
        """
        pass

    def test_synonym_entity_extractor_del(self):
        """Test case for synonym_entity_extractor_del

        Delete named instance.  # noqa: E501
        """
        pass

    def test_synonym_entity_extractor_del_testing_samples(self):
        """Test case for synonym_entity_extractor_del_testing_samples

        Delete testing samples.  # noqa: E501
        """
        pass

    def test_synonym_entity_extractor_del_testing_samples_all(self):
        """Test case for synonym_entity_extractor_del_testing_samples_all

        Delete all testing samples.  # noqa: E501
        """
        pass

    def test_synonym_entity_extractor_del_training_samples(self):
        """Test case for synonym_entity_extractor_del_training_samples

        Delete training samples.  # noqa: E501
        """
        pass

    def test_synonym_entity_extractor_del_training_samples_all(self):
        """Test case for synonym_entity_extractor_del_training_samples_all

        Delete all training samples.  # noqa: E501
        """
        pass

    def test_synonym_entity_extractor_get_details(self):
        """Test case for synonym_entity_extractor_get_details

        Get details of named instance.  # noqa: E501
        """
        pass

    def test_synonym_entity_extractor_get_details_all(self):
        """Test case for synonym_entity_extractor_get_details_all

        Get list of synonym entity extractors.  # noqa: E501
        """
        pass

    def test_synonym_entity_extractor_get_labels(self):
        """Test case for synonym_entity_extractor_get_labels

        Get list of possible labels.  # noqa: E501
        """
        pass

    def test_synonym_entity_extractor_get_params(self):
        """Test case for synonym_entity_extractor_get_params

        Get the editable model parameters of named synonym entity extractor.  # noqa: E501
        """
        pass

    def test_synonym_entity_extractor_get_testing_samples(self):
        """Test case for synonym_entity_extractor_get_testing_samples

        Get testing samples.  # noqa: E501
        """
        pass

    def test_synonym_entity_extractor_get_training_samples(self):
        """Test case for synonym_entity_extractor_get_training_samples

        Get training samples.  # noqa: E501
        """
        pass

    def test_synonym_entity_extractor_retrieve(self):
        """Test case for synonym_entity_extractor_retrieve

        Predict which entities was mentioned.  # noqa: E501
        """
        pass

    def test_synonym_entity_extractor_set_params(self):
        """Test case for synonym_entity_extractor_set_params

        Set the model parameters of named synonym entity extractor.  # noqa: E501
        """
        pass

    def test_synonym_entity_extractor_test(self):
        """Test case for synonym_entity_extractor_test

        Test the named synonym entity extractor.  # noqa: E501
        """
        pass

    def test_synonym_entity_extractor_train(self):
        """Test case for synonym_entity_extractor_train

        Train the named synonym extractor.  # noqa: E501
        """
        pass

    def test_synonym_entity_extractor_update_testing_samples(self):
        """Test case for synonym_entity_extractor_update_testing_samples

        Update testing samples by UUID.  # noqa: E501
        """
        pass

    def test_synonym_entity_extractor_update_training_samples(self):
        """Test case for synonym_entity_extractor_update_training_samples

        Update training samples by UUID.  # noqa: E501
        """
        pass

    def test_synonym_entity_extractor_vaporise(self):
        """Test case for synonym_entity_extractor_vaporise

        Vaporise the named model.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
