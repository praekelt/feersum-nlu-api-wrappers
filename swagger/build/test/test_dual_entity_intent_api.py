# coding: utf-8

"""
    FeersumNLU API

    This is the HTTP API for Feersum NLU. See https://github.com/praekelt/feersum-nlu-api-wrappers for examples of how to use the API.  # noqa: E501

    OpenAPI spec version: 2.0.55
    Contact: nlu@feersum.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import feersum_nlu
from feersum_nlu.api.dual_entity_intent_api import DualEntityIntentApi  # noqa: E501
from feersum_nlu.rest import ApiException


class TestDualEntityIntentApi(unittest.TestCase):
    """DualEntityIntentApi unit test stubs"""

    def setUp(self):
        self.api = feersum_nlu.api.dual_entity_intent_api.DualEntityIntentApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_dual_entity_intent_add_testing_samples(self):
        """Test case for dual_entity_intent_add_testing_samples

        Add testing samples.  # noqa: E501
        """
        pass

    def test_dual_entity_intent_add_training_samples(self):
        """Test case for dual_entity_intent_add_training_samples

        Add training samples.  # noqa: E501
        """
        pass

    def test_dual_entity_intent_create(self):
        """Test case for dual_entity_intent_create

        Create an dual_entity_intent model.  # noqa: E501
        """
        pass

    def test_dual_entity_intent_create_from_path(self):
        """Test case for dual_entity_intent_create_from_path

        Create a dual_entity_intent model.  # noqa: E501
        """
        pass

    def test_dual_entity_intent_del(self):
        """Test case for dual_entity_intent_del

        Delete named instance.  # noqa: E501
        """
        pass

    def test_dual_entity_intent_del_testing_samples(self):
        """Test case for dual_entity_intent_del_testing_samples

        Delete testing samples.  # noqa: E501
        """
        pass

    def test_dual_entity_intent_del_testing_samples_all(self):
        """Test case for dual_entity_intent_del_testing_samples_all

        Delete all testing samples.  # noqa: E501
        """
        pass

    def test_dual_entity_intent_del_training_samples(self):
        """Test case for dual_entity_intent_del_training_samples

        Delete training samples.  # noqa: E501
        """
        pass

    def test_dual_entity_intent_del_training_samples_all(self):
        """Test case for dual_entity_intent_del_training_samples_all

        Delete all training samples.  # noqa: E501
        """
        pass

    def test_dual_entity_intent_get_details(self):
        """Test case for dual_entity_intent_get_details

        Get details of named instance.  # noqa: E501
        """
        pass

    def test_dual_entity_intent_get_details_all(self):
        """Test case for dual_entity_intent_get_details_all

        Get list of dual_entity_intent models.  # noqa: E501
        """
        pass

    def test_dual_entity_intent_get_labels(self):
        """Test case for dual_entity_intent_get_labels

        Get list of possible labels.  # noqa: E501
        """
        pass

    def test_dual_entity_intent_get_params(self):
        """Test case for dual_entity_intent_get_params

        Get the editable model parameters of named dual_entity_intent model.  # noqa: E501
        """
        pass

    def test_dual_entity_intent_get_testing_samples(self):
        """Test case for dual_entity_intent_get_testing_samples

        Get testing samples.  # noqa: E501
        """
        pass

    def test_dual_entity_intent_get_training_samples(self):
        """Test case for dual_entity_intent_get_training_samples

        Get training samples.  # noqa: E501
        """
        pass

    def test_dual_entity_intent_retrieve(self):
        """Test case for dual_entity_intent_retrieve

        Classify entity_intent.  # noqa: E501
        """
        pass

    def test_dual_entity_intent_set_params(self):
        """Test case for dual_entity_intent_set_params

        Set the model parameters of named dual_entity_intent model.  # noqa: E501
        """
        pass

    def test_dual_entity_intent_test(self):
        """Test case for dual_entity_intent_test

        Test the named dual_entity_intent model.  # noqa: E501
        """
        pass

    def test_dual_entity_intent_train(self):
        """Test case for dual_entity_intent_train

        Train the named dual_entity_intent model.  # noqa: E501
        """
        pass

    def test_dual_entity_intent_update_testing_samples(self):
        """Test case for dual_entity_intent_update_testing_samples

        Update testning samples by UUID.  # noqa: E501
        """
        pass

    def test_dual_entity_intent_update_training_samples(self):
        """Test case for dual_entity_intent_update_training_samples

        Update training samples by UUID.  # noqa: E501
        """
        pass

    def test_dual_entity_intent_vaporise(self):
        """Test case for dual_entity_intent_vaporise

        Vaporise the named model.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
