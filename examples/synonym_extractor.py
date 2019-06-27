""" Example: Shows how to create, train and use a Synonym entity extractor. """

import urllib3

import feersum_nlu
from feersum_nlu.rest import ApiException
from examples import feersumnlu_host, feersum_nlu_auth_token

# Configure API key authorization: APIKeyHeader
configuration = feersum_nlu.Configuration()

# configuration.api_key['AUTH_TOKEN'] = feersum_nlu_auth_token
configuration.api_key['X-Auth-Token'] = feersum_nlu_auth_token  # Alternative auth key header!

configuration.host = feersumnlu_host

api_instance = feersum_nlu.SynonymEntityExtractorsApi(feersum_nlu.ApiClient(configuration))

instance_name = 'test_synonym_extr'

create_details = feersum_nlu.SynonymEntityExtractorCreateDetails(name=instance_name,
                                                                 desc="Test synonym extractor.",
                                                                 long_name="The optional more descriptive name.",
                                                                 load_from_store=False)

# The training samples.

training_sample_list = []

training_sample_list.append(feersum_nlu.SynonymSample(text="Can I have a burger with chips please?", intent=None,
                                                      entity_list=[
                                                              feersum_nlu.SynonymEntity(entity="food", index=13, len=17)
                                                          ]))

training_sample_list.append(feersum_nlu.SynonymSample(text="Can I have a slice of pizza?", intent=None,
                                                      entity_list=[
                                                          feersum_nlu.SynonymEntity(entity="food", index=13, len=14)
                                                      ]))

training_sample_list.append(feersum_nlu.SynonymSample(text="Can I have a hot dog with mustard?", intent=None,
                                                      entity_list=[
                                                          feersum_nlu.SynonymEntity(entity="food", index=13, len=20)
                                                      ]))

# === Training samples with ONLY synsets.
training_sample_list.append(feersum_nlu.SynonymSample(text=None, intent=None,
                                                      entity_list=[
                                                          feersum_nlu.SynonymEntity(entity="Game of Thrones",
                                                                                    syn_set=['GOT',
                                                                                             'GoT'])
                                                      ]))

training_sample_list.append(feersum_nlu.SynonymSample(text=None, intent=None,
                                                      entity_list=[
                                                          # ignore_case=True & ignore_word_boundaries=False is the default!
                                                          feersum_nlu.SynonymEntity(entity="Marvel's Agents of S.H.I.E.L.D.",
                                                                                    syn_set=['agents of shield',
                                                                                             's.h.i.e.l.d'],
                                                                                    ignore_case=True,
                                                                                    ignore_word_boundaries=False)
                                                      ]))
# ===

sample_delete_list = []
sample_delete_list.append(feersum_nlu.SynonymSample(text="Can I have a slice of pizza?", intent=None,
                                                    entity_list=[
                                                        feersum_nlu.SynonymEntity(entity="food", index=13, len=14)
                                                    ]))

testing_sample_list = []
testing_sample_list.append(feersum_nlu.SynonymSample(text="Can I have a burger with chips please?", intent=None,
                                                     entity_list=[
                                                         feersum_nlu.SynonymEntity(entity="food", index=13, len=17)
                                                     ]))

testing_sample_list.append(feersum_nlu.SynonymSample(text="Can I have a slice of pizza?", intent=None,
                                                     entity_list=[
                                                         feersum_nlu.SynonymEntity(entity="food", index=13, len=14)
                                                     ]))

testing_sample_list.append(feersum_nlu.SynonymSample(text="Can I have a hot dog with mustard?", intent=None,
                                                     entity_list=[
                                                         feersum_nlu.SynonymEntity(entity="food", index=13, len=20)
                                                     ]))

# text_input_0 = feersum_nlu.TextInput("I would like to buy a slice of pizza.",
#                                      lang_code="eng")  # optional language hint.
text_input_0 = feersum_nlu.TextInput("When is agents of ShielD showing?",
                                     lang_code="eng")  # optional language hint.

caller_name = 'example_caller'

print()

try:
    print("Create the synonym entity extractor:")
    api_response = api_instance.synonym_entity_extractor_create(create_details, x_caller=caller_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Add training samples to the synonym entity extractor:")
    api_response = api_instance.synonym_entity_extractor_add_training_samples(instance_name, training_sample_list)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the training samples of the synonym entity extractor:")
    api_response = api_instance.synonym_entity_extractor_get_training_samples(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Del a single training samples of the synonym entity extractor:")
    api_response = \
        api_instance.synonym_entity_extractor_del_training_samples(instance_name,
                                                                   synonym_sample_list=sample_delete_list)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Del training samples of the synonym entity extractor:")
    api_response = api_instance.synonym_entity_extractor_del_training_samples_all(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the reduced training samples of the synonym entity extractor:")
    api_response = api_instance.synonym_entity_extractor_get_training_samples(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Add all the training samples back to the synonym entity extractor:")
    api_response = api_instance.synonym_entity_extractor_add_training_samples(instance_name, training_sample_list)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Add testing samples to the synonym entity extractor:")
    api_response = api_instance.synonym_entity_extractor_add_testing_samples(instance_name, testing_sample_list)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    train_details = feersum_nlu.TrainDetails(threshold=0.99)

    print("Train the synonym entity extractor:")
    instance_detail = api_instance.synonym_entity_extractor_train(instance_name, train_details)
    print(" type(api_response)", type(instance_detail))
    print(" api_response", instance_detail)
    print()

    print("Get the details of all loaded synonym entity extractor:")
    api_response = api_instance.synonym_entity_extractor_get_details_all()
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the details of specific named loaded synonym entity extractor:")
    api_response = api_instance.synonym_entity_extractor_get_details(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    # Get the classifier's possible labels. Might be inferred from the training data, but guaranteed to be available
    # after training.
    print("Get the labels of named loaded synonym entity extractor:")
    api_response = api_instance.synonym_entity_extractor_get_labels(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Extract some entities::")
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
        feersum_nlu.ModelParams(threshold=0.9, desc="Examples: Test synonym entity extractor.",
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

    print("Get the details of specific named loaded synonym entity extractor:")
    api_response = api_instance.synonym_entity_extractor_get_details(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Extract some entities::")
    api_response = api_instance.synonym_entity_extractor_retrieve(instance_name, text_input_0, x_caller=caller_name)
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

    print("Extract some entities::")
    api_response = api_instance.synonym_entity_extractor_retrieve(instance_name, text_input_0)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Delete specific named loaded synonym entity extractor:")
    api_response = api_instance.synonym_entity_extractor_del(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Vaporise specific named loaded synonym entity extractor:")
    api_response = api_instance.synonym_entity_extractor_vaporise(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

except ApiException as e:
    print("Exception when calling an synonym Entity Extractor operation: %s\n" % e)
except urllib3.exceptions.HTTPError as e:
    print("Connection HTTPError! %s\n" % e)
