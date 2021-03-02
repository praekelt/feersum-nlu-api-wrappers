""" Example: Shows how to create, train and use an image classifier. """

import urllib3
import time
import random

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

api_client = feersum_nlu.ApiClient(configuration)

# Example of how to setup request retries!
api_client.rest_client.pool_manager.connection_pool_kw['retries'] = 3
api_instance = feersum_nlu.ImageClassifiersApi(api_client)

# instance_name = 'freiburg_groceries'
# all_data_path = "/Users/bduvenhage/Desktop/vision_data/freiburg_groceries_dataset"
# labels = ["BEANS", "CAKE", "CANDY", "CEREAL", "CHIPS", "CHOCOLATE", "COFFEE", "CORN", "FISH", "FLOUR", "HONEY", "JAM",
#           "JUICE", "MILK", "NUTS", "OIL", "PASTA", "RICE", "SODA", "SPICES", "SUGAR", "TEA", "TOMATO_SAUCE", "VINEGAR", "WATER"]

# instance_name = 'under_vs_over_image_clsfr'
# all_data_path = "/Users/bduvenhage/Desktop/vision_data/DrOetker_cropped/all"
# labels = ["over", "under"]

# instance_name = 'cat_vs_dog_image_clsfr'
# all_data_path = "/Users/bduvenhage/Desktop/vision_data/dogs-vs-cats/train"
# labels = ["cat", "dog"]

instance_name = 'hot_dog_vs_not_hot_dog'
all_data_path = "/Users/bduvenhage/Desktop/vision_data/hot-dog-vs-not-hot-dog/train"
labels = ["hot_dog", "not_hot_dog"]

# === Load the data samples ===
training_list = []  # type: List[Tuple[str, str]]
testing_list = []  # type: List[Tuple[str, str]]

print("Loading data samples...", end='', flush=True)
for label in labels:
    samples = image_utils.get_image_samples(all_data_path, label,
                                            max_samples=50)

    num_samples = len(samples)
    print(f"label: num_samples = {num_samples}")
    num_testing_samples = int(num_samples * 0.1)
    num_training_samples = num_samples - num_testing_samples

    random.shuffle(samples)
    training_samples = samples[:num_training_samples]
    testing_samples = samples[num_training_samples:]

    training_list.extend(training_samples)
    testing_list.extend(testing_samples)
print("done.")

training_samples = [feersum_nlu.LabelledImageSample(image=image, label=label) for image, label in training_list]
testing_samples = [feersum_nlu.LabelledImageSample(image=image, label=label) for image, label in testing_list]
# === ===

create_details = feersum_nlu.ImageClassifierCreateDetails(name=instance_name,
                                                          desc=instance_name,
                                                          load_from_store=False)

train_details = feersum_nlu.TrainDetails(temperature=1.0,
                                         immediate_mode=False,
                                         clsfr_algorithm="resnet152",
                                         num_epochs=15)

# image_utils.show_image("/Users/bduvenhage/Desktop/1500x500.jpg")
# image_string = image_utils.load_image(file_name="/Users/bduvenhage/Desktop/1500x500.jpg")
# image_utils.save_image(file_name="/Users/bduvenhage/Desktop/1500x500_.png", base64_string=image_string)

image_input = feersum_nlu.ImageInput(testing_samples[0].image)
print("len(image_input.image) =", len(image_input.image))

caller_name = 'example_caller'

print()

try:
    # print("Classify image:")
    # api_response = api_instance.image_classifier_retrieve(instance_name, image_input, x_caller=caller_name)
    # print(" type(api_response)", type(api_response))
    # print(" api_response", api_response)
    # print()
    # exit(0)

    # print("Update the model params:")
    # model_params = feersum_nlu.ModelParams(readonly=False)
    # api_response = api_instance.image_classifier_set_params(instance_name, model_params, x_caller=caller_name)
    # print(" type(api_response)", type(api_response))
    # print(" api_response", api_response)
    # print()
    #
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

    print("Create the image classifier:")
    api_response = api_instance.image_classifier_create(create_details)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    # api_response = api_instance.image_classifier_add_training_samples(instance_name, training_samples)
    # print(" type(api_response)", type(api_response))
    # print(" api_response", api_response)
    # print()

    batch_size = 25

    print("Add training samples to the image classifier:")
    len_training_samples = len(training_samples)
    for s in range(0, len_training_samples, batch_size):
        api_response = api_instance.image_classifier_add_training_samples(instance_name, training_samples[s:(s + batch_size)])
        print(" type(api_response)", type(api_response))
        print(" len(api_response)", len(api_response))
    print()

    print("Add testing samples to the image classifier:")
    len_testing_samples = len(testing_samples)
    for s in range(0, len_testing_samples, batch_size):
        api_response = api_instance.image_classifier_add_testing_samples(instance_name, testing_samples[s:(s + batch_size)])
        print(" type(api_response)", type(api_response))
        print(" len(api_response)", len(api_response))
    print()

    print("Get the training samples of the image classifier:")
    api_response = api_instance.image_classifier_get_training_samples(instance_name)
    print(" type(api_response)", type(api_response))
    print(" len(api_response)", len(api_response))
    print()

    print("Train the image classifier:")
    instance_detail = api_instance.image_classifier_train(instance_name, train_details)
    print(" type(api_response)", type(instance_detail))
    print(" api_response", instance_detail)
    print()

    # TRAINING:
    # If timestamp is missing then the training is running in the background and you need to poll until the
    # model ID has updated.
    # In the near future webhooks will be supported to let you know when async training has finished.

    if instance_detail.training_stamp is None:
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
    model_params = feersum_nlu.ModelParams(threshold=0.9,
                                           temperature=1.0,
                                           desc="Examples: Test image classifier.",
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
