from typing import List, Tuple, Optional, Dict, Any

import PIL
from PIL import Image

import cv2
import random

import base64
import io
import os
import binascii


def _resize_pil_image(pil_image: Image) -> Image:
    """
    Resize the image if required.

    :param pil_image: The input image.
    :return: A resized pillow image OR the input image.
    """
    target_size = 256  # The service expects images with smallest dimension 256 pixels!
    w, h = pil_image.size

    if (w < target_size) or (h < target_size) or ((w > target_size) and (h > target_size)):
        if w < h:
            resize_w = target_size
            resize_h = round(h / w * target_size)
        else:
            resize_w = round(w / h * target_size)
            resize_h = target_size

        return pil_image.resize((resize_w, resize_h), PIL.Image.BILINEAR)
    else:
        return pil_image


def _base64_encode_from_pil_image(pil_image: Image) -> str:
    """ Save image to base64 jpeg string.

    :param pil_image: The input image.
    :return: utf8 encoded base64 string.
    """
    image_file = io.BytesIO()
    pil_image.save(fp=image_file, format="jpeg", quality=75)
    base64_bytes = base64.b64encode(image_file.getvalue())
    return base64_bytes.decode('utf-8')


def _base64_decode_to_pil_image(base64_image_str: str) -> Optional[PIL.Image.Image]:
    """ Recover image from base64 jpeg string.

    :param base64_image_str: utf8 encoded base64 image string.
    :return: The recovered image.
    """
    try:
        base8_bytes = base64.b64decode(base64_image_str.encode('utf-8'))
        image_file = io.BytesIO(base8_bytes)
        return Image.open(image_file)
    except (IOError, binascii.Error, UnicodeError):
        return None


# =======================================
# =======================================
# =======================================
def show_image(file_name: str):
    """
    Show an image using PILLOW.

    :param file_name: The name of the file to load and display.
    :return: Nothing
    """
    im = Image.open(file_name)
    im.show()


def load_image_file(file_name: str,
                    ignore_resolution: bool = False,
                    random_crop: Optional[int] = None) -> str:
    """
    Load an image from file, resize and encode to base64 jpeg.

    :param file_name: The file name to load.
    :param ignore_resolution: Don't change the image resolution if True.
    :return: utf8 encoded base64 string.
    :exception IOError: If the file cannot be found, or the image cannot be
       opened and identified.
    """
    pil_image = Image.open(file_name)

    if pil_image.mode != 'RGB':
        pil_image = pil_image.convert(mode='RGB')

    if (random_crop is not None) and (random_crop > 0):
        w, h = pil_image.size
        left = random.randint(0, w - random_crop)
        right = left + random_crop - 1
        upper = random.randint(0, h - random_crop)
        lower = upper + random_crop - 1
        pil_image = pil_image.crop((left, upper, right, lower))

    if not ignore_resolution:
        pil_image = _resize_pil_image(pil_image)

    return _base64_encode_from_pil_image(pil_image)


def load_image_opencvBGR(opencv_image, ignore_resolution: bool = False) -> str:
    """
    Load an image from an opencv2 image, resize and encode to base64 jpeg.

    :param opencv_image: The opencv2 image.
    :param ignore_resolution: Don't change the image resolution if True.
    :return: utf8 encoded base64 string.
    :exception IOError: If the file cannot be found, or the image cannot be
       opened and identified.
    """
    pil_image = Image.fromarray(cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGB))  # pylint: disable=no-member

    if not ignore_resolution:
        pil_image = _resize_pil_image(pil_image)

    return _base64_encode_from_pil_image(pil_image)


def load_image_from_bytes(base8_bytes: bytes, ignore_resolution: bool = False) -> str:
    """
    Load an image from bytes, resize and encode to base64 jpeg.

    :param base8_bytes: The bytes of the image to laod.
    :param ignore_resolution: Don't change the image resolution if True.
    :return: utf8 encoded base64 string.
    :exception IOError: If the file cannot be found, or the image cannot be
       opened and identified.
    """
    image_file = io.BytesIO(base8_bytes)
    pil_image = Image.open(image_file)

    if not ignore_resolution:
        pil_image = _resize_pil_image(pil_image)

    return _base64_encode_from_pil_image(pil_image)


