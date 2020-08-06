""" Example: Shows how to use an image classifier. """

import urllib3

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

instance_name = 'cat_vs_dog_image_clsfr'
# all_data_path = "/Users/bduvenhage/Desktop/DrOetker_cropped/all"
# labels = ["over", "under", "well"]
#
# # === Load the data samples ===
# testing_list = []  # type: List[Tuple[str, str]]
#
# for label in labels:
#     samples = image_utils.get_image_samples(all_data_path, label,
#                                             max_samples=10)
#     num_samples = len(samples)
#     print(f"label: num_samples = {num_samples}")
#
#     random.shuffle(samples)
#     testing_list.extend(samples)
#
# testing_samples = [feersum_nlu.LabelledImageSample(image=image, label=label) for image, label in testing_list]
# === ===

# image_utils.show_image("/Users/bduvenhage/Desktop/1500x500.jpg")
# image_string = image_utils.load_image(file_name="/Users/bduvenhage/Desktop/1500x500.jpg")
# image_utils.save_image(file_name="/Users/bduvenhage/Desktop/1500x500_.png", base64_string=image_string)

# image_input = feersum_nlu.ImageInput(testing_samples[0].image)
image_input = feersum_nlu.ImageInput(
    image_utils.load_image_file(file_name="/Users/bduvenhage/Desktop/vision_data/DrOetker_cropped/all/under/Untitled 20.png")
)
print("len(image_input) =", len(image_input.image))


caller_name = 'example_caller'

print()

try:
    print("Classify image:")
    api_response = api_instance.image_classifier_retrieve(instance_name, image_input, x_caller=caller_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

except ApiException as e:
    print("Exception when calling a image classifier operation: %s\n" % e)
except urllib3.exceptions.HTTPError as e:
    print("Connection HTTPError! %s\n" % e)
