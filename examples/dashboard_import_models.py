"""
Example: Shows how to import a model using feersum_nlu_utils. The file formats is defined in the export example.
A model's json object was split into three separate files for instance_detail, training and testing data during export.
These files are combined into on json object used by feersum_nlu_util's import function.
"""

import json

import feersum_nlu
from examples import feersumnlu_host, feersum_nlu_auth_token

from feersum_nlu_util.transfer import import_model


def main():
    configuration = feersum_nlu.Configuration()
    configuration.api_key['X-Auth-Token'] = feersum_nlu_auth_token
    configuration.host = feersumnlu_host

    # Select the source auth token. Default is same as config/destination token, but it can be different.
    src_feersum_nlu_auth_token = feersum_nlu_auth_token
    # src_feersum_nlu_auth_token = "63454b82-ee34-4e26-9a63-6b1d4f51db49"

    model_list = [
        ("emergencies_category", "text_classifier"),
        ("figure_out_category", "text_classifier"),
        ("it_category", "text_classifier"),
        ("userhappy", "text_classifier"),
    ]  # List of exported models to be imported [(mdl,type), ...]

    # === Import models one by one ===
    for model_name, model_type in model_list:
        print("\n#####################")

        filename_model = f"exported_models/{model_name}_{src_feersum_nlu_auth_token}.{model_type}.json"

        print('filename_model =', filename_model, flush=True)

        print()
        print("model_name =", model_name)
        print("model_type =", model_type)
        print()

        # Open the instance detail json file and then try and load training and testing data CSVs.
        with open(filename_model) as json_file:
            instance_detail = json.load(json_file)
            print("  instance_detail = ", instance_detail)

            src_model_type = instance_detail.get("model_type", None)

            if src_model_type != model_type:
                print("INFO: Source model type is different from type to be imported!!!")

            # === Try to get training samples from training data CSV ===
            training_samples = instance_detail.get("training_samples")

            print("  training_samples = ", len(training_samples) if training_samples is not None else 0)

            # === Try to get testing samples from testing data CSV ===
            testing_samples = instance_detail.get("testing_samples")

            print("  testing_samples = ", len(testing_samples) if testing_samples is not None else 0)

            # === Make model dict ===
            model_dict = {"instance_detail": instance_detail,
                          "training_samples": training_samples,
                          "testing_samples": testing_samples}

            # =================================
            # === FEERSUM_NLU_UTIL's import ===
            import_model(model_name, model_type, configuration, model_dict)
            # =================================


if __name__ == '__main__':  # pragma: no cover
    main()
