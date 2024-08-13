import base64
import operator
import os
import time
from datetime import datetime, timezone
from functools import wraps
from random import randint
from typing import Any, Sequence, Tuple, List, Annotated

import cv2
import imutils
import numpy as np
from numpy import ndarray, dtype

_NUMBER_TYPE = np.float64 | np.int32 | int | float | np.float32 | np.int64
_IMAGE_TYPE = cv2.Mat | ndarray[Any, dtype] | ndarray
_RGB = Annotated[Sequence[int], 3]
_POINT_TYPE = Annotated[List[_NUMBER_TYPE] | Tuple[_NUMBER_TYPE], 2]


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__} Took {total_time:.4f} seconds')
        return result

    return timeit_wrapper


def bgr_to_rgb(color: _RGB) -> _RGB:
    return color[-1], color[1], color[0]


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


def process_image(image):
    try:
        img, cnt, colors = produce_contours(image, draw_contours=True)
        return img, cnt, colors
    except Exception as e:
        raise RuntimeError(f"Failed to process image: {e}")


@timeit
def delete_background(image: _IMAGE_TYPE) -> _IMAGE_TYPE:
    if image is None:
        raise ValueError("Image is None")

    mask = np.zeros(image.shape[:2], np.uint8)

    background_model = np.zeros((1, 65), np.float64)
    foreground_model = np.zeros((1, 65), np.float64)

    height, width = image.shape[:2]
    rect = (10, 10, width - 10, height - 10)
    cv2.grabCut(image, mask, rect, background_model, foreground_model, 5, cv2.GC_INIT_WITH_RECT)

    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
    image_no_background = image * mask2[:, :, np.newaxis]

    return image_no_background


@timeit
def produce_contours(
        image: _IMAGE_TYPE,
        blur: Tuple[int, int] = (3, 3),
        threshold: Tuple[int, int] = (140, 280),
        kernel_ksize: Tuple[int, int] = (15, 15),
        clusters: int = 5,
        iterations_kmeans: int = 10,
        draw_contours: bool = False,
) -> Tuple[_IMAGE_TYPE, Sequence[Tuple[_NUMBER_TYPE, _NUMBER_TYPE, _NUMBER_TYPE]], Sequence[_RGB]]:
    image = delete_background(image)

    data = np.reshape(image, (-1, 3))
    mask = np.all(data == [0, 0, 0], axis=1)
    data = data[~mask]
    data = np.float32(data)

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    flags = cv2.KMEANS_RANDOM_CENTERS
    _, _, centers = cv2.kmeans(data, clusters, None, criteria, iterations_kmeans, flags)

    gaussian_blur = cv2.GaussianBlur(image, blur, 0)
    edges = cv2.Canny(gaussian_blur, *threshold)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernel_ksize)
    closed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

    contours = cv2.findContours(
        closed.copy(),
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )
    contours = imutils.grab_contours(contours)
    output = []

    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)

        if draw_contours:
            center_y: int = np.mean([y, y + h]).astype(int)
            center_x: int = np.mean([x, x + w]).astype(int)

            color = (randint(0, 255), randint(0, 255), randint(0, 255))

            cv2.line(image, (x, center_y), (x + w, center_y), color, 1)
            cv2.line(image, (center_x, y), (center_x, y + h), color, 1)
            cv2.drawContours(image, [contour], -1, color, 2)

        output.append((cv2.arcLength(contour, True), w, h))

    output = sorted(output, key=operator.itemgetter(0), reverse=True)

    return image, output, [bgr_to_rgb(bgr.astype(np.uint8)) for bgr in centers]
