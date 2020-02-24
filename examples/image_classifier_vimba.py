""" Example: Shows how to use an image classifier with a webcam. """

import urllib3
from pymba import Vimba, VimbaException
import cv2

import feersum_nlu
from feersum_nlu.rest import ApiException
from examples import feersumnlu_host, feersum_nlu_auth_token

from feersum_nlu_util import image_utils

PIXEL_FORMATS_CONVERSIONS = {
    'BayerRG8': cv2.COLOR_BAYER_RG2RGB,  # pylint: disable=no-member
}

# Configure API key authorization: APIKeyHeader
configuration = feersum_nlu.Configuration()

# configuration.api_key['AUTH_TOKEN'] = feersum_nlu_auth_token
configuration.api_key['X-Auth-Token'] = feersum_nlu_auth_token  # Alternative auth key header!

configuration.host = feersumnlu_host

api_instance = feersum_nlu.ImageClassifiersApi(feersum_nlu.ApiClient(configuration))

# instance_name = 'under_vs_over_image_clsfr'
instance_name = 'cat_vs_dog_image_clsfr'
# instance_name = 'hot_dog_vs_not_hot_dog_image_clsfr'

caller_name = 'example_caller'

with Vimba() as vimba:
    camera = vimba.camera(0)  # pylint: disable=no-member

    camera.open()
    camera.arm('SingleFrame')

    try:
        print("Get the details of specific named loaded image classifiers:")
        api_response = api_instance.image_classifier_get_details(instance_name)
        print(" type(api_response)", type(api_response))
        print(" api_response", api_response)
        print()

        while True:
            # Capture frame-by-frame
            try:
                frame = camera.acquire_frame()
                image = frame.buffer_data_numpy()

                image = cv2.cvtColor(image, PIXEL_FORMATS_CONVERSIONS[frame.pixel_format])  # pylint: disable=no-member

                height, width = image.shape[:2]
                target_size = 256

                if width > height:
                    resized_height = target_size
                    resized_width = int((target_size / height) * width)
                else:
                    resized_height = int((target_size / width) * height)
                    resized_width = target_size

                resized_image = \
                    cv2.resize(image, (resized_width, resized_height),  # pylint: disable=no-member
                               interpolation=cv2.INTER_LINEAR)  # pylint: disable=no-member

                base64_img_str = image_utils.load_image_opencvBGR(resized_image)
                image_input = feersum_nlu.ImageInput(base64_img_str)  # The same size as the camera image, but jpeg encoded.

                print("Classify image:")
                score_label_list = api_instance.image_classifier_retrieve(instance_name, image_input, x_caller=caller_name)
                # score_label_list = [feersum_nlu.ScoredLabel(label="cat", probability=0.9)]
                # print(" type(api_response)", type(score_label_list))
                # print(" api_response", score_label_list)
                print(score_label_list)
                print(f"base64_img_str size = {round(len(base64_img_str)/1024, 2)}kB")
                print()

                # Display the resulting image
                font = cv2.FONT_HERSHEY_SIMPLEX  # pylint: disable=no-member
                cv2.putText(resized_image,  # pylint: disable=no-member
                            f"{score_label_list[0].label} {round(score_label_list[0].probability,2)}",
                            (10, 30), font, 1, (0, 0, 0), 5)  # pylint: disable=no-member
                cv2.putText(resized_image,  # pylint: disable=no-member
                            f"{score_label_list[0].label} {round(score_label_list[0].probability,2)}",
                            (10, 30), font, 1, (255, 255, 255), 2)  # pylint: disable=no-member

                cv2.imshow('img', resized_image)  # pylint: disable=no-member

                if cv2.waitKey(1) & 0xFF == ord('q'):  # pylint: disable=no-member
                    break

            except VimbaException as e:
                # rearm camera upon frame timeout!
                if e.error_code == VimbaException.ERR_TIMEOUT:
                    print(e)
                    camera.disarm()
                    camera.arm('SingleFrame')
                else:
                    raise

    except ApiException as e:
        print("Exception when calling a image classifier operation: %s\n" % e)
    except urllib3.exceptions.HTTPError as e:
        print("Connection HTTPError! %s\n" % e)

    camera.disarm()
    camera.close()
