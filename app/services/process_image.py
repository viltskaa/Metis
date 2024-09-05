import base64
import os
from datetime import datetime, timezone

import cv2
import numpy as np

from cv import ContourFinder


def save_image(image):
    img_filename = f"processed_image_{datetime.now(timezone.utc).strftime('%Y%m%d%H%M%S')}.jpg"
    img_directory = os.path.join(os.getcwd(), 'saved_images')
    os.makedirs(img_directory, exist_ok=True)
    img_path = os.path.join(img_directory, img_filename)

    cv2.imwrite(img_path, image)
    return img_path


def decode_image(image_base64):
    try:
        image_data = base64.b64decode(image_base64)
        np_arr = np.frombuffer(image_data, np.uint8)
        return cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    except Exception as e:
        raise ValueError(f"Failed to decode image: {e}")


def convert_image_to_base64(image):
    _, buffer = cv2.imencode('.jpg', image)
    return base64.b64encode(buffer).decode('utf-8')


def format_data(data, limit):
    result = []
    for item in data[:limit]:
        if isinstance(item, np.ndarray):
            result.append(item.tolist())
        elif isinstance(item, list):
            result.append(item)
        else:
            result.append(str(item))
    return result


def process_image(image_base64):
    try:
        image = decode_image(image_base64)

        cf = ContourFinder(
            image=image,
            blur=(7, 7),
            threshold=(160, 280),
            kernel_ksize=(15, 15),
            clusters=5,
            draw_contours=False
        )

        img, (perimeter, width, height), colors = cf.produce(return_image=True)

        perimeter = float(perimeter)
        width = float(width)
        height = float(height)

        return img, perimeter, width, height, colors
    except Exception as e:
        raise RuntimeError(f"Failed to process image: {e}")


def process_image_pattern(image_base64):
    try:
        image = decode_image(image_base64)

        cf = ContourFinder(
            image=image,
            blur=(7, 7),
            threshold=(160, 280),
            kernel_ksize=(15, 15),
            clusters=50,
            draw_contours=False
        )

        img, (perimeter, width, height), colors = cf.produce(return_image=True)
        path = save_image(image)

        perimeter = float(perimeter)
        width = float(width)
        height = float(height)

        return img, perimeter, width, height, colors, path
    except Exception as e:
        raise RuntimeError(f"Failed to process image: {e}")