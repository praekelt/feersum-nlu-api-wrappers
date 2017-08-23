import urllib3

import feersum_nlu
from feersum_nlu.rest import ApiException

# Configure API key authorization: APIKeyHeader
feersum_nlu.configuration.api_key['AUTH_TOKEN'] = 'YOUR_API_KEY'

feersum_nlu.configuration.host = "http://127.0.0.1:8000/nlu/v2"
# feersum_nlu.configuration.host = "http://dev-bernardt.za.prk.hosting:8000/nlu/v2"


# === Word manifold to use ===
print("Create the word manifold model:")
wm_api_instance = feersum_nlu.WordManifoldsApi()
wm_instance_name = 'test_wm'
# wm_create_details = feersum_nlu.CreateDetails(name=wm_instance_name, desc="Test word manifold.",
#                                               load_from_store=False, input_file="glove.6B.200d.txt")
wm_create_details = feersum_nlu.CreateDetails(name=wm_instance_name, load_from_store=True)
wm_api_response = wm_api_instance.word_manifold_create(wm_create_details)
print(" type(wm_api_response)", type(wm_api_response))
print(" wm_api_response", wm_api_response)
print()
# === ===


api_instance = feersum_nlu.IntentClassifiersApi()

instance_name = 'test_intent_clsfr'

create_details = feersum_nlu.CreateDetails(name=instance_name, desc="Test intent classifier.", load_from_store=False)

# The training samples.
labelled_text_samples = []
labelled_text_samples.append(feersum_nlu.LabelledTextSamplesInner(text="I would like to fill in a claim form",
                                                                  label="claim"))
labelled_text_samples.append(feersum_nlu.LabelledTextSamplesInner(text="I would like to get a quote",
                                                                  label="quote"))

# train_details = feersum_nlu.TrainDetails(immediate_mode=True)
train_details = feersum_nlu.TrainDetails(immediate_mode=True, word_manifold=wm_instance_name)

text_input = feersum_nlu.TextInput("How do I get a quote")


print()

try:
    print("Create the intent classifier:")
    api_response = api_instance.intent_classifier_create(create_details)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Add training samples to the intent classifier:")
    api_response = api_instance.intent_classifier_add_training_samples(instance_name, labelled_text_samples)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the training samples of the intent classifier:")
    api_response = api_instance.intent_classifier_get_training_samples(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Del the training samples of the intent classifier:")
    api_response = api_instance.intent_classifier_del_training_samples(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Add training samples to the intent classifier:")
    api_response = api_instance.intent_classifier_add_training_samples(instance_name, labelled_text_samples)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
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

    print("Classify intent:")
    api_response = api_instance.intent_classifier_retrieve(instance_name, text_input)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()
except ApiException as e:
    print("Exception when calling an intent classifier operation: %s\n" % e)
except urllib3.exceptions.MaxRetryError:
    print("Connection MaxRetryError!")

