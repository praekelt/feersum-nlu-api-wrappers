# coding: utf-8

from __future__ import absolute_import

import urllib3
import unittest

import feersum_nlu
from feersum_nlu.rest import ApiException
from test import feersumnlu_host, feersum_nlu_auth_token

import uuid


class TestLID(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_lid(self):
        # Configure API key authorization: APIKeyHeader
        configuration = feersum_nlu.Configuration()

        # configuration.api_key['AUTH_TOKEN'] = feersum_nlu_auth_token
        configuration.api_key['X-Auth-Token'] = feersum_nlu_auth_token  # Alternative auth key header!

        configuration.host = feersumnlu_host

        api_instance = feersum_nlu.LanguageRecognisersApi(feersum_nlu.ApiClient(configuration))

        instance_name = 'test_lr4_' + str(uuid.uuid4())

        create_details = \
            feersum_nlu.LanguageRecogniserCreateDetails(name=instance_name,
                                                        desc="Test LR4 lang ident model.",
                                                        lid_model_file='lid_za',
                                                        load_from_store=False)

        text_input = feersum_nlu.TextInput("Ek het 'n huisie by die see.")

        print()

        try:
            print("Create the lr4 instance:")
            api_response = api_instance.language_recogniser_create(create_details)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Get the details of all loaded lr4 instances:")
            api_response = api_instance.language_recogniser_get_details_all()
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Get the details of specific named loaded lr4 instance:")
            api_response = api_instance.language_recogniser_get_details(instance_name)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            # Get the classifier's possible labels. Might be inferred from the training data,
            # but guaranteed to be available
            # after training.
            print("Get the labels of named loaded lr4 instance:")
            api_response = api_instance.language_recogniser_get_labels(instance_name)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Identify the language of the text:")
            api_response = api_instance.language_recogniser_retrieve(instance_name, text_input)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            scored_label_list = api_response
            if len(scored_label_list) > 0:
                scored_label = scored_label_list[0]
                self.assertTrue(scored_label.label == 'afr')
            else:
                self.assertTrue(False)

            print("Delete specific named loaded lr4 instance:")
            api_response = api_instance.language_recogniser_del(instance_name)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Vaporise specific named loaded lr4 instance:")
            api_response = api_instance.language_recogniser_vaporise(instance_name)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

        except ApiException as e:
            print("Exception when calling an lr4 operation: %s\n" % e)
            self.assertTrue(False)
        except urllib3.exceptions.MaxRetryError:
            print("Connection MaxRetryError!")
            self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
