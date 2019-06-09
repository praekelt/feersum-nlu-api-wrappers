""" Example: Shows how to create, train and use a image classifier. """

import urllib3
import time

from typing import List, Tuple

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

# instance_name = 'hot_dog_vs_not_hot_dog_image_clsfr'
# train_data_path = "/Users/bduvenhage/Downloads/vision_data/hot-dog-vs-not-hot-dog/train"
# test_data_path = "/Users/bduvenhage/Downloads/vision_data/hot-dog-vs-not-hot-dog/test"
# labels = ["hot_dog", "not_hot_dog"]


instance_name = 'cat_vs_dog_image_clsfr'
train_data_path = "/Users/bduvenhage/myWork/dev/Praekelt/feersum-nlu-sdk_develop/feersum_nlu/nlp_engine_data/vision/" + \
                  "cats-vs-dogs/train"
test_data_path = "/Users/bduvenhage/myWork/dev/Praekelt/feersum-nlu-sdk_develop/feersum_nlu/nlp_engine_data/vision/" + \
                  "cats-vs-dogs/test"
labels = ["cat", "dog"]


# === Load the data samples ===
#   Assumes data in folder structure like - ..../train/dog OR ..../train/cat OR ..../test/dog etc.
training_list = []  # type: List[Tuple[str, str]]
for label in labels:
    label_samples = image_utils.get_image_samples(train_data_path, label)
    label_samples = label_samples[:min(len(label_samples), 50)]  # limit number of samples per class.
    training_list.extend(label_samples)

testing_list = []  # type: List[Tuple[str, str]]
for label in labels:
    label_samples = image_utils.get_image_samples(test_data_path, label)
    label_samples = label_samples[:min(len(label_samples), 50)]  # limit number of samples per class.
    testing_list.extend(label_samples)

training_samples = [feersum_nlu.LabelledImageSample(image=image, label=label) for image, label in training_list]
testing_samples = [feersum_nlu.LabelledImageSample(image=image, label=label) for image, label in testing_list]
# === ===


create_details = feersum_nlu.ImageClassifierCreateDetails(name=instance_name,
                                                          desc=instance_name,
                                                          load_from_store=False)


train_details = feersum_nlu.TrainDetails(immediate_mode=True,
                                         clsfr_algorithm="resnet152")

# image_utils.show_image("/Users/bduvenhage/Desktop/1500x500.jpg")
# image_string = image_utils.load_image(file_name="/Users/bduvenhage/Desktop/1500x500.jpg")
# image_utils.save_image(file_name="/Users/bduvenhage/Desktop/1500x500_.png", base64_string=image_string)

image_input = feersum_nlu.ImageInput(testing_samples[0].image)


caller_name = 'example_caller'

print()

try:
    # print("Update the model params:")
    # model_params = feersum_nlu.ModelParams(readonly=False)
    # api_response = api_instance.image_classifier_set_params(instance_name, model_params, x_caller=caller_name)
    # print(" type(api_response)", type(api_response))
    # print(" api_response", api_response)
    # print()

    print("Create the image classifier:")
    api_response = api_instance.image_classifier_create(create_details)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Add training samples to the image classifier:")
    for training_sample in training_samples:
        api_response = api_instance.image_classifier_add_training_samples(instance_name, [training_sample])
        print(" type(api_response)", type(api_response))
        print(" api_response", api_response)
    print()

    print("Add testing samples to the image classifier:")
    for testing_sample in testing_samples:
        api_response = api_instance.image_classifier_add_testing_samples(instance_name, [testing_sample])
        print(" type(api_response)", type(api_response))
        print(" api_response", api_response)
    print()

    print("Train the image classifier:")
    instance_detail = api_instance.image_classifier_train(instance_name, train_details)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    # TRAINING:
    # If timestamp begins with 'ASYNC...' the the training is running in the background and you need to poll until the
    # model ID has updated.
    # if timestamp doesn't begin with ASYNC then the training has completed synchronously and you may continue.
    # In the near future webhooks will be supported to let you know when async training has finished.

    if instance_detail.training_stamp.startswith('ASYNC'):
        # Background training in progress. We'll poll and wait for it to complete.
        print("Background training in progress...", flush=True, end='')
        previous_id = instance_detail.id

        while True:
            print('.', end='', flush=True)
            time.sleep(1)
            inst_det = api_instance.image_classifier_get_details(instance_name)
            if inst_det.id != previous_id:
                # ToDo: Stop if details indicate that training failed.
                break  # break from while-loop when ID updated which indicates training done.

        print('Done.')
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

    # print("Get some curate details of specific named loaded image classifier:")
    # # Use the same labels as returned in the confusion matrix.
    # label_pair = feersum_nlu.ClassLabelPair(matrix_name='train', true_label='cat', predicted_label='dog')
    # api_response = api_instance.image_classifier_curate(instance_name, label_pair)
    # print(" type(api_response)", type(api_response))
    # print(" api_response", api_response)
    # print()

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

    # print("Delete named loaded image classifier:")
    # api_response = api_instance.image_classifier_del(instance_name)
    # print(" type(api_response)", type(api_response))
    # print(" api_response", api_response)
    # print()
    #
    # print("Vaporise named loaded image classifier:")
    # api_response = api_instance.image_classifier_vaporise(instance_name)
    # print(" type(api_response)", type(api_response))
    # print(" api_response", api_response)
    # print()
except ApiException as e:
    print("Exception when calling a image classifier operation: %s\n" % e)
except urllib3.exceptions.HTTPError as e:
    print("Connection HTTPError! %s\n" % e)
