# coding: utf-8

from __future__ import absolute_import

import urllib3
import unittest
import time

import feersum_nlu
from feersum_nlu.rest import ApiException
from test import feersumnlu_host, feersum_nlu_auth_token

import uuid


class TestIntentClassifier(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_intent_classifier(self):
        # Configure API key authorization: APIKeyHeader
        configuration = feersum_nlu.Configuration()

        # configuration.api_key['AUTH_TOKEN'] = feersum_nlu_auth_token
        configuration.api_key['X-Auth-Token'] = feersum_nlu_auth_token  # Alternative auth key header!

        configuration.host = feersumnlu_host

        api_instance = feersum_nlu.IntentClassifiersApi(feersum_nlu.ApiClient(configuration))

        instance_name = 'test_intent_clsfr_' + str(uuid.uuid4())

        word_manifold_list = [feersum_nlu.LabelledWordManifold('eng', 'feers_wm_eng')]
        language_model_list = [feersum_nlu.LabelledLanguageModel('eng', 'feers_wm_eng')]
        # The playground's pre-loaded embeddings include:
        # "feers_wm_afr", "feers_wm_eng", "feers_wm_nbl", "feers_wm_xho",
        # "feers_wm_zul", "feers_wm_ssw", "feers_wm_nso", "feers_wm_sot",
        # "feers_wm_tsn", "feers_wm_ven", "feers_wm_tso"
        # and "glove6B50D_trimmed"

        create_details = feersum_nlu.IntentClassifierCreateDetails(name=instance_name,
                                                                   desc="Test intent classifier.",
                                                                   lid_model_file="lid_za",
                                                                   load_from_store=False)

        # The training samples.
        labelled_text_sample_list = []
        labelled_text_sample_list.append(feersum_nlu.LabelledTextSample(text="I would like to fill in a claim form.",
                                                                        label="claim"))
        labelled_text_sample_list.append(feersum_nlu.LabelledTextSample(text="How should I claim?",
                                                                        label="claim"))

        labelled_text_sample_list.append(feersum_nlu.LabelledTextSample(text="I would like to get a quote.",
                                                                        label="quote"))
        labelled_text_sample_list.append(feersum_nlu.LabelledTextSample(text="Where can I get a quote?",
                                                                        label="quote"))

        train_details = feersum_nlu.TrainDetails(threshold=0.85,
                                                 # word_manifold_list=word_manifold_list,
                                                 language_model_list=language_model_list,
                                                 immediate_mode=False)

        tsne_settings = feersum_nlu.TsneSettings(n_components=3, perplexity=35, learning_rate=250)

        text_input = feersum_nlu.TextInput("How do I get a quote?")

        print()

        try:
            print("Create the intent classifier:")
            api_response = api_instance.intent_classifier_create(create_details)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Add training samples to the intent classifier:")
            api_response = api_instance.intent_classifier_add_training_samples(instance_name, labelled_text_sample_list)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Get the training samples of the intent classifier:")
            api_response = api_instance.intent_classifier_get_training_samples(instance_name)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            labelled_text_sample_delete_list = []

            print("Del the training samples of the intent classifier:")
            # api_response = api_instance.intent_classifier_del_training_samples_all(instance_name)
            api_response = api_instance.intent_classifier_del_training_samples(instance_name,
                                                                               labelled_text_sample_list=
                                                                               labelled_text_sample_delete_list)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Add training samples to the intent classifier:")
            api_response = api_instance.intent_classifier_add_training_samples(instance_name, labelled_text_sample_list)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Add testing samples to the intent classifier:")
            api_response = api_instance.intent_classifier_add_testing_samples(instance_name, labelled_text_sample_list)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Train the intent classifier:")
            api_response = api_instance.intent_classifier_train(instance_name, train_details)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            # TRAINING:
            # If timestamp begins with 'ASYNC...' the the training is running in the background and you need to poll until
            # the model ID has updated.
            # if timestamp doesn't begin with ASYNC then the training has completed synchronously and you may continue.
            # In the near future webhooks will be supported to let you know when async training has finished.

            if api_response.training_stamp is None:
                # Background training in progress. We'll poll and wait for it to complete.
                print("Background training in progress...", flush=True, end='')
                previous_id = api_response.id

                while True:
                    print('.', end='', flush=True)
                    time.sleep(1)
                    inst_det = api_instance.intent_classifier_get_details(instance_name)
                    if inst_det.id != previous_id:
                        # ToDo: Stop if details indicate that training failed.
                        break  # break from while-loop when ID updated which indicates training done.

                print('Done.')
                print()

            print("Get the details of all loaded intent classifiers:")
            api_response = api_instance.intent_classifier_get_details_all()
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Get the details of specific named loaded intent classifiers:")
            api_response = api_instance.intent_classifier_get_details(instance_name)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            # self.assertTrue(api_response.cm_labels['0'] == 'claim' or api_response.cm_labels['1'] == 'claim')
            # self.assertTrue(api_response.cm_labels['0'] == 'quote' or api_response.cm_labels['1'] == 'quote')

            # Get the classifier's possible labels. Might be inferred from the training data, but guaranteed to be
            # available after training.
            print("Get the labels of named loaded intent classifiers:")
            api_response = api_instance.intent_classifier_get_labels(instance_name)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Get some curate details of specific named loaded intent classifier:")
            # Use the same labels as returned in the confusion matrix.
            label_pair = feersum_nlu.ClassLabelPair(matrix_name='train', true_label='1', predicted_label='1')
            api_response = api_instance.intent_classifier_curate(instance_name, label_pair)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Classify intent:")
            api_response = api_instance.intent_classifier_retrieve(instance_name, text_input)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            scored_label_list = api_response
            if len(scored_label_list) > 0:
                scored_label = scored_label_list[0]
                self.assertTrue(scored_label.label == 'quote')
            else:
                self.assertTrue(False)

            # print("Start a TSNE calculation:")
            # api_response = api_instance.intent_classifier_tsne_post(instance_name, tsne_settings)
            # print(" type(api_response)", type(api_response))
            # print(" api_response", api_response)
            # print()

            # # Wait for TSNE result to be ready.
            # time.sleep(3)

            # print("Get latest a TSNE results:")
            # api_response = api_instance.intent_classifier_tsne_get(instance_name)
            # print(" type(api_response)", type(api_response))
            # print(" api_response", api_response)
            # print()

            # =====
            print("Delete specific named loaded intent classifiers:")
            api_response = api_instance.intent_classifier_del(instance_name)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Vaporise specific named loaded intent classifiers:")
            api_response = api_instance.intent_classifier_vaporise(instance_name)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

        except ApiException as e:
            print("Exception when calling an intent classifier operation: %s\n" % e)
            self.assertTrue(False)
        except urllib3.exceptions.MaxRetryError:
            print("Connection MaxRetryError!")
            self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
