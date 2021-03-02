# coding: utf-8

from __future__ import absolute_import

import urllib3
import unittest
import time

import feersum_nlu
from feersum_nlu.rest import ApiException
from test import feersumnlu_host, feersum_nlu_auth_token

import uuid


@unittest.skip("Skipping - This test requires the server to download a LM not yet typically used in production.")
class TestTextClassifier(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_text_classifier(self):
        # Configure API key authorization: APIKeyHeader
        configuration = feersum_nlu.Configuration()

        # configuration.api_key['AUTH_TOKEN'] = feersum_nlu_auth_token
        configuration.api_key['X-Auth-Token'] = feersum_nlu_auth_token  # Alternative auth key header!

        configuration.host = feersumnlu_host

        api_instance = feersum_nlu.TextClassifiersApi(feersum_nlu.ApiClient(configuration))

        instance_name = 'test_text_clsfr_' + str(uuid.uuid4())

        create_details = feersum_nlu.TextClassifierCreateDetails(name=instance_name,
                                                                 desc="Test text classifier.",
                                                                 load_from_store=False)

        # The training samples.
        labelled_text_sample_list = []
        labelled_text_sample_list.append(feersum_nlu.LabelledTextSample(text="I would like to fill in a claim form",
                                                                        label="claim"))

        labelled_text_sample_list.append(feersum_nlu.LabelledTextSample(text="I would like to get a quote",
                                                                        label="quote"))

        train_details = feersum_nlu.TrainDetails(immediate_mode=False,
                                                 clsfr_algorithm="nearest_neighbour_l1",
                                                 language_model_list=[
                                                     {
                                                         "lang_code": "eng",
                                                         "lang_model": "feers_usent_eng"
                                                     }
                                                 ]
                                                 )

        text_input = feersum_nlu.TextInput("How do I get a quote?")

        print()

        try:
            print("Create the text classifier:")
            api_response = api_instance.text_classifier_create(create_details)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Add training samples to the text classifier:")
            api_response = api_instance.text_classifier_add_training_samples(instance_name, labelled_text_sample_list)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Get the training samples of the text classifier:")
            api_response = api_instance.text_classifier_get_training_samples(instance_name)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            labelled_text_sample_delete_list = []
            labelled_text_sample_delete_list.append(feersum_nlu.LabelledTextSample(text="I would like to get a quote",
                                                                                   label="quote"))

            print("Del the training samples of the text classifier:")
            # api_response = api_instance.text_classifier_del_training_samples_all(instance_name)
            api_response = api_instance.text_classifier_del_training_samples(instance_name,
                                                                             labelled_text_sample_list=
                                                                             labelled_text_sample_delete_list)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Add training samples to the text classifier:")
            api_response = api_instance.text_classifier_add_training_samples(instance_name, labelled_text_sample_list)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Train the text classifier:")
            api_response = api_instance.text_classifier_train(instance_name, train_details)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            # TRAINING:
            # If timestamp is missing then the training is running in the background and you need to poll until
            # the model ID has updated.
            # In the near future webhooks will be supported to let you know when async training has finished.

            if api_response.training_stamp is None:
                # Background training in progress. We'll poll and wait for it to complete.
                print("Background training in progress...", flush=True, end='')
                previous_id = api_response.id

                while True:
                    print('.', end='', flush=True)
                    time.sleep(1)
                    inst_det = api_instance.text_classifier_get_details(instance_name)
                    if inst_det.id != previous_id:
                        # ToDo: Stop if details indicate that training failed.
                        break  # break from while-loop when ID updated which indicates training done.

                print('Done.')
                print()

            print("Get the details of all loaded text classifiers:")
            api_response = api_instance.text_classifier_get_details_all()
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Get the details of specific named loaded text classifiers:")
            api_response = api_instance.text_classifier_get_details(instance_name)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            self.assertTrue(api_response.cm_labels['0'] == 'claim' or api_response.cm_labels['1'] == 'claim')
            self.assertTrue(api_response.cm_labels['0'] == 'quote' or api_response.cm_labels['1'] == 'quote')

            # Get the classifier's possible labels. Might be inferred from the training data, but guaranteed to be
            # available after training.
            print("Get the labels of named loaded text classifiers:")
            api_response = api_instance.text_classifier_get_labels(instance_name)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Get some curate details of specific named loaded text classifier:")
            # Use the same labels as returned in the confusion matrix.
            label_pair = feersum_nlu.ClassLabelPair(matrix_name='train', true_label='1', predicted_label='1')
            api_response = api_instance.text_classifier_curate(instance_name, label_pair)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Classify text:")
            api_response = api_instance.text_classifier_retrieve(instance_name, text_input)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            scored_label_list = api_response
            if len(scored_label_list) > 0:
                scored_label = scored_label_list[0]
                print(scored_label.label, flush=True)
                self.assertTrue(scored_label.label == 'quote')
            else:
                self.assertTrue(False)

            # =====
            print("Delete specific named loaded text classifiers:")
            api_response = api_instance.text_classifier_del(instance_name)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Vaporise specific named loaded text classifiers:")
            api_response = api_instance.text_classifier_vaporise(instance_name)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

        except ApiException as e:
            print("Exception when calling an text classifier operation: %s\n" % e)
            self.assertTrue(False)
        except urllib3.exceptions.MaxRetryError:
            print("Connection MaxRetryError!")
            self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
