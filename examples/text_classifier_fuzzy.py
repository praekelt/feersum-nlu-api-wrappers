""" Example: Shows how to create, train and use a fuzzy Levenshtein text classifier. """

import urllib3

import feersum_nlu
from feersum_nlu.rest import ApiException
from examples import feersumnlu_host, feersum_nlu_auth_token

# Configure API key authorization: APIKeyHeader
configuration = feersum_nlu.Configuration()

# configuration.api_key['AUTH_TOKEN'] = feersum_nlu_auth_token
configuration.api_key['X-Auth-Token'] = feersum_nlu_auth_token  # Alternative auth key header!

configuration.host = feersumnlu_host

api_instance = feersum_nlu.TextClassifiersApi(feersum_nlu.ApiClient(configuration))

instance_name = 'test_txt_clsfr'

create_details = feersum_nlu.TextClassifierCreateDetails(name=instance_name,
                                                         desc="Test text classifier.",
                                                         load_from_store=False)

# The training samples.
labelled_text_sample_list = []

labelled_text_sample_list.append(feersum_nlu.LabelledTextSample(
    text="Game of Thrones Season 1",
    label="GOT_S1"))
labelled_text_sample_list.append(feersum_nlu.LabelledTextSample(
    text="GOT Season 1",
    label="GOT_S1"))
labelled_text_sample_list.append(feersum_nlu.LabelledTextSample(
    text="Game of Thrones Season 2",
    label="GOT_S2"))
labelled_text_sample_list.append(feersum_nlu.LabelledTextSample(
    text="GOT Season 2",
    label="GOT_S2"))

labelled_text_sample_list.append(feersum_nlu.LabelledTextSample(
    text="Rugby World Cup Semi-Final",
    label="RUGBY_WC_SF"))

labelled_text_sample_list.append(feersum_nlu.LabelledTextSample(
    text="Rugby World Cup Final",
    label="RUGBY_WC_FIN"))

labelled_text_sample_list.append(feersum_nlu.LabelledTextSample(
    text="Rugby World Cup Semi-Final",
    label="RUGBY_WC_SF"))

labelled_text_sample_list.append(feersum_nlu.LabelledTextSample(
    text="Silicon Valley Season 1",
    label="SIL_VAL_S1"))

train_details = feersum_nlu.TrainDetails(immediate_mode=True,
                                         temperature=0.1,
                                         clsfr_algorithm="nearest_neighbour_fuzzy",
                                         )

# text_input = feersum_nlu.TextInput("When is Silicon Valley on?")
text_input = feersum_nlu.TextInput("When is the Rugby on?")

caller_name = 'example_caller'

print()

try:
    #    print("Update the model params:")
    #    model_params = feersum_nlu.ModelParams(readonly=False)
    #    api_response = api_instance.text_classifier_set_params(instance_name, model_params, x_caller=caller_name)
    #    print(" type(api_response)", type(api_response))
    #    print(" api_response", api_response)
    #    print()

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

    print("Train the text classifier:")
    api_response = api_instance.text_classifier_train(instance_name, train_details)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Classify text:")
    api_response = api_instance.text_classifier_retrieve(instance_name, text_input, x_caller=caller_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    # print("Get the model params:")
    # api_response = api_instance.text_classifier_get_params(instance_name)
    # print(" type(api_response)", type(api_response))
    # print(" api_response", api_response)
    # print()

    # print("Delete named loaded text classifier:")
    # api_response = \
    api_instance.text_classifier_del(instance_name)
    # print(" type(api_response)", type(api_response))
    # print(" api_response", api_response)
    # print()

    # print("Vaporise named loaded text classifier:")
    # api_response = \
    api_instance.text_classifier_vaporise(instance_name)
    # print(" type(api_response)", type(api_response))
    # print(" api_response", api_response)
    # print()

except ApiException as e:
    print("Exception when calling a text classifier operation: %s\n" % e)
except urllib3.exceptions.HTTPError as e:
    print("Connection HTTPError! %s\n" % e)
