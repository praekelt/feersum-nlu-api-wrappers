""" Example: Shows how to create, train and use a synonym entity extractor. """

import urllib3

import unittest

import feersum_nlu
from feersum_nlu.rest import ApiException
from test import feersumnlu_host, feersum_nlu_auth_token

import uuid


class TestSynonymExtractor(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_synonym_extractor(self):
        # Configure API key authorization: APIKeyHeader
        configuration = feersum_nlu.Configuration()

        # configuration.api_key['AUTH_TOKEN'] = feersum_nlu_auth_token
        configuration.api_key['X-Auth-Token'] = feersum_nlu_auth_token  # Alternative auth key header!

        configuration.host = feersumnlu_host

        api_instance = feersum_nlu.SynonymEntityExtractorsApi(feersum_nlu.ApiClient(configuration))

        instance_name = 'test_synonym_extr_' + str(uuid.uuid4())

        create_details = feersum_nlu.SynonymEntityExtractorCreateDetails(name=instance_name,
                                                                         desc="Test Synonym extractor.",
                                                                         long_name="The optional more descriptive name.",
                                                                         load_from_store=False)

        # The training samples.

        training_sample_list = []
        training_sample_list.append(feersum_nlu.SynonymSample(text="Can I have water please?", intent=None,
                                                              entity_list=[
                                                                  feersum_nlu.SynonymEntity(entity="drink", index=11, len=5)
                                                              ]))

        training_sample_list.append(feersum_nlu.SynonymSample(text="Can I have a soft drink?", intent=None,
                                                              entity_list=[
                                                                  feersum_nlu.SynonymEntity(entity="drink", index=13, len=10)
                                                              ]))

        training_sample_list.append(feersum_nlu.SynonymSample(text="Can I have a coffee?", intent=None,
                                                              entity_list=[
                                                                  feersum_nlu.SynonymEntity(entity="drink", index=13, len=6)
                                                              ]))

        sample_delete_list = []
        sample_delete_list.append(feersum_nlu.SynonymSample(text="Can I have a soft drink?", intent=None,
                                                            entity_list=[
                                                                feersum_nlu.SynonymEntity(entity="drink", index=13, len=10)
                                                            ]))

        testing_sample_list = []
        testing_sample_list.append(feersum_nlu.SynonymSample(text="Can I have water please?", intent=None,
                                                             entity_list=[
                                                                 feersum_nlu.SynonymEntity(entity="drink", index=11, len=5)
                                                             ]))

        testing_sample_list.append(feersum_nlu.SynonymSample(text="Can I have a soft drink?", intent=None,
                                                             entity_list=[
                                                                 feersum_nlu.SynonymEntity(entity="drink", index=13, len=10)
                                                             ]))

        testing_sample_list.append(feersum_nlu.SynonymSample(text="Can I have a coffee?", intent=None,
                                                             entity_list=[
                                                                 feersum_nlu.SynonymEntity(entity="drink", index=13, len=6)
                                                             ]))

        text_input_0 = feersum_nlu.TextInput("I would like to buy a coffee please.",
                                             lang_code="eng")  # optional language hint.

        print()

        try:
            print("Create the Synonym entity extractor:")
            api_response = api_instance.synonym_entity_extractor_create(create_details)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Add training samples to the Synonym entity extractor:")
            api_response = api_instance.synonym_entity_extractor_add_training_samples(instance_name, training_sample_list)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Get the training samples of the Synonym entity extractor:")
            api_response = api_instance.synonym_entity_extractor_get_training_samples(instance_name)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Del a single training samples of the Synonym entity extractor:")
            api_response = \
                api_instance.synonym_entity_extractor_del_training_samples(instance_name,
                                                                           synonym_sample_list=sample_delete_list)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Add training samples to the Synonym entity extractor avoiding duplicates:")
            api_response = api_instance.synonym_entity_extractor_add_training_samples(instance_name, training_sample_list)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Del training samples of the Synonym entity extractor:")
            api_response = api_instance.synonym_entity_extractor_del_training_samples_all(instance_name)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Get the reduced training samples of the Synonym entity extractor:")
            api_response = api_instance.synonym_entity_extractor_get_training_samples(instance_name)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Add all the training samples back to the Synonym entity extractor:")
            api_response = api_instance.synonym_entity_extractor_add_training_samples(instance_name, training_sample_list)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Add testing samples to the Synonym entity extractor:")
            api_response = api_instance.synonym_entity_extractor_add_testing_samples(instance_name, testing_sample_list)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            try:
                print("Try to add invalid sample to the Synonym entity extractor:")
                api_instance.synonym_entity_extractor_add_testing_samples(instance_name, [
                    feersum_nlu.SynonymSample(text="Can I have a burger with chips please?", intent=None, entity_list=None)])
            except ApiException:
                self.assertTrue(True)  # This should fail!

            try:
                print("Try to add invalid sample to the Synonym entity extractor:")
                api_instance.synonym_entity_extractor_add_testing_samples(instance_name, [
                    feersum_nlu.SynonymSample(text=None, intent=None,
                                              entity_list=[feersum_nlu.SynonymEntity(entity="food", index=13, len=17)])])
            except ApiException:
                self.assertTrue(True)  # This should fail!

            train_details = feersum_nlu.TrainDetails(threshold=0.99)

            print("Train the Synonym entity extractor:")
            instance_detail = api_instance.synonym_entity_extractor_train(instance_name, train_details)
            print(" type(api_response)", type(instance_detail))
            print(" api_response", instance_detail)
            print()

            print("Get the details of all loaded Synonym entity extractor:")
            api_response = api_instance.synonym_entity_extractor_get_details_all()
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Get the details of specific named loaded Synonym entity extractor:")
            api_response = api_instance.synonym_entity_extractor_get_details(instance_name)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            # Get the classifier's possible labels. Might be inferred from the training data, but guaranteed to be available
            # after training.
            print("Get the labels of named loaded Synonym entity extractor:")
            api_response = api_instance.synonym_entity_extractor_get_labels(instance_name)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Extract some entities:")
            api_response = api_instance.synonym_entity_extractor_retrieve(instance_name, text_input_0)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Get the parameters:")
            api_response = api_instance.synonym_entity_extractor_get_params(instance_name)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Update the parameters:")
            model_params = \
                feersum_nlu.ModelParams(threshold=0.9, desc="Examples: Test Synonym entity extractor.",
                                        long_name="A longer name.", readonly=True)
            api_response = api_instance.synonym_entity_extractor_set_params(instance_name, model_params)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Update the parameters:")
            model_params = \
                feersum_nlu.ModelParams(readonly=False)
            api_response = api_instance.synonym_entity_extractor_set_params(instance_name, model_params)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Get the details of specific named loaded Synonym entity extractor:")
            api_response = api_instance.synonym_entity_extractor_get_details(instance_name)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Extract some entities:")
            api_response = api_instance.synonym_entity_extractor_retrieve(instance_name, text_input_0)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            self.assertTrue(len(api_response) == 1)
            self.assertTrue(api_response[0].entity == 'drink')

            print("Update the parameters:")
            model_params = \
                feersum_nlu.ModelParams(readonly=False)
            api_response = api_instance.synonym_entity_extractor_set_params(instance_name, model_params)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            api_response = api_instance.synonym_entity_extractor_retrieve(instance_name, text_input_0)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Delete specific named loaded Synonym entity extractor:")
            api_response = api_instance.synonym_entity_extractor_del(instance_name)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

            print("Vaporise specific named loaded Synonym entity extractor:")
            api_response = api_instance.synonym_entity_extractor_vaporise(instance_name)
            print(" type(api_response)", type(api_response))
            print(" api_response", api_response)
            print()

        except ApiException as e:
            print("Exception when calling an Synonym Entity Extractor operation: %s\n" % e)
            self.assertTrue(False)
        except urllib3.exceptions.HTTPError as e:
            print("Connection HTTPError! %s\n" % e)
            self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
