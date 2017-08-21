import urllib3

import feersum_nlu
from feersum_nlu.rest import ApiException

# Configure API key authorization: APIKeyHeader
feersum_nlu.configuration.api_key['AUTH_TOKEN'] = 'YOUR_API_KEY'
feersum_nlu.configuration.host = "http://127.0.0.1:8080/nlu/v2"

api_instance = feersum_nlu.TextClassifiersApi()

instance_name = 'test_txt_clsfr'

create_details = feersum_nlu.CreateDetails(name=instance_name, load_from_store=False)

# The training samples.
labelled_text_samples = []
labelled_text_samples.append(feersum_nlu.LabelledTextSamplesInner(text="I would like to fill in a claim form",
                                                                  label="claim"))
labelled_text_samples.append(feersum_nlu.LabelledTextSamplesInner(text="I would like to get a quote",
                                                                  label="quote"))

train_details = feersum_nlu.TrainDetails(immediate_mode=True)

text_input = feersum_nlu.TextInput("I would please like to fill in a claim form.")

try:
    # Create the text classifier.
    api_response = api_instance.text_classifier_create(create_details)
    print(api_response)

    # Add training samples to the text classifier.
    api_response = api_instance.text_classifier_add_training_samples(instance_name, labelled_text_samples)
    print(api_response)

    # Train the text classifier.
    api_response = api_instance.text_classifier_train(instance_name, train_details)
    print(api_response)

    # Get the details of all loaded text classifiers.
    api_response = api_instance.text_classifier_get_details_all()
    print(api_response)

    # Classify text.
    api_response = api_instance.text_classifier_retrieve(instance_name, text_input)
    print(api_response)
except ApiException as e:
    print("Exception when calling DateParsersApi->date_parser_retrieve: %s\n" % e)
except urllib3.exceptions.MaxRetryError:
    print("Connection MaxRetryError!")

