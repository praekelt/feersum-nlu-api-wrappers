"""
Example: Shows how to export models using feersum_nlu_util. The model's json object received from the export function is
split into three separate files for instance_details, training and testing data.
"""

import json
import urllib3
import csv

import feersum_nlu
from feersum_nlu.rest import ApiException
from examples import feersumnlu_host, feersum_nlu_auth_token

from feersum_nlu_util.transfer import export_model


def main():
    configuration = feersum_nlu.Configuration()
    configuration.api_key['X-Auth-Token'] = feersum_nlu_auth_token  # Alternative auth key header!
    configuration.host = feersumnlu_host

    dash_api_instance = feersum_nlu.DashboardApi(feersum_nlu.ApiClient(configuration))

    print()

    try:
        print("Saving ALL dashboard models to disk...", end='', flush=True)
        detail = dash_api_instance.dashboard_nlu_get_details()  # type: feersum_nlu.models.dashboard_detail.DashboardDetail

        print(" type(api_response)", type(detail))
        print(" api_response", detail)
        print()

        for model in detail.model_list:
            print(".", end='', flush=True)

            if not model.trashed and model.name != "":
                # =================================
                # === FEERSUM_NLU_UTIL's export ===
                model_dict = export_model(model.name, model.model_type, configuration)
                # =================================

                instance_detail = model_dict.get("instance_detail")

                # Write export to file if model supported export.
                if instance_detail is not None:
                    # Add the model type which may be used for type checking on import.
                    training_samples = model_dict.get("training_samples")
                    testing_samples = model_dict.get("testing_samples")
                    samples = model_dict.get("samples")

                    training_samples_json = []
                    testing_samples_json = []
                    samples_json = []

                    # Convert samples to JSON-serialisable dicts.
                    if training_samples is not None:
                        for sample in training_samples:
                            training_samples_json.append(sample.to_dict())

                    if testing_samples is not None:
                        for sample in testing_samples:
                            testing_samples_json.append(sample.to_dict())

                    if samples is not None:
                        for sample in samples:
                            samples_json.append(sample.to_dict())

                    # Add the model type and training+testing data to the instance detail
                    instance_detail["model_type"] = model.model_type

                    if len(training_samples_json):
                        instance_detail["training_samples"] = training_samples_json

                    if len(testing_samples_json):
                        instance_detail["testing_samples"] = testing_samples_json

                    if len(samples_json):
                        instance_detail["samples"] = samples_json

                    instance_detail_filename = f"exported_models/{model.name}_{feersum_nlu_auth_token}.{model.model_type}"

                    # Write .json files.
                    with open(instance_detail_filename + ".json", "w") as json_file:
                        json.dump(instance_detail, json_file, sort_keys=True, indent=4)

                    if model.model_type in ['text_classifier',
                                            'intent_classifier',
                                            'faq_matcher',
                                            'crf_entity_extractor'
                                            'synonym_entity_extractor']:
                        # Also write the classifiers' training samples to .csv
                        if training_samples is not None:
                            with open(instance_detail_filename + ".train.csv", "w", newline='') as csv_file:
                                csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                                for sample in training_samples:
                                    # print('(', sample.label, ',', sample.text, ')')
                                    csv_writer.writerow([sample.label, sample.text])

                        # Also write the classifiers' testing samples to .csv
                        if testing_samples is not None:
                            with open(instance_detail_filename + ".test.csv", "w", newline='') as csv_file:
                                csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                                for sample in testing_samples:
                                    # print('(', sample.label, ',', sample.text, ')')
                                    csv_writer.writerow([sample.label, sample.text])

                    elif model.model_type in ['image_classifier']:
                        # Also write the classifiers' training samples to .csv
                        if training_samples is not None:
                            with open(instance_detail_filename + ".train.csv", "w", newline='') as csv_file:
                                csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                                for sample in training_samples:
                                    # print('(', sample.label, ',', sample.image, ')')
                                    csv_writer.writerow([sample.label, sample.image])

                        # Also write the classifiers' testing samples to .csv
                        if testing_samples is not None:
                            with open(instance_detail_filename + ".test.csv", "w", newline='') as csv_file:
                                csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                                for sample in testing_samples:
                                    # print('(', sample.label, ',', sample.image, ')')
                                    csv_writer.writerow([sample.label, sample.image])

                    elif model.model_type in ['text_dataset']:
                        # Also write the datasets' samples to .csv
                        if samples is not None:
                            with open(instance_detail_filename + ".samples.csv", "w", newline='') as csv_file:
                                csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                                for sample in samples:
                                    # print('(', sample.label, ',', sample.text, ')')
                                    csv_writer.writerow([sample.label, sample.text])

                    elif model.model_type in ['image_dataset']:
                        # Also write the datasets' samples to .csv
                        if samples is not None:
                            with open(instance_detail_filename + ".samples.csv", "w", newline='') as csv_file:
                                csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                                for sample in samples:
                                    # print('(', sample.label, ',', sample.image, ')')
                                    csv_writer.writerow([sample.label, sample.image])

        print(' done.', flush=True)

    except ApiException as e:
        print("Exception when calling an api endpoint: %s\n" % e)
    except urllib3.exceptions.HTTPError as e:
        print("Connection HTTPError! %s\n" % e)


if __name__ == '__main__':  # pragma: no cover
    main()
