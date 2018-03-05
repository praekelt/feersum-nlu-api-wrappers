""" Example: Shows how to download and save the training samples of an intent classifier. """

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

instance_name = 'test_intent_clsfr'

print()

try:
    print("Get the training samples of the intent classifier:")
    training_samples = api_instance.intent_classifier_get_training_samples(instance_name)
    print(" type(training_samples)", type(training_samples))
    print(" training_samples", training_samples)
    print()

    print("Get the details of specific named loaded intent classifier:")
    api_response = api_instance.intent_classifier_get_details(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    # Get the classifier's possible labels. Might be inferred from the training data, but guaranteed to be available
    # after training.
    print("Get the labels of named loaded intent classifier:")
    api_response = api_instance.intent_classifier_get_labels(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    # ===
    # Write the training samples to a csv file.
    with open('training_samples.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile,
                                delimiter=',',
                                quotechar='"',
                                quoting=csv.QUOTE_MINIMAL)

        for sample in training_samples:
            label = sample.label
            text = sample.text

            if (label is not None) and (text is not None):
                csv_writer.writerow([label, text])

except ApiException as e:
    print("Exception when calling an intent classifier operation: %s\n" % e)
except urllib3.exceptions.HTTPError as e:
    print("Connection HTTPError! %s\n" % e)
