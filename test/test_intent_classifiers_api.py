# coding: utf-8

"""
    FeersumNLU API

    This is the HTTP API for Feersum NLU. See https://github.com/praekelt/feersum-nlu-api-wrappers for examples of how to use the API.

    OpenAPI spec version: 2.0.3
    Contact: nlu@feersum.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import os
import sys
import unittest

import feersum_nlu
from feersum_nlu.rest import ApiException
from feersum_nlu.apis.intent_classifiers_api import IntentClassifiersApi


class TestIntentClassifiersApi(unittest.TestCase):
    """ IntentClassifiersApi unit test stubs """

    def setUp(self):
        self.api = feersum_nlu.apis.intent_classifiers_api.IntentClassifiersApi()

    def tearDown(self):
        pass

    def test_intent_classifier_add_training_samples(self):
        """
        Test case for intent_classifier_add_training_samples

        Add training samples.
        """
        pass

    def test_intent_classifier_create(self):
        """
        Test case for intent_classifier_create

        Create an intent classifier.
        """
        pass

    def test_intent_classifier_curate(self):
        """
        Test case for intent_classifier_curate

        Endpoint to aid in the curation of a model instance.
        """
        pass

    def test_intent_classifier_del_training_samples(self):
        """
        Test case for intent_classifier_del_training_samples

        Delete training samples.
        """
        pass

    def test_intent_classifier_get_details(self):
        """
        Test case for intent_classifier_get_details

        Get details of named instance.
        """
        pass

    def test_intent_classifier_get_details_all(self):
        """
        Test case for intent_classifier_get_details_all

        Get list of loaded intent classifiers.
        """
        pass

    def test_intent_classifier_get_labels(self):
        """
        Test case for intent_classifier_get_labels

        Get list of possible labels.
        """
        pass

    def test_intent_classifier_get_training_samples(self):
        """
        Test case for intent_classifier_get_training_samples

        Get training samples.
        """
        pass

    def test_intent_classifier_online_training_samples(self):
        """
        Test case for intent_classifier_online_training_samples

        Train/update the classifier online with the samples provided.
        """
        pass

    def test_intent_classifier_retrieve(self):
        """
        Test case for intent_classifier_retrieve

        Classify intent.
        """
        pass

    def test_intent_classifier_train(self):
        """
        Test case for intent_classifier_train

        Train the named intent classifier.
        """
        pass


if __name__ == '__main__':
    unittest.main()
