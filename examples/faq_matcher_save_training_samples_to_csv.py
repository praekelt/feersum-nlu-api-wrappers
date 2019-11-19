""" Example: Shows how to download and save the training samples of a FAQ matcher. """

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

api_instance = feersum_nlu.FaqMatchersApi(feersum_nlu.ApiClient(configuration))

instance_name = 'test_faq_mtchr'

print()

try:
    print("Get the details of specific named loaded FAQ matcher:")
    api_response = api_instance.faq_matcher_get_details(instance_name)
    print(" type(api_response)", type(api_response), flush=True)
    print(" api_response", api_response, flush=True)
    print()

    num_training_samples = api_response.num_training_samples
    print(num_training_samples)

    training_samples = []
    sample_batch_size = 1000

    for i in range(0, num_training_samples, sample_batch_size):
        current_batch_size = min(sample_batch_size + i, num_training_samples) - i
        print(i, current_batch_size)
        training_samples_batch = api_instance.faq_matcher_get_training_samples(instance_name,
                                                                               index=i,
                                                                               len=current_batch_size)
        training_samples.extend(training_samples_batch)

    # print("Get the training samples of the FAQ matcher:")
    # training_samples = api_instance.faq_matcher_get_training_samples(instance_name)
    # print(" type(training_samples)", type(training_samples), flush=True)
    # print(" training_samples", training_samples, flush=True)
    # print()

    # Get the classifier's possible labels. Might be inferred from the training data, but guaranteed to be available
    # after training.
    print("Get the labels of named loaded FAQ matcher:")
    api_response = api_instance.faq_matcher_get_labels(instance_name)
    print(" type(api_response)", type(api_response), flush=True)
    # print(" api_response", api_response, flush=True)
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
            lang_code = str(sample.lang_code)

            if (label is not None) and (text is not None):
                csv_writer.writerow([label, text, lang_code])

except ApiException as e:
    print("Exception when calling an FAQ matcher operation: %s\n" % e, flush=True)
except urllib3.exceptions.HTTPError as e:
    print("Connection HTTPError! %s\n" % e)
