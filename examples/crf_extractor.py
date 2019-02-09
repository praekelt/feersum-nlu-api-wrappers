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

instance_name = 'test_crf_extr'

create_details = feersum_nlu.CrfEntityExtractorCreateDetails(name=instance_name,
                                                             desc="Test crf extractor.",
                                                             long_name=instance_name,
                                                             load_from_store=False)

# The training samples.
crf_sample_list = []
crf_sample_list.append(feersum_nlu.CrfSample(text="Can I have a burger with chips please?",
                                             entity_list=[feersum_nlu.CrfEntity(index=13, len=17,
                                                                                entity="food")]))
crf_sample_list.append(feersum_nlu.CrfSample(text="Can I have a slice of pizza?",
                                             entity_list=[feersum_nlu.CrfEntity(index=13, len=14,
                                                                                entity="food")]))
crf_sample_list.append(feersum_nlu.CrfSample(text="Can I have a hot dog with mustard?",
                                             entity_list=[feersum_nlu.CrfEntity(index=13, len=20,
                                                                                entity="food")]))

# train_details = feersum_nlu.TrainDetails(immediate_mode=True)
train_details = feersum_nlu.TrainDetails(threshold=1.0)

text_input = feersum_nlu.TextInput("I would like to buy a beef sandwich with mustard.")

print()

try:
    print("Create the crf extractor:")
    api_response = api_instance.crf_entity_extractor_create(create_details)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Add training samples to the crf extractor:")
    api_response = api_instance.crf_entity_extractor_add_training_samples(instance_name, crf_sample_list)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the training samples of the crf extractor:")
    api_response = api_instance.crf_entity_extractor_get_training_samples(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Del the training samples of the crf extractor:")
    api_response = api_instance.crf_entity_extractor_del_training_samples_all(instance_name)
    # api_response = api_instance.crf_entity_extractor_classifier_del_training_samples(instance_name,
    #                                                                    labelled_text_sample_list=[])
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Add training samples to the crf extractor:")
    api_response = api_instance.crf_entity_extractor_add_training_samples(instance_name, crf_sample_list)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Del testing samples of the crf extractor:")
    api_response = api_instance.crf_entity_extractor_del_testing_samples_all(instance_name)
    # api_response = api_instance.crf_entity_extractor_del_testing_samples(instance_name,
    #                                                             labelled_text_sample_list=
    #                                                             labelled_text_sample_testing_list)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Train the crf extractor:")
    api_response = api_instance.crf_entity_extractor_train(instance_name, train_details)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the details of all loaded crf extractors:")
    api_response = api_instance.crf_entity_extractor_get_details_all()
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the details of specific named loaded crf extractors:")
    api_response = api_instance.crf_entity_extractor_get_details(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    # Get the classifier's possible labels. Might be inferred from the training data, but guaranteed to be available
    # after training.
    print("Get the labels of named loaded crf extractors:")
    api_response = api_instance.crf_entity_extractor_get_labels(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the model params:")
    api_response = api_instance.crf_entity_extractor_get_params(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Update the model params:")
    model_params = feersum_nlu.ModelParams(threshold=0.7, desc="Examples: Test extractor.",
                                           long_name='Test extractor')
    api_response = api_instance.crf_entity_extractor_set_params(instance_name, model_params)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the details of specific named loaded crf extractors:")
    api_response = api_instance.crf_entity_extractor_get_details(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Extract entities:")
    api_response = api_instance.crf_entity_extractor_retrieve(instance_name, text_input)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Delete specific named loaded crf extractors:")
    api_response = api_instance.crf_entity_extractor_del(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Vaporise specific named loaded crf extractors:")
    api_response = api_instance.crf_entity_extractor_vaporise(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

except ApiException as e:
    print("Exception when calling an crf extractor operation: %s\n" % e)
except urllib3.exceptions.HTTPError as e:
    print("Connection HTTPError! %s\n" % e)
