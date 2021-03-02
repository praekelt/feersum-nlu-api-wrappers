""" Example: Shows how to create, train and use an image classifier. """

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
caller_name = 'example_caller'

dataset_name = 'labelled_images_dataset'
api_instance = feersum_nlu.ImageDatasetsApi(feersum_nlu.ApiClient(configuration))
create_details = feersum_nlu.ImageDatasetCreateDetails(name=dataset_name,
                                                       load_from_store=True)
dataset_samples = []
print()

try:
    print("Load the image dataset:")
    api_response = api_instance.image_dataset_create(create_details)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the dataset samples of the image dataset:")
    dataset_samples = api_instance.image_dataset_get_samples(dataset_name)
    print(" type(dataset_samples)", type(dataset_samples))
    print(" dataset_samples", dataset_samples)
    print()

    print("Get the details of specific named loaded image dataset:")
    api_response = api_instance.image_dataset_get_details(dataset_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the labels of named loaded image dataset:")
    api_response = api_instance.image_dataset_get_labels(dataset_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

except ApiException as e:
    print("Exception when calling a image dataset operation: %s\n" % e)
except urllib3.exceptions.HTTPError as e:
    print("Connection HTTPError! %s\n" % e)

# image_utils.save_image(file_name="temp.png", base64_image_str=dataset_samples[0].image)
# image_utils.show_image("temp.png")


classifier_name = dataset_name
api_instance = feersum_nlu.ImageClassifiersApi(feersum_nlu.ApiClient(configuration))
create_details = feersum_nlu.ImageClassifierCreateDetails(name=classifier_name,
                                                          desc=classifier_name,
                                                          load_from_store=False)

training_samples = dataset_samples
testing_samples = dataset_samples
# === ===

train_details = feersum_nlu.TrainDetails(temperature=1.0,
                                         immediate_mode=False,
                                         clsfr_algorithm="resnet152",
                                         num_epochs=40)

caller_name = 'example_caller'

print()

try:
    print("Create the image classifier:")
    api_response = api_instance.image_classifier_create(create_details)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Add training samples to the image classifier:")
    for training_sample in training_samples:
        api_response = api_instance.image_classifier_add_training_samples(classifier_name, [training_sample])
        print(" type(api_response)", type(api_response))
        print(" api_response", api_response)
    print()

    print("Add testing samples to the image classifier:")
    for testing_sample in testing_samples:
        api_response = api_instance.image_classifier_add_testing_samples(classifier_name, [testing_sample])
        print(" type(api_response)", type(api_response))
        print(" api_response", api_response)
    print()

    print("Get the training samples of the image classifier:")
    api_response = api_instance.image_classifier_get_training_samples(classifier_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Train the image classifier:")
    instance_detail = api_instance.image_classifier_train(classifier_name, train_details)
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
            inst_det = api_instance.image_classifier_get_details(classifier_name)
            if inst_det.id != previous_id:
                # ToDo: Stop if details indicate that training failed.
                break  # break from while-loop when ID updated which indicates training done.

        print('Done.')
        print()

    print("Get the details of specific named loaded image classifiers:")
    api_response = api_instance.image_classifier_get_details(classifier_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    # Get the classifier's possible labels. Might be inferred from the training data, but guaranteed to be available
    # after training.
    print("Get the labels of named loaded image classifiers:")
    api_response = api_instance.image_classifier_get_labels(classifier_name)
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
