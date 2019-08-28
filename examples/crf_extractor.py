""" Example: Shows how to create, train and use a CRF entity extractor. """

import urllib3

import feersum_nlu
from feersum_nlu.rest import ApiException
from examples import feersumnlu_host, feersum_nlu_auth_token

# Configure API key authorization: APIKeyHeader
configuration = feersum_nlu.Configuration()

# configuration.api_key['AUTH_TOKEN'] = feersum_nlu_auth_token
configuration.api_key['X-Auth-Token'] = feersum_nlu_auth_token  # Alternative auth key header!

configuration.host = feersumnlu_host

api_instance = feersum_nlu.CrfEntityExtractorsApi(feersum_nlu.ApiClient(configuration))

instance_name = 'crf_entity_extractor_integration_test'

create_details = feersum_nlu.CrfEntityExtractorCreateDetails(name=instance_name,
                                                             desc="Test CRF extractor.",
                                                             long_name="The optional more descriptive name.",
                                                             load_from_store=False)

# The training samples.

training_sample_list = []
training_sample_list.append(feersum_nlu.CrfSample(text="Can I have a burger with chips please?", intent=None,
                                                  entity_list=[
                                                      feersum_nlu.CrfEntity(entity="food", index=13, len=17)
                                                  ]))

training_sample_list.append(feersum_nlu.CrfSample(text="Can I have a slice of pizza?", intent=None,
                                                  entity_list=[
                                                      feersum_nlu.CrfEntity(entity="food", index=13, len=14)
                                                  ]))

training_sample_list.append(feersum_nlu.CrfSample(text="Can I have a hot dog with mustard?", intent=None,
                                                  entity_list=[
                                                      feersum_nlu.CrfEntity(entity="food", index=13, len=20)
                                                  ]))

sample_delete_list = []
sample_delete_list.append(feersum_nlu.CrfSample(text="Can I have a slice of pizza?", intent=None,
                                                entity_list=[
                                                    feersum_nlu.CrfEntity(entity="food", index=13, len=14)
                                                ]))

testing_sample_list = []
testing_sample_list.append(feersum_nlu.CrfSample(text="Can I have a burger with chips please?", intent=None,
                                                 entity_list=[
                                                     feersum_nlu.CrfEntity(entity="food", index=13, len=17)
                                                 ]))

testing_sample_list.append(feersum_nlu.CrfSample(text="Can I have a slice of pizza?", intent=None,
                                                 entity_list=[
                                                     feersum_nlu.CrfEntity(entity="food", index=13, len=14)
                                                 ]))

testing_sample_list.append(feersum_nlu.CrfSample(text="Can I have a hot dog with mustard?", intent=None,
                                                 entity_list=[
                                                     feersum_nlu.CrfEntity(entity="food", index=13, len=20)
                                                 ]))

text_input_0 = feersum_nlu.TextInput("I would like to buy a beef sandwich with mustard.",
                                     lang_code="eng")  # optional language hint.

caller_name = 'example_caller'

print()

try:
    print("Create the CRF entity extractor:")
    api_response = api_instance.crf_entity_extractor_create(create_details, x_caller=caller_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Add training samples to the CRF entity extractor:")
    api_response = api_instance.crf_entity_extractor_add_training_samples(instance_name, training_sample_list)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the training samples of the CRF entity extractor:")
    api_response = api_instance.crf_entity_extractor_get_training_samples(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Del a single training samples of the CRF entity extractor:")
    api_response = \
        api_instance.crf_entity_extractor_del_training_samples(instance_name,
                                                               crf_sample_list=sample_delete_list)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Del training samples of the CRF entity extractor:")
    api_response = api_instance.crf_entity_extractor_del_training_samples_all(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the reduced training samples of the CRF entity extractor:")
    api_response = api_instance.crf_entity_extractor_get_training_samples(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Add all the training samples back to the CRF entity extractor:")
    api_response = api_instance.crf_entity_extractor_add_training_samples(instance_name, training_sample_list)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Add testing samples to the CRF entity extractor:")
    api_response = api_instance.crf_entity_extractor_add_testing_samples(instance_name, testing_sample_list)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    train_details = feersum_nlu.TrainDetails(threshold=0.99)

    print("Train the CRF entity extractor:")
    instance_detail = api_instance.crf_entity_extractor_train(instance_name, train_details)
    print(" type(api_response)", type(instance_detail))
    print(" api_response", instance_detail)
    print()

    print("Get the details of all loaded CRF entity extractor:")
    api_response = api_instance.crf_entity_extractor_get_details_all()
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the details of specific named loaded CRF entity extractor:")
    api_response = api_instance.crf_entity_extractor_get_details(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    # Get the classifier's possible labels. Might be inferred from the training data, but guaranteed to be available
    # after training.
    print("Get the labels of named loaded CRF entity extractor:")
    api_response = api_instance.crf_entity_extractor_get_labels(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Extract some entities::")
    api_response = api_instance.crf_entity_extractor_retrieve(instance_name, text_input_0, x_caller=caller_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the parameters:")
    api_response = api_instance.crf_entity_extractor_get_params(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Update the parameters:")
    model_params = \
        feersum_nlu.ModelParams(threshold=0.9, desc="Examples: Test CRF entity extractor.",
                                long_name="A longer name.", readonly=True)
    api_response = api_instance.crf_entity_extractor_set_params(instance_name, model_params)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Update the parameters:")
    model_params = \
        feersum_nlu.ModelParams(readonly=False)
    api_response = api_instance.crf_entity_extractor_set_params(instance_name, model_params)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the details of specific named loaded CRF entity extractor:")
    api_response = api_instance.crf_entity_extractor_get_details(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Match a question:")
    api_response = api_instance.crf_entity_extractor_retrieve(instance_name, text_input_0)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Update the parameters:")
    model_params = \
        feersum_nlu.ModelParams(readonly=False)
    api_response = api_instance.crf_entity_extractor_set_params(instance_name, model_params)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    api_response = api_instance.crf_entity_extractor_retrieve(instance_name, text_input_0)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Delete specific named loaded CRF entity extractor:")
    api_response = api_instance.crf_entity_extractor_del(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Vaporise specific named loaded CRF entity extractor:")
    api_response = api_instance.crf_entity_extractor_vaporise(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

except ApiException as e:
    print("Exception when calling an CRF Entity Extractor operation: %s\n" % e)
except urllib3.exceptions.HTTPError as e:
    print("Connection HTTPError! %s\n" % e)
