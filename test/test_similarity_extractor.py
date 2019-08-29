""" Test the similar word entity extractor. """

# coding: utf-8

from __future__ import absolute_import

import unittest
import urllib3

from examples import feersumnlu_host, feersum_nlu_auth_token
import feersum_nlu
from feersum_nlu.rest import ApiException
from test import feersumnlu_host, feersum_nlu_auth_token

import uuid


class TestSimEnt(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_sim_ent(self):
        # Configure API key authorization: APIKeyHeader
        configuration = feersum_nlu.Configuration()

        # configuration.api_key['AUTH_TOKEN'] = feersum_nlu_auth_token
        configuration.api_key['X-Auth-Token'] = feersum_nlu_auth_token  # Alternative auth key header!

        configuration.host = feersumnlu_host

        api_instance = feersum_nlu.SimWordEntityExtractorsApi(feersum_nlu.ApiClient(configuration))

        instance_name = 'sim-word-extractor-test_' + str(uuid.uuid4())

        similarity_ent_create_details = \
            feersum_nlu.SimWordEntityExtractorCreateDetails(name=instance_name,
                                                            desc="Test similarity extractor.",
                                                            similar_words=["red", "green", "blue", "purple",
                                                                           "white", "black", "grey"],
                                                            threshold=0.6,
                                                            # (0.0-1.0] - lower vals result in more false positives.
                                                            word_manifold="feers_wm_eng",
                                                            # This is one of the built-in word embeddings.
                                                            load_from_store=False)

        text_input = feersum_nlu.TextInput("I have an orange car with pink stripes.")
        # api_response [{'entity': 'orange', 'similarity': 0.6299035873841149},
        #               {'entity': 'pink', 'similarity': 0.690814436389662}]

        print()

        try:
            print("Create the entity extractor:")
            api_response = api_instance.sim_word_entity_extractor_create(similarity_ent_create_details)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Get the details of all loaded entity extractors:")
            api_response = api_instance.sim_word_entity_extractor_get_details_all()
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Get the details of specific named loaded entity extractor:")
            api_response = api_instance.sim_word_entity_extractor_get_details(instance_name)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Extract entities:")
            api_response = api_instance.sim_word_entity_extractor_retrieve(instance_name, text_input)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            self.assertTrue(api_response[0].entity == 'orange')
            self.assertTrue(round(api_response[0].similarity, 2) == 0.63)

            self.assertTrue(api_response[1].entity == 'pink')
            self.assertTrue(round(api_response[1].similarity, 2) == 0.69)

            print("Delete named loaded entity extractor:")
            api_response = api_instance.sim_word_entity_extractor_del(instance_name)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Vaporise named loaded entity extractor:")
            api_response = api_instance.sim_word_entity_extractor_vaporise(instance_name)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

        except ApiException as e:
            print("Exception when calling a entity extractor operation: %s\n" % e)
            self.assertTrue(False)
        except urllib3.exceptions.HTTPError as e:
            print("Connection HTTPError! %s\n" % e)
            self.assertTrue(False)
