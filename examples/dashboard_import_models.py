""" Example: Shows how to get info about the service using the Dashboard endpoint.  """

import json
import urllib3
import csv

import feersum_nlu
from feersum_nlu.rest import ApiException
from examples import feersumnlu_host, feersum_nlu_auth_token

print()

# Configure API key authorization: APIKeyHeader
configuration = feersum_nlu.Configuration()

# configuration.api_key['AUTH_TOKEN'] = feersum_nlu_auth_token
configuration.api_key['X-Auth-Token'] = feersum_nlu_auth_token  # Alternative auth key header!

configuration.host = feersumnlu_host

# === List of exported models to be imported ===
model_list = [("faq_model_name", "faq_matcher")]

# model_list = [("Help", "faq_matcher")]

# === Import models one by one ===
for model_name, model_type in model_list:
    print("#####################")
    print("#####################")

    filename_model = "exported_models/" + model_name + "_" + feersum_nlu_auth_token + "." + model_type + ".json"
    filename_train_csv = "exported_models/" + model_name + "_" + feersum_nlu_auth_token + "." + model_type + ".train.csv"
    filename_test_csv = "exported_models/" + model_name + "_" + feersum_nlu_auth_token + "." + model_type + ".test.csv"

    print('filename_model =', filename_model, flush=True)
    print('filename_train_csv =', filename_train_csv, flush=True)
    print('filename_test_csv =', filename_test_csv, flush=True)

    print()

    try:
        print("model_name =", model_name)
        print("model_type =", model_type)

        with open(filename_model) as json_file:
            json_model = json.load(json_file)
            print("  json_model = ", json_model)

            desc = json_model.get('desc')
            long_name = json_model.get('long_name')

            # Try to get training samples.
            training_samples = []

            try:
                with open(filename_train_csv, newline='') as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')

                    for row in csv_reader:
                        training_samples.append(feersum_nlu.LabelledTextSample(text=row[1], label=row[0]))
            except FileNotFoundError:
                pass

            print("  training_samples = ", len(training_samples))

            # Try to get testing samples.
            testing_samples = []

            try:
                with open(filename_test_csv, newline='') as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')

                    for row in csv_reader:
                        testing_samples.append(feersum_nlu.LabelledTextSample(text=row[1], label=row[0]))
            except FileNotFoundError:
                pass

            print("  testing_samples = ", len(testing_samples))

            # === ===
            # === ===
            # === ===

            if model_type == 'language_recogniser':
                lid_model_file = json_model.get('lid_model_file')

                create_details = feersum_nlu.LanguageRecogniserCreateDetails(name=model_name,
                                                                             desc=desc,
                                                                             long_name=long_name,
                                                                             load_from_store=False,
                                                                             lid_model_file=lid_model_file)

                api_instance = feersum_nlu.LanguageRecognisersApi(feersum_nlu.ApiClient(configuration))

                print("  Creating model ... ", flush=True)
                api_response = api_instance.language_recogniser_create(create_details)

                train_details = feersum_nlu.TrainDetails()

                print()

                print("  Get the details of the imported model ... ", flush=True)
                api_response = api_instance.language_recogniser_get_details(model_name)
                print("   api_response", api_response)
            elif model_type == 'text_classifier':
                create_details = feersum_nlu.TextClassifierCreateDetails(name=model_name,
                                                                         desc=desc,
                                                                         long_name=long_name,
                                                                         load_from_store=False)

                api_instance = feersum_nlu.TextClassifiersApi(feersum_nlu.ApiClient(configuration))

                print("  Creating model ... ", flush=True)
                api_response = api_instance.text_classifier_create(create_details)

                if len(training_samples):
                    api_response = api_instance.text_classifier_add_training_samples(model_name, training_samples)

                if len(testing_samples):
                    api_response = api_instance.text_classifier_add_testing_samples(model_name, testing_samples)

                train_details = feersum_nlu.TrainDetails()

                print("  Training model ... ", flush=True)
                api_response = api_instance.text_classifier_train(model_name, train_details)

                print()

                print("  Get the details of the imported model ... ", flush=True)
                api_response = api_instance.text_classifier_get_details(model_name)
                print("   api_response", api_response)
            elif model_type == 'intent_classifier':
                create_details = feersum_nlu.IntentClassifierCreateDetails(name=model_name,
                                                                           desc=desc,
                                                                           long_name=long_name,
                                                                           lid_model_file="lid_za",
                                                                           load_from_store=False)

                api_instance = feersum_nlu.IntentClassifiersApi(feersum_nlu.ApiClient(configuration))

                print("  Creating model ... ", flush=True)
                api_response = api_instance.intent_classifier_create(create_details)

                if len(training_samples):
                    api_response = api_instance.intent_classifier_add_training_samples(model_name, training_samples)

                if len(testing_samples):
                    api_response = api_instance.intent_classifier_add_testing_samples(model_name, testing_samples)

                train_threshold = json_model.get('threshold')
                word_manifold_list_json = json_model.get('word_manifold_list')
                word_manifold_list = [feersum_nlu.LabeledWordManifold('eng', 'feers_wm_eng')]

                train_details = feersum_nlu.TrainDetails(threshold=train_threshold, word_manifold_list=word_manifold_list)

                print("  Training model ... ", flush=True)
                api_response = api_instance.intent_classifier_train(model_name, train_details)

                print()

                print("  Get the details of the imported model ... ", flush=True)
                api_response = api_instance.intent_classifier_get_details(model_name)
                print("   api_response", api_response)
            elif model_type == 'faq_matcher':
                create_details = feersum_nlu.FaqMatcherCreateDetails(name=model_name,
                                                                     desc=desc,
                                                                     long_name=long_name,
                                                                     lid_model_file="lid_za",
                                                                     load_from_store=False)

                api_instance = feersum_nlu.FaqMatchersApi(feersum_nlu.ApiClient(configuration))

                print("  Creating model ... ", flush=True)
                api_response = api_instance.faq_matcher_create(create_details)

                if len(training_samples):
                    api_response = api_instance.faq_matcher_add_training_samples(model_name, training_samples)

                if len(testing_samples):
                    api_response = api_instance.faq_matcher_add_testing_samples(model_name, testing_samples)

                train_threshold = json_model.get('threshold')
                word_manifold_list_json = json_model.get('word_manifold_list')
                word_manifold_list = [feersum_nlu.LabeledWordManifold('eng', 'feers_wm_eng')]

                train_details = feersum_nlu.TrainDetails(threshold=train_threshold, word_manifold_list=word_manifold_list)

                print("  Training model ... ", flush=True)
                api_response = api_instance.faq_matcher_train(model_name, train_details)

                print()

                print("  Get the details of the imported model ... ", flush=True)
                api_response = api_instance.faq_matcher_get_details(model_name)
                print("   api_response", api_response)
            elif model_type == 'duckling_entity_extractor':
                reference_time = json_model.get('reference_time')

                create_details = feersum_nlu.DucklingEntityExtractorCreateDetails(name=model_name,
                                                                                  desc=desc,
                                                                                  long_name=long_name,
                                                                                  reference_time=reference_time,
                                                                                  load_from_store=False)

                api_instance = feersum_nlu.DucklingEntityExtractorsApi(feersum_nlu.ApiClient(configuration))

                print("  Creating model ... ", flush=True)
                api_response = api_instance.duckling_entity_extractor_create(create_details)

                print()

                print("  Get the details of the imported model ... ", flush=True)
                api_response = api_instance.duckling_entity_extractor_get_details(model_name)
                print("   api_response", api_response)
            elif model_type == 'regex_entity_extractor':
                regex = json_model.get('regex')

                create_details = feersum_nlu.RegexEntityExtractorCreateDetails(name=model_name,
                                                                               desc=desc,
                                                                               long_name=long_name,
                                                                               regex=regex,
                                                                               load_from_store=False)

                api_instance = feersum_nlu.RegexEntityExtractorsApi(feersum_nlu.ApiClient(configuration))

                print("  Creating model ... ", flush=True)
                api_response = api_instance.regex_entity_extractor_create(create_details)

                print()

                print("  Get the details of the imported model ... ", flush=True)
                api_response = api_instance.regex_entity_extractor_get_details(model_name)
                print("   api_response", api_response)
            elif model_type == 'sim_word_entity_extractor':
                similar_words = json_model.get('similar_words')
                sim_word_threshold = json_model.get('threshold')
                word_manifold = json_model.get('word_manifold')

                create_details = feersum_nlu.SimWordEntityExtractorCreateDetails(name=model_name,
                                                                                 desc=desc,
                                                                                 long_name=long_name,
                                                                                 similar_words=similar_words,
                                                                                 threshold=sim_word_threshold,
                                                                                 word_manifold=word_manifold,
                                                                                 load_from_store=False)

                api_instance = feersum_nlu.SimWordEntityExtractorsApi(feersum_nlu.ApiClient(configuration))

                print("  Creating model ... ", flush=True)
                api_response = api_instance.sim_word_entity_extractor_create(create_details)

                print()

                print("  Get the details of the imported model ... ", flush=True)
                api_response = api_instance.sim_word_entity_extractor_get_details(model_name)
                print("   api_response", api_response)
            elif model_type == 'person_name_entity_extractor':
                create_details = feersum_nlu.PersonNameEntityExtractorCreateDetails(name=model_name,
                                                                                    desc=desc,
                                                                                    long_name=long_name,
                                                                                    load_from_store=False)

                api_instance = feersum_nlu.PersonNameEntityExtractorsApi(feersum_nlu.ApiClient(configuration))

                print("  Creating model ... ", flush=True)
                api_response = api_instance.person_name_entity_extractor_create(create_details)

                print()

                print("  Get the details of the imported model ... ", flush=True)
                api_response = api_instance.person_name_entity_extractor_get_details(model_name)
                print("   api_response", api_response)

    except ApiException as e:
        print("Exception when calling an api endpoint: %s\n" % e)
    except urllib3.exceptions.HTTPError as e:
        print("Connection HTTPError! %s\n" % e)

    print()

print("Done.", flush=True)
