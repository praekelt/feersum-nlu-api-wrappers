from typing import Dict
import urllib3

import feersum_nlu
from feersum_nlu.rest import ApiException


# =======================================
# =======================================
# =======================================
def export_model(model_name: str, model_type: str, configuration: feersum_nlu.Configuration) -> Dict:
    """
    Export the model to a json object {"instance_detail":, "training_samples":, "testing_samples":}

    :param model_name:
    :param model_type:
    :param configuration:
    :return: {"instance_detail":, "training_samples":, "testing_samples":} - instance_detail is None if export not supported!
    """

    try:
        # Get the instance_detail if model type is supported for export.
        if model_type == 'language_recogniser':
            api_instance = feersum_nlu.LanguageRecognisersApi(feersum_nlu.ApiClient(configuration))
            instance_detail = api_instance.language_recogniser_get_details(model_name)
        elif model_type == 'text_classifier':
            api_instance = feersum_nlu.TextClassifiersApi(feersum_nlu.ApiClient(configuration))
            instance_detail = api_instance.text_classifier_get_details(model_name)
        elif model_type == 'intent_classifier':
            api_instance = feersum_nlu.IntentClassifiersApi(feersum_nlu.ApiClient(configuration))
            instance_detail = api_instance.intent_classifier_get_details(model_name)
        elif model_type == 'faq_matcher':
            api_instance = feersum_nlu.FaqMatchersApi(feersum_nlu.ApiClient(configuration))
            instance_detail = api_instance.faq_matcher_get_details(model_name)
        elif model_type == 'duckling_entity_extractor':
            api_instance = feersum_nlu.DucklingEntityExtractorsApi(feersum_nlu.ApiClient(configuration))
            instance_detail = api_instance.duckling_entity_extractor_get_details(model_name)
        elif model_type == 'regex_entity_extractor':
            api_instance = feersum_nlu.RegexEntityExtractorsApi(feersum_nlu.ApiClient(configuration))
            instance_detail = api_instance.regex_entity_extractor_get_details(model_name)
        elif model_type == 'sim_word_entity_extractor':
            api_instance = feersum_nlu.SimWordEntityExtractorsApi(feersum_nlu.ApiClient(configuration))
            instance_detail = api_instance.sim_word_entity_extractor_get_details(model_name)
        elif model_type == 'person_name_entity_extractor':
            api_instance = feersum_nlu.PersonNameEntityExtractorsApi(feersum_nlu.ApiClient(configuration))
            instance_detail = api_instance.person_name_entity_extractor_get_details(model_name)
        else:
            api_instance = None
            instance_detail = None

        # Create instance detail dict to return.
        if instance_detail is not None:
            instance_detail_dict = instance_detail.to_dict()
        else:
            instance_detail_dict = None

        # Get train and test data when model has it.
        if api_instance is not None:
            if model_type == 'text_classifier':
                training_samples = api_instance.text_classifier_get_training_samples(model_name)
                testing_samples = api_instance.text_classifier_get_testing_samples(model_name)
            elif model_type == 'intent_classifier':
                training_samples = api_instance.intent_classifier_get_training_samples(model_name)
                testing_samples = api_instance.intent_classifier_get_testing_samples(model_name)
            elif model_type == 'faq_matcher':
                training_samples = api_instance.faq_matcher_get_training_samples(model_name)
                testing_samples = api_instance.faq_matcher_get_testing_samples(model_name)
            else:
                training_samples = None
                testing_samples = None
        else:
            training_samples = None
            testing_samples = None

        return {"instance_detail": instance_detail_dict,
                "training_samples": training_samples,
                "testing_samples": testing_samples}

    except ApiException as e:
        print("Exception when calling an api endpoint: %s\n" % e)
        return {"instance_detail": None, "training_samples": None, "testing_samples": None}
    except urllib3.exceptions.HTTPError as e:
        print("Connection HTTPError! %s\n" % e)
        return {"instance_detail": None, "training_samples": None, "testing_samples": None}


# =======================================
# =======================================
# =======================================
def import_model(model_name: str, model_type: str, configuration: feersum_nlu.Configuration,
                 model_dict: Dict):
    """
    Imprt the model to a json object {"instance_detail":, "training_samples":, "testing_samples":}

    :param model_name:
    :param model_type:
    :param configuration:
    :param model_dict: {"instance_detail":, "training_samples":, "testing_samples":}
    :return: None
    """

    instance_detail = model_dict.get("instance_detail")
    training_samples = model_dict.get("training_samples")
    testing_samples = model_dict.get("testing_samples")

    desc = instance_detail.get('desc')
    long_name = instance_detail.get('long_name')

    try:
        if model_type == 'language_recogniser':
            lid_model_file = instance_detail.get('lid_model_file')

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

            print("  train_details =", str(train_details.to_dict()))

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

            train_threshold = instance_detail.get('threshold')

            word_manifold_list_json = instance_detail.get('word_manifold_list')
            word_manifold_list = []

            for word_manifold_json in word_manifold_list_json:
                language = word_manifold_json.get("label")
                manifold = word_manifold_json.get("word_manifold")

                if language is not None:
                    word_manifold_list.append(feersum_nlu.LabeledWordManifold(language, manifold))

            train_details = feersum_nlu.TrainDetails(threshold=train_threshold,
                                                     word_manifold_list=word_manifold_list)

            print("  train_details =", str(train_details.to_dict()))

            print("  train_details =", str(train_details.to_dict()))

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

            train_threshold = instance_detail.get('threshold')

            word_manifold_list_json = instance_detail.get('word_manifold_list')
            word_manifold_list = []

            for word_manifold_json in word_manifold_list_json:
                language = word_manifold_json.get("label")
                manifold = word_manifold_json.get("word_manifold")

                if language is not None:
                    word_manifold_list.append(feersum_nlu.LabeledWordManifold(language, manifold))

            train_details = feersum_nlu.TrainDetails(threshold=train_threshold,
                                                     word_manifold_list=word_manifold_list)

            print("  train_details =", str(train_details.to_dict()))

            print("  Training model ... ", flush=True)
            api_response = api_instance.faq_matcher_train(model_name, train_details)

            print()

            print("  Get the details of the imported model ... ", flush=True)
            api_response = api_instance.faq_matcher_get_details(model_name)
            print("   api_response", api_response)
        elif model_type == 'duckling_entity_extractor':
            reference_time = instance_detail.get('reference_time')

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
            regex = instance_detail.get('regex')

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
            similar_words = instance_detail.get('similar_words')
            sim_word_threshold = instance_detail.get('threshold')
            word_manifold = instance_detail.get('word_manifold')

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

