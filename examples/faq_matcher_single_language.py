""" Example: Shows how to create, train and use an FAQ matcher. """

import urllib3
import time

import feersum_nlu
from feersum_nlu.rest import ApiException
from examples import feersumnlu_host, feersum_nlu_auth_token

# Configure API key authorization: APIKeyHeader
configuration = feersum_nlu.Configuration()

# configuration.api_key['AUTH_TOKEN'] = feersum_nlu_auth_token
configuration.api_key['X-Auth-Token'] = feersum_nlu_auth_token  # Alternative auth key header!

configuration.host = feersumnlu_host

api_instance = feersum_nlu.FaqMatchersApi(feersum_nlu.ApiClient(configuration))

instance_name = 'test_faq_mtchr'

create_details = feersum_nlu.FaqMatcherCreateDetails(name=instance_name,
                                                     desc="Test FAQ matcher.",
                                                     long_name="Loong Name",
                                                     lid_model_file="lid_za",
                                                     load_from_store=False)

# The training samples.
labelled_text_sample_list = []
labelled_text_sample_list.append(feersum_nlu.LabelledTextSample(text="How claim?",
                                                                label="claim",
                                                                lang_code="eng"))

labelled_text_sample_list.append(feersum_nlu.LabelledTextSample(text="How quote?",
                                                                label="quote"))

labelled_text_sample_delete_list = []
labelled_text_sample_delete_list.append(feersum_nlu.LabelledTextSample(text="Hoe eis?",
                                                                       label="claim",
                                                                       lang_code="afr"))

labelled_text_sample_testing_list = []
labelled_text_sample_testing_list.append(feersum_nlu.LabelledTextSample(text="Where do I claim?",
                                                                        label="claim",
                                                                        lang_code="eng"))

labelled_text_sample_testing_list.append(feersum_nlu.LabelledTextSample(text="Can I put in a claim?",
                                                                        label="quote"))  # text actually on 'claim'.

# word_manifold_list = [feersum_nlu.LabelledWordManifold('eng', 'feers_wm_eng'),
#                       feersum_nlu.LabelledWordManifold('afr', 'feers_wm_afr'),
#                       feersum_nlu.LabelledWordManifold('zul', 'feers_wm_zul')]
word_manifold_list = [feersum_nlu.LabelledWordManifold('eng', 'glove6B50D_trimmed')]
# The playground's pre-loaded embeddings include:
# "feers_wm_afr", "feers_wm_eng", "feers_wm_nbl", "feers_wm_xho",
# "feers_wm_zul", "feers_wm_ssw", "feers_wm_nso", "feers_wm_sot",
# "feers_wm_tsn", "feers_wm_ven", "feers_wm_tso"
# and "glove6B50D_trimmed"

train_details = feersum_nlu.TrainDetails(threshold=0.95,
                                         word_manifold_list=word_manifold_list)

text_input = feersum_nlu.TextInput("Where do I claim?")

print()

try:
    print("Create the FAQ matcher:")
    api_response = api_instance.faq_matcher_create(create_details)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Add training samples to the FAQ matcher:")
    api_response = api_instance.faq_matcher_add_training_samples(instance_name, labelled_text_sample_list)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the training samples of the FAQ matcher:")
    api_response = api_instance.faq_matcher_get_training_samples(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Del training samples of the FAQ matcher:")
    # api_response = api_instance.faq_matcher_del_training_samples_all(instance_name)
    api_response = \
        api_instance.faq_matcher_del_training_samples(instance_name,
                                                      labelled_text_sample_list=labelled_text_sample_delete_list)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the reduced training samples of the FAQ matcher:")
    api_response = api_instance.faq_matcher_get_training_samples(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Add all the training samples back to the FAQ matcher:")
    api_response = api_instance.faq_matcher_add_training_samples(instance_name, labelled_text_sample_list)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Add testing samples to the FAQ matcher:")
    api_response = api_instance.faq_matcher_add_testing_samples(instance_name, labelled_text_sample_testing_list)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    # print("Del testing samples of the FAQ matcher:")
    # api_response = api_instance.faq_matcher_del_testing_samples_all(instance_name)
    # # api_response = api_instance.faq_matcher_del_testing_samples(instance_name,
    # #                                                             labelled_text_sample_list=
    # #                                                             labelled_text_sample_testing_list)
    # print(" type(api_response)", type(api_response))
    # print(" api_response", api_response)
    # print()

    print("Train the FAQ matcher:")
    api_response = api_instance.faq_matcher_train(instance_name, train_details)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Waiting for training...", flush=True)
    time.sleep(20.0)

    # print("Get the details of all loaded FAQ matcher:")
    # api_response = api_instance.faq_matcher_get_details_all()
    # print(" type(api_response)", type(api_response))
    # print(" api_response", api_response)
    # print()

    print("Get the details of specific named loaded FAQ matcher:")
    api_response = api_instance.faq_matcher_get_details(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    cm_labels = api_response.cm_labels
    print()

    # Get the classifier's possible labels. Might be inferred from the training data, but guaranteed to be available
    # after training.
    print("Get the labels of named loaded FAQ matcher:")
    api_response = api_instance.faq_matcher_get_labels(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("From the model details the cm_labels where =", cm_labels)
    print(cm_labels)
    print()

    print("Get some curate details of training matrix of specific named loaded FAQ matcher:")
    # Use the same labels as returned in the confusion matrix.
    label_pair = feersum_nlu.ClassLabelPair(matrix_name='train', true_label='0', predicted_label='0')
    api_response = api_instance.faq_matcher_curate(instance_name, label_pair)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get some curate details of the testing matrix of specific named loaded FAQ matcher:")
    print(" > Look at cell (1,0) which turns out to have been a claim sample incorrectly labelled as quote.")
    # Use the same labels as returned in the confusion matrix.
    label_pair = feersum_nlu.ClassLabelPair(matrix_name='test', true_label='1', predicted_label='0')
    api_response = api_instance.faq_matcher_curate(instance_name, label_pair)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Match a question:")
    api_response = api_instance.faq_matcher_retrieve(instance_name, text_input)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Update the parameters:")
    model_params = feersum_nlu.ModelParams(threshold=0.9, desc="Examples: Test FAQ matcher.", long_name="Loooong name.")
    api_response = api_instance.faq_matcher_set_params(instance_name, model_params)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Match a question:")
    api_response = api_instance.faq_matcher_retrieve(instance_name, text_input)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Delete specific named loaded FAQ matcher:")
    api_response = api_instance.faq_matcher_del(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Vaporise specific named loaded FAQ matcher:")
    api_response = api_instance.faq_matcher_vaporise(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

except ApiException as e:
    print("Exception when calling an FAQ matcher operation: %s\n" % e)
except urllib3.exceptions.HTTPError as e:
    print("Connection HTTPError! %s\n" % e)
