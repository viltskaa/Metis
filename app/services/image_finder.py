import base64
from PIL import Image
from io import BytesIO


def path_to_base64(image_path: str) -> str:
    with Image.open(image_path) as img:
        buffered = BytesIO()
        img.save(buffered, format="JPEG")
        img_bytes = buffered.getvalue()
        img_base64 = base64.b64encode(img_bytes).decode("utf-8")

    return img_base64
