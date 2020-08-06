""" Example: Shows how to create and use an image dataset. """

import urllib3
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

api_instance = feersum_nlu.ImageDatasetsApi(feersum_nlu.ApiClient(configuration))

instance_name = 'cat_vs_dog_image_dataset'
all_data_path = "/Volumes/256GB/vision_data/dogs-vs-cats/train"
labels = ["cat", "dog"]

# === Load the data samples ===
sample_list = []  # type: List[Tuple[str, str]]

print("Loading data samples...", end='', flush=True)
for label in labels:
    image_samples = image_utils.get_image_samples(all_data_path, label,
                                                  max_samples=100)

    num_image_samples = len(image_samples)
    print(f"label: num_image_samples = {num_image_samples}")

    random.shuffle(image_samples)
    sample_list.extend(image_samples)
print("done.")

dataset_samples = [feersum_nlu.LabelledImageSample(image=image, label=label) for image, label in sample_list]
# === ===

create_details = feersum_nlu.ImageDatasetCreateDetails(name=instance_name,
                                                       desc=instance_name,
                                                       load_from_store=False)

caller_name = 'example_caller'

print()

try:
    print("Create the image dataset:")
    api_response = api_instance.image_dataset_create(create_details)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    # api_response = api_instance.image_dataset_add_samples(instance_name, dataset_samples)
    # print(" type(api_response)", type(api_response))
    # print(" api_response", api_response)
    # print()

    print("Add dataset samples to the image dataset:")
    for dataset_sample in dataset_samples:
        api_response = api_instance.image_dataset_add_samples(instance_name, [dataset_sample])
        print(" type(api_response)", type(api_response))
        print(" api_response", api_response)
    print()

    print("Get the dataset samples of the image dataset:")
    api_response = api_instance.image_dataset_get_samples(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the details of all loaded image datasets:")
    api_response = api_instance.image_dataset_get_details_all()
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the details of specific named loaded image dataset:")
    api_response = api_instance.image_dataset_get_details(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the labels of named loaded image dataset:")
    api_response = api_instance.image_dataset_get_labels(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    # print("Delete named loaded image dataset:")
    # api_response = api_instance.image_dataset_del(instance_name)
    # print(" type(api_response)", type(api_response))
    # print(" api_response", api_response)
    # print()
    #
    # print("Vaporise named loaded image dataset:")
    # api_response = api_instance.image_dataset_vaporise(instance_name)
    # print(" type(api_response)", type(api_response))
    # print(" api_response", api_response)
    # print()
except ApiException as e:
    print("Exception when calling a image dataset operation: %s\n" % e)
except urllib3.exceptions.HTTPError as e:
    print("Connection HTTPError! %s\n" % e)
