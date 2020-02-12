""" Example: Shows use the image reader. """

import urllib3
import cv2

import feersum_nlu
from feersum_nlu.rest import ApiException
from examples import feersumnlu_host, feersum_nlu_auth_token

from feersum_nlu_util import image_utils

# Configure API key authorization: APIKeyHeader
configuration = feersum_nlu.Configuration()

# configuration.api_key['AUTH_TOKEN'] = feersum_nlu_auth_token
configuration.api_key['X-Auth-Token'] = feersum_nlu_auth_token  # Alternative auth key header!

configuration.host = feersumnlu_host

api_instance = feersum_nlu.ImageReadersApi(feersum_nlu.ApiClient(configuration))

caller_name = 'example_caller'

# cap = cv2.VideoCapture(1)  # pylint: disable=no-member
print()

try:
    while True:
        # Capture frame-by-frame
        # ret, frame = cap.read()
        image = cv2.imread('/Users/bduvenhage/Desktop/disc3.jpg')

        # height, width = image.shape[:2]
        # target_size = 800
        #
        # if width > height:
        #     resized_height = target_size
        #     resized_width = int((target_size / height) * width)
        # else:
        #     resized_height = int((target_size / width) * height)
        #     resized_width = target_size
        #
        # resized_image = \
        #     cv2.resize(image, (resized_width, resized_height), interpolation=cv2.INTER_LINEAR)  # pylint: disable=no-member

        resized_image = image

        base64_img_str = image_utils.load_image_opencvBGR(resized_image)
        image_input = feersum_nlu.ImageInput(base64_img_str)  # The same size as the camera frame, but jpeg encoded.

        print("Read from image:")
        text_list = api_instance.image_reader_retrieve("generic", image_input, x_caller=caller_name)
        print(text_list)
        print(f"base64_img_str size = {round(len(base64_img_str)/1024, 2)}kB")
        print()

        for idx, text_object in enumerate(text_list):
            # Display the resulting frame
            font = cv2.FONT_HERSHEY_SIMPLEX  # pylint: disable=no-member

            cv2.putText(resized_image,  # pylint: disable=no-member
                        f"{text_object.text}",  # pylint: disable=no-member
                        (10, 30 + idx*35), font, 1, (0, 0, 0), 5)  # pylint: disable=no-member
            cv2.putText(resized_image,  # pylint: disable=no-member
                        f"{text_object.text}",  # pylint: disable=no-member
                        (10, 30 + idx*35), font, 1, (255, 255, 255), 2)  # pylint: disable=no-member

        cv2.imshow('img', resized_image)  # pylint: disable=no-member

        if cv2.waitKey(1) & 0xFF == ord('q'):  # pylint: disable=no-member
            break

    # When everything done, release the capture
    # cap.release()
    cv2.destroyAllWindows()  # pylint: disable=no-member

except ApiException as e:
    print("Exception when calling a image classifier operation: %s\n" % e)
except urllib3.exceptions.HTTPError as e:
    print("Connection HTTPError! %s\n" % e)
