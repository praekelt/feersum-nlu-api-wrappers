""" Example: Shows how to create, train and use a image classifier. """

import urllib3
import base64

import feersum_nlu
from feersum_nlu.rest import ApiException
from examples import feersumnlu_host, feersum_nlu_auth_token

from feersum_nlu_util import image_utils

# Configure API key authorization: APIKeyHeader
configuration = feersum_nlu.Configuration()

# configuration.api_key['AUTH_TOKEN'] = feersum_nlu_auth_token
configuration.api_key['X-Auth-Token'] = feersum_nlu_auth_token  # Alternative auth key header!

configuration.host = feersumnlu_host

api_instance = feersum_nlu.ImageClassifiersApi(feersum_nlu.ApiClient(configuration))

instance_name = 'image_txt_clsfr'

create_details = feersum_nlu.ImageClassifierCreateDetails(name=instance_name,
                                                          desc="Test image classifier.",
                                                          load_from_store=False)

# The training samples.
labelled_image_sample_list = []

labelled_image_sample_list.append(feersum_nlu.LabelledImageSample(
    image=base64.b64encode(b"I would like to fill in a claim form").decode('utf-8'),
    label="claim"))
labelled_image_sample_list.append(feersum_nlu.LabelledImageSample(
    image=base64.b64encode(b"I had an accident?").decode('utf-8'),
    label="claim"))
labelled_image_sample_list.append(feersum_nlu.LabelledImageSample(
    image=base64.b64encode(b"My wheel was damaged?").decode('utf-8'),
    label="claim"))

labelled_image_sample_list.append(feersum_nlu.LabelledImageSample(
    image=base64.b64encode(b"I would like to get a quote").decode('utf-8'),
    label="quote"))
labelled_image_sample_list.append(feersum_nlu.LabelledImageSample(
    image=base64.b64encode(b"Is it expensive?").decode('utf-8'),
    label="quote"))
labelled_image_sample_list.append(feersum_nlu.LabelledImageSample(
    image=base64.b64encode(b"How much does it cost?").decode('utf-8'),
    label="quote"))

train_details = feersum_nlu.TrainDetails(immediate_mode=True  # ,
                                         # clsfr_algorithm="naive_bayes",
                                         # language_model_list=[
                                         #     {
                                         #         "lang_code": "eng",
                                         #         "lang_model": "glove6B50D_trimmed"
                                         #     }
                                         # ]
                                         )


# image_utils.show_image("/Users/bduvenhage/Desktop/1500x500.jpg")
image_string = image_utils.load_image(file_name="/Users/bduvenhage/Desktop/1500x500.jpg")
# image_utils.save_image(file_name="/Users/bduvenhage/Desktop/1500x500_.png", base64_string=image_string)
image_input = feersum_nlu.ImageInput(image_string)


caller_name = 'example_caller'

print()

try:
    #    print("Update the model params:")
    #    model_params = feersum_nlu.ModelParams(readonly=False)
    #    api_response = api_instance.image_classifier_set_params(instance_name, model_params, x_caller=caller_name)
    #    print(" type(api_response)", type(api_response))
    #    print(" api_response", api_response)
    #    print()

    print("Create the image classifier:")
    api_response = api_instance.image_classifier_create(create_details)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Add training samples to the image classifier:")
    api_response = api_instance.image_classifier_add_training_samples(instance_name, labelled_image_sample_list)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the training samples of the image classifier:")
    api_response = api_instance.image_classifier_get_training_samples(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Del the training samples of the image classifier:")
    api_response = api_instance.image_classifier_del_training_samples_all(instance_name)
    # api_response = api_instance.image_classifier_del_training_samples(instance_name,
    #                                                              labelled_image_sample_list=
    #                                                              labelled_image_sample_delete_list)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Add training samples to the image classifier:")
    api_response = api_instance.image_classifier_add_training_samples(instance_name, labelled_image_sample_list)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Del testing samples of the image classifier:")
    api_response = api_instance.image_classifier_del_testing_samples_all(instance_name)
    # api_response = api_instance.image_classifier_del_testing_samples(instance_name,
    #                                                             labelled_image_sample_list=
    #                                                             labelled_image_sample_testing_list)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Train the image classifier:")
    api_response = api_instance.image_classifier_train(instance_name, train_details)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the details of all loaded image classifiers:")
    api_response = api_instance.image_classifier_get_details_all()
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the details of specific named loaded image classifiers:")
    api_response = api_instance.image_classifier_get_details(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    # Get the classifier's possible labels. Might be inferred from the training data, but guaranteed to be available
    # after training.
    print("Get the labels of named loaded image classifiers:")
    api_response = api_instance.image_classifier_get_labels(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get some curate details of specific named loaded image classifier:")
    # Use the same labels as returned in the confusion matrix.
    label_pair = feersum_nlu.ClassLabelPair(matrix_name='train', true_label='claim', predicted_label='claim')
    api_response = api_instance.image_classifier_curate(instance_name, label_pair)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Classify image:")
    api_response = api_instance.image_classifier_retrieve(instance_name, image_input, x_caller=caller_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the model params:")
    api_response = api_instance.image_classifier_get_params(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Update the model params:")
    model_params = feersum_nlu.ModelParams(threshold=0.9, desc="Examples: Test image classifier.",
                                           long_name='Test image Classifier',
                                           readonly=True)
    api_response = api_instance.image_classifier_set_params(instance_name, model_params)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the details of specific named loaded image classifiers:")
    api_response = api_instance.image_classifier_get_details(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Delete named loaded image classifier:")
    api_response = api_instance.image_classifier_del(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Vaporise named loaded image classifier:")
    api_response = api_instance.image_classifier_vaporise(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()
except ApiException as e:
    print("Exception when calling a image classifier operation: %s\n" % e)
except urllib3.exceptions.HTTPError as e:
    print("Connection HTTPError! %s\n" % e)
