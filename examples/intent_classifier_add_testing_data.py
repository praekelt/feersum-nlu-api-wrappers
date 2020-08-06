""" Example: Shows how to create, train and use an intent classifier. """

import urllib3
import csv

import feersum_nlu
from feersum_nlu.rest import ApiException
from examples import feersumnlu_host, feersum_nlu_auth_token

# Configure API key authorization: APIKeyHeader
configuration = feersum_nlu.Configuration()

# configuration.api_key['AUTH_TOKEN'] = feersum_nlu_auth_token
configuration.api_key['X-Auth-Token'] = feersum_nlu_auth_token  # Alternative auth key header!

configuration.host = feersumnlu_host

api_instance = feersum_nlu.IntentClassifiersApi(feersum_nlu.ApiClient(configuration))

instance_name = 'navigation2'
caller_name = 'example_caller'

labelled_text_sample_list = []
with open('Testing_utterances_import_2020-07-30.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(reader)

    for row in reader:
        label = row[0]
        text = row[1]
        labelled_text_sample_list.append(feersum_nlu.LabelledTextSample(text=text,
                                                                        label=label))

train_details = feersum_nlu.TrainDetails(immediate_mode=True)

print()

try:
    print("Get the details of the specific named loaded intent classifier:")
    api_response = api_instance.intent_classifier_get_details(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    exit(0)

    # print("Del the testing samples of the intent classifier:")
    # api_response = api_instance.intent_classifier_del_testing_samples_all(instance_name)
    # print(" type(api_response)", type(api_response))
    # print(" api_response", api_response)
    # print()

    print("Add testing samples to the intent classifier:")
    api_response = api_instance.intent_classifier_add_testing_samples(instance_name, labelled_text_sample_list)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    # print("Get the testing samples of the intent classifier:")
    # api_response = api_instance.intent_classifier_get_testing_samples(instance_name)
    # print(" type(api_response)", type(api_response))
    # print(" api_response", api_response)
    # print()

    print("Train the intent classifier:")
    api_response = api_instance.intent_classifier_train(instance_name, train_details)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

except ApiException as e:
    print("Exception when calling an intent classifier operation: %s\n" % e)
except urllib3.exceptions.HTTPError as e:
    print("Connection HTTPError! %s\n" % e)
