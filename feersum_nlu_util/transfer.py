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
        if model_type == 'text_classifier':
            api_instance = feersum_nlu.TextClassifiersApi(feersum_nlu.ApiClient(configuration))
            instance_detail = api_instance.text_classifier_get_details(model_name)
        elif model_type == 'text_dataset':
            api_instance = feersum_nlu.TextDatasetsApi(feersum_nlu.ApiClient(configuration))
            instance_detail = api_instance.text_dataset_get_details(model_name)
        elif model_type == 'intent_classifier':
            api_instance = feersum_nlu.IntentClassifiersApi(feersum_nlu.ApiClient(configuration))
            instance_detail = api_instance.intent_classifier_get_details(model_name)
        elif model_type == 'faq_matcher':
            api_instance = feersum_nlu.FaqMatchersApi(feersum_nlu.ApiClient(configuration))
            instance_detail = api_instance.faq_matcher_get_details(model_name)
        elif model_type == 'language_recogniser':
            api_instance = feersum_nlu.LanguageRecognisersApi(feersum_nlu.ApiClient(configuration))
            instance_detail = api_instance.language_recogniser_get_details(model_name)
        elif model_type == 'regex_entity_extractor':
            api_instance = feersum_nlu.RegexEntityExtractorsApi(feersum_nlu.ApiClient(configuration))
            instance_detail = api_instance.regex_entity_extractor_get_details(model_name)
        # elif model_type == 'person_name_entity_extractor':
        #     api_instance = feersum_nlu.PersonNameEntityExtractorsApi(feersum_nlu.ApiClient(configuration))
        #     instance_detail = api_instance.person_name_entity_extractor_get_details(model_name)
        elif model_type == 'duckling_entity_extractor':
            api_instance = feersum_nlu.DucklingEntityExtractorsApi(feersum_nlu.ApiClient(configuration))
            instance_detail = api_instance.duckling_entity_extractor_get_details(model_name)
        elif model_type == 'synonym_entity_extractor':
            api_instance = feersum_nlu.SynonymEntityExtractorsApi(feersum_nlu.ApiClient(configuration))
            instance_detail = api_instance.synonym_entity_extractor_get_details(model_name)
        elif model_type == 'crf_entity_extractor':
            api_instance = feersum_nlu.CrfEntityExtractorsApi(feersum_nlu.ApiClient(configuration))
            instance_detail = api_instance.crf_entity_extractor_get_details(model_name)
        elif model_type == 'data_object':
            api_instance = feersum_nlu.DataObjectsApi(feersum_nlu.ApiClient(configuration))
            instance_detail = api_instance.data_object_get_details(model_name)
        elif model_type == 'image_classifier':
            api_instance = feersum_nlu.ImageClassifiersApi(feersum_nlu.ApiClient(configuration))
            instance_detail = api_instance.image_classifier_get_details(model_name)
        elif model_type == 'image_dataset':
            api_instance = feersum_nlu.ImageDatasetsApi(feersum_nlu.ApiClient(configuration))
            instance_detail = api_instance.image_dataset_get_details(model_name)
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
                samples = None
            elif model_type == 'text_dataset':
                training_samples = None
                testing_samples = None
                samples = api_instance.text_dataset_get_samples(model_name)
            elif model_type == 'intent_classifier':
                training_samples = api_instance.intent_classifier_get_training_samples(model_name)
                testing_samples = api_instance.intent_classifier_get_testing_samples(model_name)
                samples = None
            elif model_type == 'faq_matcher':
                training_samples = api_instance.faq_matcher_get_training_samples(model_name)
                testing_samples = api_instance.faq_matcher_get_testing_samples(model_name)
                samples = None
            elif model_type == 'crf_entity_extractor':
                training_samples = api_instance.crf_entity_extractor_get_training_samples(model_name)
                testing_samples = api_instance.crf_entity_extractor_get_testing_samples(model_name)
                samples = None
            elif model_type == 'synonym_entity_extractor':
                training_samples = api_instance.synonym_entity_extractor_get_training_samples(model_name)
                testing_samples = api_instance.synonym_entity_extractor_get_testing_samples(model_name)
                samples = None
            elif model_type == 'image_classifier':
                training_samples = api_instance.image_classifier_get_training_samples(model_name)
                testing_samples = api_instance.image_classifier_get_testing_samples(model_name)
                samples = None
            elif model_type == 'image_dataset':
                training_samples = None
                testing_samples = None
                samples = api_instance.image_dataset_get_samples(model_name)
            else:
                training_samples = None
                testing_samples = None
                samples = None
        else:
            training_samples = None
            testing_samples = None
            samples = None

        return {"instance_detail": instance_detail_dict,
                "training_samples": training_samples,
                "testing_samples": testing_samples,
                "samples": samples}

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
                 model_dict: Dict) -> bool:
    """
    Import the model to a json object {"instance_detail":, "training_samples":, "testing_samples":}

    :param model_name:
    :param model_type:
    :param configuration:
    :param model_dict: {"instance_detail":, "training_samples":, "testing_samples":}
    :return: None
    """

    instance_detail = model_dict.get("instance_detail")

    if instance_detail is None:
        return False

    training_samples_json = model_dict.get("training_samples")
    testing_samples_json = model_dict.get("testing_samples")

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

            training_samples = []
            testing_samples = []

            if training_samples_json:
                for sample in training_samples_json:
                    training_samples.append(feersum_nlu.LabelledTextSample(text=sample.get("text"),
                                                                           label=sample.get("label"),
                                                                           lang_code=sample.get("lang_code"),
                                                                           comment=sample.get("comment")))
            if testing_samples_json:
                for sample in testing_samples_json:
                    testing_samples.append(feersum_nlu.LabelledTextSample(text=sample.get("text"),
                                                                          label=sample.get("label"),
                                                                          lang_code=sample.get("lang_code"),
                                                                          comment=sample.get("comment")))

            if len(training_samples):
                api_response = api_instance.text_classifier_add_training_samples(model_name, training_samples)

            if len(testing_samples):
                api_response = api_instance.text_classifier_add_testing_samples(model_name, testing_samples)

            clsfr_algorithm = instance_detail.get('clsfr_algorithm')

            train_threshold = instance_detail.get('threshold')
            train_temperature = instance_detail.get('temperature')

            language_model_list_json = instance_detail.get('language_model_list')
            language_model_list = []

            for language_model_json in language_model_list_json:
                lang_code = language_model_json.get("lang_code")
                lang_model = language_model_json.get("lang_model")

                if lang_code is not None:
                    language_model_list.append(feersum_nlu.LabelledLanguageModel(lang_code, lang_model))

            train_details = feersum_nlu.TrainDetails(threshold=train_threshold,
                                                     temperature=train_temperature,
                                                     clsfr_algorithm=clsfr_algorithm,
                                                     language_model_list=language_model_list)

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

            training_samples = []
            testing_samples = []

            if training_samples_json:
                for sample in training_samples_json:
                    training_samples.append(feersum_nlu.LabelledTextSample(text=sample.get("text"),
                                                                           label=sample.get("label"),
                                                                           lang_code=sample.get("lang_code"),
                                                                           comment=sample.get("comment")))
            if testing_samples_json:
                for sample in testing_samples_json:
                    testing_samples.append(feersum_nlu.LabelledTextSample(text=sample.get("text"),
                                                                          label=sample.get("label"),
                                                                          lang_code=sample.get("lang_code"),
                                                                          comment=sample.get("comment")))

            if len(training_samples):
                api_response = api_instance.intent_classifier_add_training_samples(model_name, training_samples)

            if len(testing_samples):
                api_response = api_instance.intent_classifier_add_testing_samples(model_name, testing_samples)

            train_threshold = instance_detail.get('threshold')
            train_temperature = instance_detail.get('temperature')

            word_manifold_list_json = instance_detail.get('word_manifold_list')
            word_manifold_list = []

            for word_manifold_json in word_manifold_list_json:
                language = word_manifold_json.get("label")
                manifold = word_manifold_json.get("word_manifold")

                if language is not None:
                    word_manifold_list.append(feersum_nlu.LabelledWordManifold(language, manifold))

            train_details = feersum_nlu.TrainDetails(threshold=train_threshold,
                                                     temperature=train_temperature,
                                                     word_manifold_list=word_manifold_list)

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

            training_samples = []
            testing_samples = []

            if training_samples_json:
                for sample in training_samples_json:
                    training_samples.append(feersum_nlu.LabelledTextSample(text=sample.get("text"),
                                                                           label=sample.get("label"),
                                                                           lang_code=sample.get("lang_code"),
                                                                           comment=sample.get("comment")))
            if testing_samples_json:
                for sample in testing_samples_json:
                    testing_samples.append(feersum_nlu.LabelledTextSample(text=sample.get("text"),
                                                                          label=sample.get("label"),
                                                                          lang_code=sample.get("lang_code"),
                                                                          comment=sample.get("comment")))

            if len(training_samples):
                api_response = api_instance.faq_matcher_add_training_samples(model_name, training_samples)

            if len(testing_samples):
                api_response = api_instance.faq_matcher_add_testing_samples(model_name, testing_samples)

            train_threshold = instance_detail.get('threshold')
            train_temperature = instance_detail.get('temperature')

            word_manifold_list_json = instance_detail.get('word_manifold_list')
            word_manifold_list = []

            for word_manifold_json in word_manifold_list_json:
                language = word_manifold_json.get("label")
                manifold = word_manifold_json.get("word_manifold")

                if language is not None:
                    word_manifold_list.append(feersum_nlu.LabelledWordManifold(language, manifold))

            train_details = feersum_nlu.TrainDetails(threshold=train_threshold,
                                                     temperature=train_temperature,
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
        # elif model_type == 'person_name_entity_extractor':
        #     create_details = feersum_nlu.PersonNameEntityExtractorCreateDetails(name=model_name,
        #                                                                         desc=desc,
        #                                                                         long_name=long_name,
        #                                                                         load_from_store=False)
        #
        #     api_instance = feersum_nlu.PersonNameEntityExtractorsApi(feersum_nlu.ApiClient(configuration))
        #
        #     print("  Creating model ... ", flush=True)
        #     api_response = api_instance.person_name_entity_extractor_create(create_details)
        #
        #     print()
        #
        #     print("  Get the details of the imported model ... ", flush=True)
        #     api_response = api_instance.person_name_entity_extractor_get_details(model_name)
        #     print("   api_response", api_response)
        elif model_type == 'crf_entity_extractor':
            create_details = feersum_nlu.CrfEntityExtractorCreateDetails(name=model_name,
                                                                         desc=desc,
                                                                         long_name=long_name,
                                                                         load_from_store=False)

            api_instance = feersum_nlu.CrfEntityExtractorsApi(feersum_nlu.ApiClient(configuration))

            print("  Creating model ... ", flush=True)
            api_response = api_instance.crf_entity_extractor_create(create_details)

            training_samples = []
            testing_samples = []

            if training_samples_json:
                for sample in training_samples_json:
                    entity_list_json = sample.get("entity_list")
                    entity_list = []

                    for entity_json in entity_list_json:
                        entity_list.append(feersum_nlu.CrfEntity(entity=entity_json.get("entity"),
                                                                 index=entity_json.get("index"),
                                                                 len=entity_json.get("len")))

                    training_samples.append(feersum_nlu.CrfSample(text=sample.get("text"),
                                                                  intent=sample.get("intent"),
                                                                  entity_list=entity_list))

            if testing_samples_json:
                for sample in testing_samples_json:
                    entity_list_json = sample.get("entity_list")
                    entity_list = []

                    for entity_json in entity_list_json:
                        entity_list.append(feersum_nlu.CrfEntity(entity=entity_json.get("entity"),
                                                                 index=entity_json.get("index"),
                                                                 len=entity_json.get("len")))

                    testing_samples.append(feersum_nlu.CrfSample(text=sample.get("text"),
                                                                 intent=sample.get("intent"),
                                                                 entity_list=entity_list))

            if len(training_samples):
                api_response = api_instance.crf_entity_extractor_add_training_samples(model_name, training_samples)

            if len(testing_samples):
                api_response = api_instance.crf_entity_extractor_add_testing_samples(model_name, testing_samples)

            train_threshold = instance_detail.get('threshold')

            train_details = feersum_nlu.TrainDetails(threshold=train_threshold)

            print("  train_details =", str(train_details.to_dict()))

            print("  train_details =", str(train_details.to_dict()))

            print("  Training model ... ", flush=True)
            api_response = api_instance.crf_entity_extractor_train(model_name, train_details)

            print()

            print("  Get the details of the imported model ... ", flush=True)
            api_response = api_instance.crf_entity_extractor_get_details(model_name)
            print("   api_response", api_response)
        elif model_type == 'synonym_entity_extractor':
            create_details = feersum_nlu.SynonymEntityExtractorCreateDetails(name=model_name,
                                                                             desc=desc,
                                                                             long_name=long_name,
                                                                             load_from_store=False)

            api_instance = feersum_nlu.SynonymEntityExtractorsApi(feersum_nlu.ApiClient(configuration))

            print("  Creating model ... ", flush=True)
            api_response = api_instance.synonym_entity_extractor_create(create_details)

            training_samples = []
            testing_samples = []

            # 'text': 'str',
            # 'intent': 'str',
            # 'entity_list': 'list[SynonymEntity]'
            #     'entity': 'str',
            #     'syn_set': 'list[str]',
            #     'index': 'int',
            #     'len': 'int'

            if training_samples_json:
                for sample in training_samples_json:
                    entity_list_json = sample.get("entity_list")
                    entity_list = []

                    for entity_json in entity_list_json:
                        entity_list.append(feersum_nlu.SynonymEntity(entity=entity_json.get("entity"),
                                                                     syn_set=entity_json.get("syn_set"),
                                                                     index=entity_json.get("index"),
                                                                     len=entity_json.get("len")))

                    training_samples.append(feersum_nlu.SynonymSample(text=sample.get("text"),
                                                                      intent=sample.get("intent"),
                                                                      entity_list=entity_list))

            if testing_samples_json:
                for sample in testing_samples_json:
                    entity_list_json = sample.get("entity_list")
                    entity_list = []

                    for entity_json in entity_list_json:
                        entity_list.append(feersum_nlu.SynonymEntity(entity=entity_json.get("entity"),
                                                                     syn_set=entity_json.get("syn_set"),
                                                                     index=entity_json.get("index"),
                                                                     len=entity_json.get("len")))

                    testing_samples.append(feersum_nlu.SynonymSample(text=sample.get("text"),
                                                                     intent=sample.get("intent"),
                                                                     entity_list=entity_list))

            if len(training_samples):
                api_response = api_instance.synonym_entity_extractor_add_training_samples(model_name, training_samples)

            if len(testing_samples):
                api_response = api_instance.synonym_entity_extractor_add_testing_samples(model_name, testing_samples)

            train_threshold = instance_detail.get('threshold')

            train_details = feersum_nlu.TrainDetails(threshold=train_threshold)

            print("  train_details =", str(train_details.to_dict()))

            print("  train_details =", str(train_details.to_dict()))

            print("  Training model ... ", flush=True)
            api_response = api_instance.synonym_entity_extractor_train(model_name, train_details)

            print()

            print("  Get the details of the imported model ... ", flush=True)
            api_response = api_instance.synonym_entity_extractor_get_details(model_name)
            print("   api_response", api_response)

    except ApiException as e:
        print("Exception when calling an api endpoint: %s\n" % e)
    except urllib3.exceptions.HTTPError as e:
        print("Connection HTTPError! %s\n" % e)
