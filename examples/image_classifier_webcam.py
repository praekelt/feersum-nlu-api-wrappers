""" Example: Shows how to create, train and use a image classifier. """

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

api_instance = feersum_nlu.ImageClassifiersApi(feersum_nlu.ApiClient(configuration))

instance_name = 'cat_vs_dog_image_clsfr'
caller_name = 'example_caller'

cap = cv2.VideoCapture(0)  # pylint: disable=no-member
print()

try:
    print("Get the details of specific named loaded image classifiers:")
    api_response = api_instance.image_classifier_get_details(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        height, width = frame.shape[:2]

        if width > height:
            resized_height = 256
            resized_width = int((256.0 / height) * width)
        else:
            resized_height = int((256.0 / width) * height)
            resized_width = 256

        resized_frame = \
            cv2.resize(frame, (resized_width, resized_height), interpolation=cv2.INTER_LINEAR)  # pylint: disable=no-member

        cv2.imwrite("img.png", resized_frame)  # pylint: disable=no-member
        image_input = feersum_nlu.ImageInput(image_utils.load_image("img.png"))

        print("Classify image:")
        score_label_list = api_instance.image_classifier_retrieve(instance_name, image_input, x_caller=caller_name)
        # print(" type(api_response)", type(score_label_list))
        # print(" api_response", score_label_list)
        print()
        print(score_label_list)

        # Display the resulting frame
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(resized_frame,  # pylint: disable=no-member
                    f"{score_label_list[0].label} {round(score_label_list[0].probability,2)}",  # pylint: disable=no-member
                    (10, 30), font, 1, (0, 0, 0), 5)  # pylint: disable=no-member
        cv2.putText(resized_frame,  # pylint: disable=no-member
                    f"{score_label_list[0].label} {round(score_label_list[0].probability,2)}",  # pylint: disable=no-member
                    (10, 30), font, 1, (255, 255, 255), 2)  # pylint: disable=no-member

        cv2.imshow('img', resized_frame)  # pylint: disable=no-member

        if cv2.waitKey(1) & 0xFF == ord('q'):  # pylint: disable=no-member
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()  # pylint: disable=no-member

except ApiException as e:
    print("Exception when calling a image classifier operation: %s\n" % e)
except urllib3.exceptions.HTTPError as e:
    print("Connection HTTPError! %s\n" % e)
