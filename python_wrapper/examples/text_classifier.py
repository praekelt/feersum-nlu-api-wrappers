import urllib3

import feersum_nlu
from feersum_nlu.rest import ApiException

# Configure API key authorization: APIKeyHeader
feersum_nlu.configuration.api_key['AUTH_TOKEN'] = 'YOUR_API_KEY'

# feersum_nlu.configuration.host = "http://127.0.0.1:8100/nlu/v2"
feersum_nlu.configuration.host = "http://nlu.playground.feersum.io:8100/nlu/v2"

api_instance = feersum_nlu.TextClassifiersApi()

instance_name = 'test_txt_clsfr'

create_details = feersum_nlu.CreateDetails(name=instance_name, desc="Test text classifier.", load_from_store=False)

# The training samples.
labelled_text_sample_list = []
labelled_text_sample_list.append(feersum_nlu.LabelledTextSample(text="I would like to fill in a claim form",
                                                            label="claim"))
labelled_text_sample_list.append(feersum_nlu.LabelledTextSample(text="I would like to get a quote",
                                                            label="quote"))

train_details = feersum_nlu.TrainDetails(immediate_mode=True)

text_input = feersum_nlu.TextInput("I would please like to fill in a claim form.")

print()

try:
    print("Create the text classifier:")
    api_response = api_instance.text_classifier_create(create_details)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Add training samples to the text classifier:")
    api_response = api_instance.text_classifier_add_training_samples(instance_name, labelled_text_sample_list)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the training samples of the text classifier:")
    api_response = api_instance.text_classifier_get_training_samples(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Del the training samples of the text classifier:")
    api_response = api_instance.text_classifier_del_training_samples(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Add training samples to the text classifier:")
    api_response = api_instance.text_classifier_add_training_samples(instance_name, labelled_text_sample_list)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Train the text classifier:")
    api_response = api_instance.text_classifier_train(instance_name, train_details)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the details of all loaded text classifiers:")
    api_response = api_instance.text_classifier_get_details_all()
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the details of specific named loaded text classifiers:")
    api_response = api_instance.text_classifier_get_details(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Classify text:")
    api_response = api_instance.text_classifier_retrieve(instance_name, text_input)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()
except ApiException as e:
    print("Exception when calling a text classifier operation: %s\n" % e)
except urllib3.exceptions.MaxRetryError:
    print("Connection MaxRetryError!")
