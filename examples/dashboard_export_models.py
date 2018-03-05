""" Example: Shows how to get info about the service using the Dashboard endpoint.  """

import json
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

api_instance = feersum_nlu.DashboardApi(feersum_nlu.ApiClient(configuration))

print()

try:
    print("Save dashboard models to disk...", end='', flush=True)
    dashboard_detail = api_instance.dashboard_get_details()  # type: feersum_nlu.models.dashboard_detail.DashboardDetail

    for model in dashboard_detail.model_list:
        print(".", end='', flush=True)
        if not model.trashed:
            if model.model_type == 'text_classifier':
                api_instance = feersum_nlu.TextClassifiersApi(feersum_nlu.ApiClient(configuration))
                instance_detail = api_instance.text_classifier_get_details(model.name)
            elif model.model_type == 'intent_classifier':
                api_instance = feersum_nlu.IntentClassifiersApi(feersum_nlu.ApiClient(configuration))
                instance_detail = api_instance.intent_classifier_get_details(model.name)
            elif model.model_type == 'faq_matcher':
                api_instance = feersum_nlu.FaqMatchersApi(feersum_nlu.ApiClient(configuration))
                instance_detail = api_instance.faq_matcher_get_details(model.name)
            elif model.model_type == 'regex_entity_extractor':
                api_instance = feersum_nlu.RegexEntityExtractorsApi(feersum_nlu.ApiClient(configuration))
                instance_detail = api_instance.regex_entity_extractor_get_details(model.name)
            elif model.model_type == 'sim_word_entity_extractor':
                api_instance = feersum_nlu.SimWordEntityExtractorsApi(feersum_nlu.ApiClient(configuration))
                instance_detail = api_instance.sim_word_entity_extractor_get_details(model.name)
            else:
                instance_detail = None

            if instance_detail is not None:
                json_dict = instance_detail.to_dict()

                filename = model.name + "_" + feersum_nlu_auth_token + "." + model.model_type

                with open(filename + ".json", "w") as json_file:
                    json.dump(json_dict, json_file, sort_keys=True, indent=4)

                # Save train and test data.
                if model.model_type == 'text_classifier':
                    training_samples = api_instance.text_classifier_get_training_samples(model.name)
                    testing_samples = api_instance.text_classifier_get_testing_samples(model.name)
                elif model.model_type == 'intent_classifier':
                    training_samples = api_instance.intent_classifier_get_training_samples(model.name)
                    testing_samples = api_instance.intent_classifier_get_testing_samples(model.name)
                elif model.model_type == 'faq_matcher':
                    training_samples = api_instance.faq_matcher_get_training_samples(model.name)
                    testing_samples = api_instance.faq_matcher_get_testing_samples(model.name)
                else:
                    training_samples = None
                    testing_samples = None

                if training_samples is not None:
                    with open(filename + ".train.csv", "w", newline='') as csv_file:
                        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                        for sample in training_samples:
                            # print('(', sample.label, ',', sample.text, ')')
                            csv_writer.writerow([sample.label, sample.text])

                if testing_samples is not None:
                    with open(filename + ".test.csv", "w", newline='') as csv_file:
                        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                        for sample in testing_samples:
                            # print('(', sample.label, ',', sample.text, ')')
                            csv_writer.writerow([sample.label, sample.text])

    print(' done.', flush=True)

except ApiException as e:
    print("Exception when calling DashboardApi->dashboard_get_details: %s\n" % e)
except urllib3.exceptions.HTTPError as e:
    print("Connection HTTPError! %s\n" % e)
