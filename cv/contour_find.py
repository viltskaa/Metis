import operator
import time
from functools import wraps
from typing import Any, Annotated, Sequence, List, Tuple, Optional

import cv2
import imutils
import numpy as np
from sklearn.cluster import KMeans
from numpy import ndarray, dtype

_NUMBER_TYPE = np.float64 | np.int32 | int | float | np.float32 | np.int64
_IMAGE_TYPE = cv2.Mat | np.ndarray[Any, np.dtype] | np.ndarray
_RGB = _BGR = Annotated[Sequence[int], 3]
_HEX = str
_POINT_TYPE = Annotated[List[_NUMBER_TYPE] | Tuple[_NUMBER_TYPE], 2]
_CONTOUR_TYPE = Sequence[cv2.Mat | ndarray[Any, dtype] | ndarray], cv2.Mat | ndarray[Any, dtype] | ndarray


def between2points(p1: _POINT_TYPE, p2: _POINT_TYPE) -> np.float32:
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2).astype(np.float32)


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


class Color:
    def __init__(self, *,
                 rgb: Optional[_RGB] = None,
                 bgr: Optional[_BGR] = None):
        self.__rgb: Optional[_RGB] = None
        if rgb is not None:
            self.__rgb: _RGB = rgb
        if bgr is not None:
            self.__rgb: _RGB = (bgr[-1], bgr[1], bgr[0])

    @property
    def rgb(self) -> Optional[_RGB]:
        return self.__rgb

    @property
    def hex(self) -> Optional[_HEX]:
        if self.__rgb is not None:
            return "#%02x%02x%02x" % (int(self.__rgb[0]), int(self.__rgb[1]), int(self.__rgb[2]))
        return None

    def __str__(self) -> str:
        if self.__rgb is not None:
            return self.hex
        return "None"

    def __repr__(self) -> str:
        return self.__str__()


class ContourFinder:
    def __init__(
            self,
            image: _IMAGE_TYPE,
            *,
            blur: Tuple[int, int] = (3, 3),
            threshold: Tuple[int, int] = (140, 280),
            kernel_ksize: Tuple[int, int] = (15, 15),
            clusters: int = 5,
            draw_contours: bool = False,
    ):
        self.__image = image
        self.__blur = blur
        self.__threshold = threshold
        self.__kernel_ksize = kernel_ksize
        self.__clusters = clusters
        self.__draw_contours = draw_contours

    @timeit
    def __get_pallet(self, array: ndarray) -> List[Color]:
        array_from_image = array
        palette, index = np.unique(self.__asvoid(array_from_image).ravel(), return_inverse=True)
        palette = palette.view(array_from_image.dtype).reshape(-1, array_from_image.shape[-1])
        count = np.bincount(index)
        order = np.argsort(count)
        return [Color(bgr=rgb.astype(np.int16)) for rgb in palette[order[::-1]]]

    @timeit
    def __get_pallet_kmeans(self, array: ndarray) -> List[Color]:
        kmeans = KMeans(n_clusters=self.__clusters)
        kmeans.fit(array)
        return [Color(bgr=rgb) for rgb in kmeans.cluster_centers_.astype(int)]

    @staticmethod
    def __asvoid(array):
        array = np.ascontiguousarray(array)
        return array.view(np.dtype((np.void, array.dtype.itemsize * array.shape[-1])))

    def __get_pallet_from_contour(self, contour: _CONTOUR_TYPE) -> List[Color]:
        fill_color = (255, 255, 255)
        mask = np.zeros(self.__image.shape[:2], dtype=np.uint8)
        cv2.drawContours(mask, [contour], -1, fill_color, thickness=cv2.FILLED)

        pixels_inside_contour = cv2.bitwise_and(self.__image, self.__image, mask=mask)
        pixels_inside_contour = pixels_inside_contour[np.where((pixels_inside_contour != [0, 0, 0]).any(axis=2))]

        return self.__get_pallet_kmeans(pixels_inside_contour)

    @timeit
    def produce(
            self, *,
            return_image: bool = False
    ) -> tuple[_IMAGE_TYPE | None, tuple[float | Any, np.float32, np.float32], list[Color]]:
        gray_scale_image = self.__image.copy()
        gaussian_blur = cv2.GaussianBlur(gray_scale_image, self.__blur, 0)
        edges = cv2.Canny(gaussian_blur, *self.__threshold)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, self.__kernel_ksize)
        closed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

        contours = cv2.findContours(
            closed,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )
        contours = imutils.grab_contours(contours)
        contour, contour_lenght = sorted(
            [[contour, cv2.arcLength(contour, True)] for contour in contours],
            key=operator.itemgetter(1),
            reverse=True
        )[0]

        rect = cv2.minAreaRect(contour)
        box = cv2.boxPoints(rect)
        box = np.int32(box)

        possible_distances = (
            between2points(box[0], box[1]),
            between2points(box[1], box[2])
        )

        pallet = self.__get_pallet_from_contour(contour)

        if self.__draw_contours:
            color = 36, 255, 12
            cv2.drawContours(self.__image, [contour], -1, color, 5)
            cv2.drawContours(self.__image, [box], -1, color, 5)

        return (
            self.__image if return_image else None,
            (contour_lenght, min(possible_distances), max(possible_distances)),
            pallet
        )
