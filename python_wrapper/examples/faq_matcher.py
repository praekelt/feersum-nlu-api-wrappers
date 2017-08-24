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


api_instance = feersum_nlu.FaqMatchersApi()

instance_name = 'test_faq_mtchr'

create_details = feersum_nlu.CreateDetails(name=instance_name, desc="Test FAQ matcher.", load_from_store=False)

# The training samples.
labelled_text_samples = []
labelled_text_samples.append(feersum_nlu.LabelledTextSamplesInner(text="How do I claim?",
                                                                  label="claim"))
labelled_text_samples.append(feersum_nlu.LabelledTextSamplesInner(text="How do I get a quote?",
                                                                  label="quote"))

# train_details = feersum_nlu.TrainDetails(immediate_mode=True)
train_details = feersum_nlu.TrainDetails(immediate_mode=True, word_manifold=wm_instance_name)

text_input = feersum_nlu.TextInput("How do I put in claim?")


print()

try:
    print("Create the FAQ matcher:")
    api_response = api_instance.faq_matcher_create(create_details)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Add training samples to the FAQ matcher:")
    api_response = api_instance.faq_matcher_add_training_samples(instance_name, labelled_text_samples)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the training samples of the FAQ matcher:")
    api_response = api_instance.faq_matcher_get_training_samples(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Del the training samples of the FAQ matcher:")
    api_response = api_instance.faq_matcher_del_training_samples(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Add training samples to the FAQ matcher:")
    api_response = api_instance.faq_matcher_add_training_samples(instance_name, labelled_text_samples)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Train the FAQ matcher:")
    api_response = api_instance.faq_matcher_train(instance_name, train_details)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the details of all loaded FAQ matcher:")
    api_response = api_instance.faq_matcher_get_details_all()
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the details of specific named loaded FAQ matcher:")
    api_response = api_instance.faq_matcher_get_details(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Match a question:")
    api_response = api_instance.faq_matcher_retrieve(instance_name, text_input)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()
except ApiException as e:
    print("Exception when calling an FAQ matcher operation: %s\n" % e)
except urllib3.exceptions.MaxRetryError:
    print("Connection MaxRetryError!")

