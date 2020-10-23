""" Example: Shows how to create and use an image dataset. """

import urllib3

import feersum_nlu
from feersum_nlu.rest import ApiException
from examples import feersumnlu_host, feersum_nlu_auth_token

# from feersum_nlu_util import image_utils

# Configure API key authorization: APIKeyHeader
configuration = feersum_nlu.Configuration()

# configuration.api_key['AUTH_TOKEN'] = feersum_nlu_auth_token
configuration.api_key['X-Auth-Token'] = feersum_nlu_auth_token  # Alternative auth key header!

configuration.host = feersumnlu_host

api_instance = feersum_nlu.ImageDatasetsApi(feersum_nlu.ApiClient(configuration))

instance_name = 'labelled_images_1'

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

    print("Get the details of specific named loaded image dataset:")
    api_response = api_instance.image_dataset_get_details(instance_name)
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
