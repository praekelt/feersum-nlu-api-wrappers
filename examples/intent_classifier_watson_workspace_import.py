""" Example: Shows how to create, train and use an intent classifier from a Watson workspace export. """

import urllib3
from typing import List
import json

import feersum_nlu
from feersum_nlu.rest import ApiException
from examples import feersumnlu_host, feersum_nlu_auth_token


def import_watson_workspace_intents(filename: str) -> List[feersum_nlu.LabelledTextSample]:
    labelled_text_sample_list = []  # type: List[feersum_nlu.LabelledTextSample]

    with open(filename) as json_file:
        workspace = json.load(json_file)

        print(f"Workspace name = {workspace.get('name')}")

        intents = workspace.get('intents')
        # print(json.dumps(intents, indent=4))

        if intents is not None:
            for intent in intents:
                label = intent.get('intent')
                utterance_examples = intent.get('examples')

                if label is not None and utterance_examples is not None:
                    for utterance_example in utterance_examples:
                        text = utterance_example.get('text')
                        labelled_text_sample_list.append(feersum_nlu.LabelledTextSample(text=text, label=label))

    return labelled_text_sample_list


# Configure API key authorization: APIKeyHeader
configuration = feersum_nlu.Configuration()

# configuration.api_key['AUTH_TOKEN'] = feersum_nlu_auth_token
configuration.api_key['X-Auth-Token'] = feersum_nlu_auth_token  # Alternative auth key header!

configuration.host = feersumnlu_host

api_instance = feersum_nlu.IntentClassifiersApi(feersum_nlu.ApiClient(configuration))

instance_name = 'tumi_intent_clsfr'

word_manifold_list = [feersum_nlu.LabelledWordManifold('eng', 'feers_wm_eng')]
# The playground's pre-loaded embeddings include:
# "feers_wm_afr", "feers_wm_eng", "feers_wm_nbl", "feers_wm_xho",
# "feers_wm_zul", "feers_wm_ssw", "feers_wm_nso", "feers_wm_sot",
# "feers_wm_tsn", "feers_wm_ven", "feers_wm_tso"
# and "glove6B50D_trimmed"

create_details = feersum_nlu.IntentClassifierCreateDetails(name=instance_name,
                                                           desc="TUMI intent classifier.",
                                                           long_name=instance_name,
                                                           lid_model_file="lid_za",
                                                           load_from_store=False)

# The training samples.
# labelled_text_sample_list = []
# labelled_text_sample_list.append(feersum_nlu.LabelledTextSample(text="I would like to fill in a claim form.",
#                                                                 label="claim"))

labelled_text_sample_list = \
    import_watson_workspace_intents("data/watson-workspace-export-for-44a4bcc9-1fca-4580-aa6e-d683a2357e8a.json")


# train_details = feersum_nlu.TrainDetails(immediate_mode=True)
train_details = feersum_nlu.TrainDetails(threshold=1.0,
                                         word_manifold_list=word_manifold_list,
                                         immediate_mode=True)

text_input = feersum_nlu.TextInput("I was charged for a movie but it isn't available to watch, what must I do?")

print()

try:
    print("Create the intent classifier:")
    api_response = api_instance.intent_classifier_create(create_details)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Add training samples to the intent classifier:")
    api_response = api_instance.intent_classifier_add_training_samples(instance_name, labelled_text_sample_list)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the training samples of the intent classifier:")
    api_response = api_instance.intent_classifier_get_training_samples(instance_name)
    # print(" type(api_response)", type(api_response))
    # print(" api_response", api_response)
    print()

    print("Train the intent classifier:")
    api_response = api_instance.intent_classifier_train(instance_name, train_details)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the details of all loaded intent classifiers:")
    api_response = api_instance.intent_classifier_get_details_all()
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the details of specific named loaded intent classifiers:")
    api_response = api_instance.intent_classifier_get_details(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    # Get the classifier's possible labels. Might be inferred from the training data, but guaranteed to be available
    # after training.
    print("Get the labels of named loaded intent classifiers:")
    api_response = api_instance.intent_classifier_get_labels(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the model params:")
    api_response = api_instance.intent_classifier_get_params(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Classify intent:")
    api_response = api_instance.intent_classifier_retrieve(instance_name, text_input)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    # print("Delete specific named loaded intent classifiers:")
    # api_response = api_instance.intent_classifier_del(instance_name)
    # print(" type(api_response)", type(api_response))
    # print(" api_response", api_response)
    # print()

    # print("Vaporise specific named loaded intent classifiers:")
    # api_response = api_instance.intent_classifier_vaporise(instance_name)
    # print(" type(api_response)", type(api_response))
    # print(" api_response", api_response)
    # print()

except ApiException as e:
    print("Exception when calling an intent classifier operation: %s\n" % e)
except urllib3.exceptions.HTTPError as e:
    print("Connection HTTPError! %s\n" % e)
