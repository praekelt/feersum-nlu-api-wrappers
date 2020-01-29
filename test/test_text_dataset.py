# coding: utf-8

from __future__ import absolute_import

import urllib3
import unittest
import time

import feersum_nlu
from feersum_nlu.rest import ApiException
from test import feersumnlu_host, feersum_nlu_auth_token

import uuid


class TestTextDataset(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_text_dataset(self):
        # Configure API key authorization: APIKeyHeader
        configuration = feersum_nlu.Configuration()

        # configuration.api_key['AUTH_TOKEN'] = feersum_nlu_auth_token
        configuration.api_key['X-Auth-Token'] = feersum_nlu_auth_token  # Alternative auth key header!

        configuration.host = feersumnlu_host

        api_instance = feersum_nlu.TextDatasetsApi(feersum_nlu.ApiClient(configuration))

        instance_name = 'test_text_dataset_' + str(uuid.uuid4())

        create_details = feersum_nlu.TextDatasetCreateDetails(name=instance_name,
                                                              desc="Test text dataset.",
                                                              load_from_store=False)

        # The training samples.
        labelled_text_sample_list = []
        labelled_text_sample_list.append(feersum_nlu.LabelledTextSample(text="I would like to fill in a claim form",
                                                                        label="claim"))

        labelled_text_sample_list.append(feersum_nlu.LabelledTextSample(text="I would like to get a quote",
                                                                        label="quote"))

        print()

        try:
            print("Create the text dataset:")
            api_response = api_instance.text_dataset_create(create_details)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Add samples to the text dataset:")
            api_response = api_instance.text_dataset_add_samples(instance_name, labelled_text_sample_list)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Get the samples of the text dataset:")
            api_response = api_instance.text_dataset_get_samples(instance_name)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            labelled_text_sample_delete_list = [feersum_nlu.LabelledTextSample(text="I would like to get a quote",
                                                                               label="quote")]

            print("Del a sample of the text dataset by text&label:")
            # api_response = api_instance.text_dataset_del_samples_all(instance_name)
            api_response = api_instance.text_dataset_del_samples(instance_name,
                                                                 labelled_text_sample_list=
                                                                 labelled_text_sample_delete_list)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Add all samples back to the text dataset:")
            api_response = api_instance.text_dataset_add_samples(instance_name, labelled_text_sample_list)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Get the samples of the text dataset:")
            api_response = api_instance.text_dataset_get_samples(instance_name)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            sample_uuid = api_response[0].uuid
            print("sample_uuid = ", sample_uuid)
            print()

            labelled_text_sample_update_list = [feersum_nlu.LabelledTextSample(uuid=sample_uuid,
                                                                               text=api_response[0].text + " more text.",
                                                                               label=api_response[0].label,
                                                                               lang_code="eng")]

            print("Update a sample of the text dataset by its UUID:")
            # api_response = api_instance.text_dataset_del_samples_all(instance_name)
            api_response = api_instance.text_dataset_update_samples(instance_name,
                                                                    labelled_text_sample_list=
                                                                    labelled_text_sample_update_list)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            labelled_text_sample_delete_list = [feersum_nlu.LabelledTextSample(uuid=sample_uuid)]

            print("Del a sample of the text dataset by its UUID:")
            # api_response = api_instance.text_dataset_del_samples_all(instance_name)
            api_response = api_instance.text_dataset_del_samples(instance_name,
                                                                 labelled_text_sample_list=
                                                                 labelled_text_sample_delete_list)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Add all samples back to the text dataset:")
            api_response = api_instance.text_dataset_add_samples(instance_name, labelled_text_sample_list)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Get the details of all loaded text dataset:")
            api_response = api_instance.text_dataset_get_details_all()
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Get the details of specific named loaded text dataset:")
            api_response = api_instance.text_dataset_get_details(instance_name)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            # Get the dataset's labels.
            print("Get the labels of named loaded text dataset:")
            api_response = api_instance.text_dataset_get_labels(instance_name)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            # =====
            print("Delete specific named loaded text dataset:")
            api_response = api_instance.text_dataset_del(instance_name)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Vaporise specific named loaded text dataset:")
            api_response = api_instance.text_dataset_vaporise(instance_name)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

        except ApiException as e:
            print("Exception when calling an text dataset operation: %s\n" % e)
            self.assertTrue(False)
        except urllib3.exceptions.MaxRetryError:
            print("Connection MaxRetryError!")
            self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
