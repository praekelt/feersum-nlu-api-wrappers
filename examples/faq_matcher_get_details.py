""" Example: Shows how to create, train and use an FAQ matcher. """

import urllib3

import feersum_nlu
from feersum_nlu.rest import ApiException
from examples import feersumnlu_host, feersum_nlu_auth_token

# Configure API key authorization: APIKeyHeader
configuration = feersum_nlu.Configuration()

# configuration.api_key['AUTH_TOKEN'] = feersum_nlu_auth_token
configuration.api_key['X-Auth-Token'] = feersum_nlu_auth_token  # Alternative auth key header!

configuration.host = feersumnlu_host

api_instance = feersum_nlu.FaqMatchersApi(feersum_nlu.ApiClient(configuration))

instance_name = 'test_faq'

# text_input_0 = feersum_nlu.TextInput("Can I give my baby tea?",
#                                      lang_code=None)  # optional language hint.

caller_name = 'example_caller'

print()

# The testing samples.
text_sample_list = []

try:
    print("Get the parameters:")
    api_response = api_instance.faq_matcher_get_params(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the details of specific named loaded FAQ matcher:")
    api_response = api_instance.faq_matcher_get_details(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    cm_labels = api_response.cm_labels
    print()

    # print("Get the labels of named loaded FAQ matcher:")
    # api_response = api_instance.faq_matcher_get_details(instance_name)
    # print(" type(api_response)", type(api_response))
    # print(" api_response", api_response)
    # print()

    print("Get some curate details of training matrix of specific named loaded FAQ matcher:")
    # Use the same labels as returned in the confusion matrix.
    label_pair = feersum_nlu.ClassLabelPair(matrix_name='train', true_label='76', predicted_label='24')
    api_response = api_instance.faq_matcher_curate(instance_name, label_pair)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

except ApiException as e:
    print("Exception when calling an FAQ matcher operation: %s\n" % e)
except urllib3.exceptions.HTTPError as e:
    print("Connection HTTPError! %s\n" % e)
