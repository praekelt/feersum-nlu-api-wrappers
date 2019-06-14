from typing import List, Tuple, Optional

import PIL
from PIL import Image

import base64
import io
import os


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
    pil_image.save(fp=image_file, format="jpeg", quality=50)
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
    except IOError:
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


def load_image(file_name: str) -> str:
    """
    Load an image from disk, resize and encode to base64 jpeg.

    :param file_name: The file name to load.
    :return: utf8 encoded base64 string.
    :exception IOError: If the file cannot be found, or the image cannot be
       opened and identified.
    """
    pil_image = Image.open(file_name)
    return _base64_encode_from_pil_image(_resize_pil_image(pil_image))


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


def check_image_format(base64_image_str: str) -> bool:
    """
    Reformat the base64 image string for consumption by API.

    :param base64_image_str: utf8 encoded base64 image string.
    :return: True if image is 256x256xRGB jpeg.
    """
    pil_image = _base64_decode_to_pil_image(base64_image_str)

    if pil_image is None:
        return False

    w, h = pil_image.size
    target_size = 256  # The service expects images with smallest dimension 256 pixels!

    return ((w == target_size) and (h >= target_size)) or ((w >= target_size) and (h == target_size))


def reformat_image(base64_image_str: str) -> Optional[str]:
    """
    Reformat the base64 image string for consumption by API.

    :param base64_image_str: utf8 encoded base64 image string.
    :return: utf8 encoded base64 string (256x256xRGB jpeg)
    """
    pil_image = _base64_decode_to_pil_image(base64_image_str)

    if pil_image is None:
        return None

    return _base64_encode_from_pil_image(_resize_pil_image(pil_image))


def get_image_samples(data_path: str, label: str) -> List[Tuple[str, str]]:
    """
    Get all the images within a specific data_path/'label' file path and assign 'label' to the samples.
    :param data_path: The base path i.e. '/home/data/cat_vs_dog'
    :param label: The actual label folder to load i.e. 'cat' which would load images in '/home/data/cat_vs_dog/cat' as cat.
    :return: The list of loaded base64 image samples all labeled with 'label'.
    """
    directory = os.fsencode(data_path + "/" + label)

    image_samples = []  # type: List[Tuple[str, str]]

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith((".jpg", ".jpeg", ".j2k", ".j2p", ".jpx", ".png", ".bmp")):
            image_samples.append((load_image(data_path + "/" + label + "/" + filename), label))

    return image_samples
