""" Example: Shows how to create, train and use an FAQ matcher. """

import os
import urllib3
import csv

import feersum_nlu
from feersum_nlu.rest import ApiException

# Try to get the API key from your OS environment, else use 'YOUR_API_KEY' as the default value in the code below.
# You may use any environment variable you want, it doesn't have to be 'FEERSUM_NLU_AUTH_TOKEN'.
feersum_nlu_auth_token = os.environ.get('FEERSUM_NLU_AUTH_TOKEN', 'YOUR_API_KEY')
print('feersum_nlu_auth_token = ', feersum_nlu_auth_token)

# Configure API key authorization: APIKeyHeader
feersum_nlu.configuration.api_key['AUTH_TOKEN'] = feersum_nlu_auth_token

# feersum_nlu.configuration.host = "http://127.0.0.1:8100/nlu/v2"
feersum_nlu.configuration.host = "https://nlu.playground.feersum.io:443/nlu/v2"

api_instance = feersum_nlu.FaqMatchersApi()

instance_name = 'FNB_FAQ'

print()

try:
    print("Get the training samples of the FAQ matcher:")
    training_samples = api_instance.faq_matcher_get_training_samples(instance_name)
    print(" type(training_samples)", type(training_samples))
    print(" training_samples", training_samples)
    print()

    print("Get the details of specific named loaded FAQ matcher:")
    api_response = api_instance.faq_matcher_get_details(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    # Get the classifier's possible labels. Might be inferred from the training data, but guaranteed to be available
    # after training.
    print("Get the labels of named loaded FAQ matcher:")
    api_response = api_instance.faq_matcher_get_labels(instance_name)
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
            label = sample.get('label')
            text = sample.get('text')

            if (label is not None) and (text is not None):
                csv_writer.writerow([label, text])

except ApiException as e:
    print("Exception when calling an FAQ matcher operation: %s\n" % e)
except urllib3.exceptions.MaxRetryError:
    print("Connection MaxRetryError!")