def save_image(file_name: str, base64_image_str: str) -> bool:
    """
    Save a base64 encoded image to disk.

    :param file_name: The image file name. Image format to save is deduced from the file extension.
    :param base64_image_str: The base64 encoded image to decode and save.
    :return: True if successful.
    """
    pil_image = _base64_decode_to_pil_image(base64_image_str)

    if pil_image is not None:
        pil_image.save(fp=file_name)
        return True
    else:
        return False


def check_image_format(base64_image_str: str, ignore_resolution: bool = False) -> bool:
    """
    Check the format of the base64 image string for consumption by API.

    :param base64_image_str: utf8 encoded base64 image string.
    :param ignore_resolution: Don't check the image resolution if True.
    :return: True if image is 256x256xRGB jpeg.
    """
    pil_image = _base64_decode_to_pil_image(base64_image_str)

    if pil_image is None:
        return False

    if ignore_resolution:
        return True  # return here that the format is ok if ignore_resolution!

    w, h = pil_image.size
    target_size = 256  # The service expects images with smallest dimension 256 pixels!

    return ((w == target_size) and (h >= target_size)) or ((w >= target_size) and (h == target_size))


def reformat_image(base64_image_str: str) -> Optional[str]:
    """
    Reformat the base64 image string for consumption by API. Changes both size and encoding.

    :param base64_image_str: utf8 encoded base64 image string.
    :return: utf8 encoded base64 string (256x256xRGB jpeg)
    """
    pil_image = _base64_decode_to_pil_image(base64_image_str)

    if pil_image is None:
        return None

    resized_image = _resize_pil_image(pil_image)

    return _base64_encode_from_pil_image(resized_image)


def get_image_samples(data_path: str, label: str,
                      max_samples: Optional[int] = None,
                      ignore_resolution: bool = False,
                      random_crop: Optional[int] = None,
                      repeat: Optional[int] = None) -> List[Tuple[str, str]]:
    """
    Get all the images within a specific data_path/'label' file path and assign 'label' to the samples.
    :param data_path: The base path i.e. '/home/data/cat_vs_dog'
    :param label: The actual label folder to load i.e. 'cat' which would load images in '/home/data/cat_vs_dog/cat' as cat.
    :param max_samples: The maximum number of samples to load and return.
    :param ignore_resolution: Don't change the image resolution if True.
    :return: The list of loaded base64 image samples all labeled with 'label'.
    """
    directory = os.fsencode(data_path + "/" + label)

    image_samples = []  # type: List[Tuple[str, str]]

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.lower().endswith((".jpg", ".jpeg", ".j2k", ".j2p", ".jpx", ".png", ".bmp")):
            if (repeat is None) or (repeat < 1):
                repeat = 1

            for i in range(repeat):
                image_samples.append((load_image_file(data_path + "/" + label + "/" + filename,
                                                      ignore_resolution=ignore_resolution,
                                                      random_crop=random_crop), label))

        if (max_samples is not None) and (len(image_samples) >= max_samples):
            break  # from for-loop.

    return image_samples


def get_image_value_samples(data_path: str,
                            name_value_dict: Dict[str, Any],
                            max_samples: Optional[int] = None) -> List[Tuple[str, Any]]:
    """
    Get all the images within a specific data_path and assign values from name_value_dict.
    :param data_path: The base path i.e. '/home/data/images'
    :param name_value_dict: The name value dict to use.
    :param max_samples: The maximum number of samples to load and return. No limit if max_samples=None!
    :return: The list of loaded base64 image samples all labeled with 'label'.
    """
    directory = os.fsencode(data_path)

    image_value_samples = []  # type: List[Tuple[str, Any]]

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.lower().endswith((".jpg", ".jpeg", ".j2k", ".j2p", ".jpx", ".png", ".bmp")):
            value = name_value_dict.get(filename)
            image_str = load_image_file(data_path + "/" + filename)

            if value is not None:
                image_value_samples.append((image_str, value))

        if (max_samples is not None) and (len(image_value_samples) >= max_samples):
            break  # from for-loop.

    return image_value_samples
