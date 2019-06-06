import PIL
from PIL import Image

import base64
import io


# =======================================
# =======================================
# =======================================
def show_image(file_name: str):
    im = Image.open(file_name)
    im.show()


def load_image(file_name: str) -> str:
    """
    Load an image from disk and encode to base64 jpeg.

    :param file_name: The file name to load.
    :return: utf8 encoded base64 string.
    """
    pil_image = Image.open(file_name)

    # Resize the image.
    target_size = 256
    w, h = pil_image.size

    if w < h:
        resize_w = target_size
        resize_h = round(h / w * target_size)
    else:
        resize_w = round(w / h * target_size)
        resize_h = target_size

    pil_image = pil_image.resize((resize_w, resize_h), PIL.Image.BILINEAR)

    # Save to in memory jpeg byte stream.
    image_file = io.BytesIO()
    pil_image.save(fp=image_file, format="jpeg", quality=50)
    base64_bytes = base64.b64encode(image_file.getvalue())

    return base64_bytes.decode('utf-8')


def save_image(file_name: str, base64_string: str) -> bool:
    """
    Save a base64 encoded image to disk.

    :param file_name: The image file name. Image format to save is deduced from the file extension.
    :param base64_string: The base64 encoded string to decode and save.
    :return: True if successful.
    """
    base8_bytes = base64.b64decode(base64_string.encode('utf-8'))
    image_file = io.BytesIO(base8_bytes)
    pil_image = Image.open(image_file)
    pil_image.save(fp=file_name)

    return True
