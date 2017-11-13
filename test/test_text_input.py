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
from feersum_nlu.models.text_input import TextInput


class TestTextInput(unittest.TestCase):
    """ TextInput unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTextInput(self):
        """
        Test TextInput
        """
        model = feersum_nlu.models.text_input.TextInput()


if __name__ == '__main__':
    unittest.main()