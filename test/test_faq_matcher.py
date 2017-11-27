# coding: utf-8

from __future__ import absolute_import

import os
import urllib3
import unittest

import feersum_nlu
from feersum_nlu.rest import ApiException


class TestSentiment(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_sentiment(self):
        # Try to get the API key from your OS environment, else use 'YOUR_API_KEY' as the default value in the code below.
        # You may use any environment variable you want, it doesn't have to be 'FEERSUM_NLU_AUTH_TOKEN'.
        feersum_nlu_auth_token = os.environ.get('FEERSUM_NLU_AUTH_TOKEN', 'YOUR_API_KEY')
        print('feersum_nlu_auth_token = ', feersum_nlu_auth_token)

        # Configure API key authorization: APIKeyHeader
        feersum_nlu.configuration.api_key['AUTH_TOKEN'] = feersum_nlu_auth_token

        # feersum_nlu.configuration.host = "http://127.0.0.1:8100/nlu/v2"
        feersum_nlu.configuration.host = "https://nlu.playground.feersum.io:443/nlu/v2"

        api_instance = feersum_nlu.FaqMatchersApi()

        instance_name = 'test_faq_mtchr'

        # wm_instance_name = 'feers_wm_eng'
        # We'll use the built-in manifolds, not the ones defined below!
        # # === Word manifold to use ===
        # print("Create the word manifold model:")
        # wm_api_instance = feersum_nlu.WordManifoldsApi()
        # wm_create_details = feersum_nlu.CreateDetails(name=wm_instance_name, desc="Test word manifold.",
        #                                               load_from_store=False, input_file="glove.6B.50d.trimmed.txt")
        # # wm_create_details = feersum_nlu.CreateDetails(name=wm_instance_name, load_from_store=True)
        # wm_api_response = wm_api_instance.word_manifold_create(wm_create_details)
        # print(" type(wm_api_response)", type(wm_api_response))
        # print(" wm_api_response", wm_api_response)
        # print()
        # # === ===


        create_details = feersum_nlu.CreateDetails(name=instance_name, desc="Test FAQ matcher.", load_from_store=False)

        # The training samples.
        labelled_text_sample_list = []
        labelled_text_sample_list.append(feersum_nlu.LabelledTextSample(text="How do I claim?",
                                                                        label="claim"))
        labelled_text_sample_list.append(feersum_nlu.LabelledTextSample(text="Hoe moet ek eis?",
                                                                        label="claim"))

        labelled_text_sample_list.append(feersum_nlu.LabelledTextSample(text="How do I get a quote?",
                                                                        label="quote"))
        labelled_text_sample_list.append(feersum_nlu.LabelledTextSample(text="Hoe kan ek 'n prys kry?",
                                                                        label="quote"))

        # Use default English manifold.
        # train_details = feersum_nlu.TrainDetails(immediate_mode=True)
        # OR
        # Use specified single manifold; the language defaults to English.
        # train_details = feersum_nlu.TrainDetails(immediate_mode=True, word_manifold=wm_instance_name)
        # OR
        # Use specified list of manifolds for multiple languages.
        word_manifold_list = [feersum_nlu.LabeledWordManifold('eng', 'feers_wm_eng'),
                              feersum_nlu.LabeledWordManifold('afr', 'feers_wm_afr'),
                              feersum_nlu.LabeledWordManifold('zul', 'feers_wm_zul')]

        train_details = feersum_nlu.TrainDetails(immediate_mode=True,
                                                 threshold=0.85,
                                                 word_manifold_list=word_manifold_list)

        text_input = feersum_nlu.TextInput("Where can I get a quote?")

        print()

        try:
            print("Create the FAQ matcher:")
            api_response = api_instance.faq_matcher_create(create_details)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Add training samples to the FAQ matcher:")
            api_response = api_instance.faq_matcher_add_training_samples(instance_name, labelled_text_sample_list)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Get the training samples of the FAQ matcher:")
            api_response = api_instance.faq_matcher_get_training_samples(instance_name)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Del the training samples of the FAQ matcher:")
            api_response = api_instance.faq_matcher_del_training_samples(instance_name)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Add training samples to the FAQ matcher:")
            api_response = api_instance.faq_matcher_add_training_samples(instance_name, labelled_text_sample_list)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Train the FAQ matcher:")
            api_response = api_instance.faq_matcher_train(instance_name, train_details)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Get the details of all loaded FAQ matcher:")
            api_response = api_instance.faq_matcher_get_details_all()
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Get the details of specific named loaded FAQ matcher:")
            api_response = api_instance.faq_matcher_get_details(instance_name)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            # Get the classifier's possible labels. Might be inferred from the training data, but guaranteed to be available
            # after training.
            print("Get the labels of named loaded FAQ matcher:")
            api_response = api_instance.faq_matcher_get_labels(instance_name)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Get some curate details of specific named loaded FAQ matcher:")
            # Use the same labels as returned in the confusion matrix.
            label_pair = feersum_nlu.ClassLabelPair(matrix_name='train', true_label='0', predicted_label='0')
            api_response = api_instance.faq_matcher_curate(instance_name, label_pair)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Match a question:")
            api_response = api_instance.faq_matcher_retrieve(instance_name, text_input)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            scored_label_list = api_response
            if len(scored_label_list) > 0:
                scored_label = scored_label_list[0]
                self.assertTrue(scored_label.get('label', '') == 'quote')
            else:
                self.assertTrue(False)

        except ApiException as e:
            print("Exception when calling an FAQ matcher operation: %s\n" % e)
            self.assertTrue(False)
        except urllib3.exceptions.MaxRetryError:
            print("Connection MaxRetryError!")
            self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
