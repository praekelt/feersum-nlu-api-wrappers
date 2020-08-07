""" Example: Shows how to load a pre-trained text classifier model from the store. """

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
                                                         load_from_store=True)

text_input = feersum_nlu.TextInput("Where can I get a quote?")

print()

try:
    print("Create the text classifier:")
    api_response = api_instance.text_classifier_create(create_details)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the details of all loaded text classifiers:")
    api_response = api_instance.text_classifier_get_details_all()
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the details of specific named loaded FAQ matcher:")
    api_response = api_instance.text_classifier_get_details(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    # Get the classifier's possible labels. Might be inferred from the training data, but guaranteed to be available
    # after training.
    print("Get the labels of named loaded FAQ matcher:")
    api_response = api_instance.text_classifier_get_labels(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    # print("Update the parameters:")
    # model_params = \
    #     feersum_nlu.ModelParams(threshold=0.8, desc="Example desc.", long_name="A longer name.")
    # api_response = api_instance.text_classifier_set_params(instance_name, model_params)
    # print(" type(api_response)", type(api_response))
    # print(" api_response", api_response)
    # print()

    print("Match a question:")
    api_response = api_instance.text_classifier_retrieve(instance_name, text_input)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the model params:")
    api_response = api_instance.text_classifier_get_params(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Update the model params:")
    model_params = feersum_nlu.ModelParams(threshold=0.8, readonly=True)
    api_response = api_instance.text_classifier_set_params(instance_name, model_params)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the model params:")
    api_response = api_instance.text_classifier_get_params(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

except ApiException as e:
    print("Exception when calling a text classifier operation: %s\n" % e)
except urllib3.exceptions.HTTPError:
    print("Connection HTTPError!")
