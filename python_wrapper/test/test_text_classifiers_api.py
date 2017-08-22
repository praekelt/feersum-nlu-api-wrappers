# coding: utf-8

"""
    Feersum NLU API

    This is an HTTP API for Feersum NLU

    OpenAPI spec version: 1.0.0
    
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
from feersum_nlu.apis.text_classifiers_api import TextClassifiersApi


class TestTextClassifiersApi(unittest.TestCase):
    """ TextClassifiersApi unit test stubs """

    def setUp(self):
        self.api = feersum_nlu.apis.text_classifiers_api.TextClassifiersApi()

    def tearDown(self):
        pass

    def test_text_classifier_add_training_samples(self):
        """
        Test case for text_classifier_add_training_samples

        Add training samples.
        """
        pass

    def test_text_classifier_create(self):
        """
        Test case for text_classifier_create

        Create a text classifier.
        """
        pass

    def test_text_classifier_del_training_samples(self):
        """
        Test case for text_classifier_del_training_samples

        Delete training samples.
        """
        pass

    def test_text_classifier_get_details(self):
        """
        Test case for text_classifier_get_details

        Get details of named instance.
        """
        pass

    def test_text_classifier_get_details_all(self):
        """
        Test case for text_classifier_get_details_all

        Get list of loaded text classifiers.
        """
        pass

    def test_text_classifier_get_training_samples(self):
        """
        Test case for text_classifier_get_training_samples

        Get training samples.
        """
        pass

    def test_text_classifier_retrieve(self):
        """
        Test case for text_classifier_retrieve

        Classify text.
        """
        pass

    def test_text_classifier_train(self):
        """
        Test case for text_classifier_train

        Train the named text classifier.
        """
        pass


if __name__ == '__main__':
    unittest.main()
