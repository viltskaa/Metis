import base64
import os
from datetime import datetime, timezone

import cv2
import numpy as np

from cv import ContourFinder

def undistort_image(image):
  camera_matrix = np.array([[1.67628927e+03, 0.00000000e+00, 9.32036340e+02],
               [0.00000000e+00, 1.68409533e+03, 4.84948281e+02],
               [0.00000000e+00, 0.00000000e+00, 1.00000000e+00]])
  dist_coefs = np.array([-0.62830179, 0.79986763, -0.00491951, -0.00458237, -0.73075514])

  try:
    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    h, w = img.shape[:2]
    newcameramtx, roi = cv2.getOptimalNewCameraMatrix(camera_matrix, dist_coefs, (w, h), 1, (w, h))
    dst = cv2.undistort(img, camera_matrix, dist_coefs, None, newcameramtx)
    dst = cv2.cvtColor(dst, cv2.COLOR_RGB2BGR)

    return dst
  except cv2.error as e:
    print(f"Ошибка обработки изображения: {e}")
    return None
  except Exception as e:
    print(f"Произошла неизвестная ошибка: {e}")
    return None

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

        undistorted_img = undistort_image(image)

        cf = ContourFinder(
            image=undistorted_img,
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

        undistorted_img = undistort_image(image)

        cf = ContourFinder(
            image=undistorted_img,
            blur=(7, 7),
            threshold=(160, 280),
            kernel_ksize=(15, 15),
            clusters=50,
            draw_contours=False
        )

        img, (perimeter, width, height), colors = cf.produce(return_image=True)
        path = save_image(undistorted_img)

        perimeter = float(perimeter)
        width = float(width)
        height = float(height)

        return img, perimeter, width, height, colors, path
    except Exception as e:
        raise RuntimeError(f"Failed to process image: {e}")