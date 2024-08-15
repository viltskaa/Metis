from typing import Sequence, Optional, List
from sklearn.neighbors import KDTree

import numpy as np

from app.database import TableTopPattern
from app.services import TableTopPatternService, ColorPalletPatternService
from app.services.parse_color import hex_to_rgb


def calculate_color_similarity(new_rgb_colors: Sequence[Sequence[int]], existing_rgb_colors: np.ndarray) -> float:
    kdtree = KDTree(existing_rgb_colors)
    total_similarity_score = 0.0

    for new_rgb in new_rgb_colors:
        new_rgb_normalized = [new_rgb[0] / 255.0, new_rgb[1] / 255.0, new_rgb[2] / 255.0]
        dist, _ = kdtree.query([new_rgb_normalized], k=1)
        total_similarity_score += dist[0][0]

    return total_similarity_score / len(new_rgb_colors)


def compare_sizes(width1: float, height1: float, perimeter1: float,
                  width2: float, height2: float, perimeter2: float,
                  tolerance: float = 0.01) -> bool:
    width_diff = abs(width1 - width2) / max(width1, width2)
    height_diff = abs(height1 - height2) / max(height1, height2)
    perimeter_diff = abs(perimeter1 - perimeter2) / max(perimeter1, perimeter2)

    return width_diff <= tolerance and height_diff <= tolerance and perimeter_diff <= tolerance


def get_similar_id(width: float,
                   height: float,
                   perimeter: float,
                   colors_rgb: Sequence[Sequence[int]],
                   similarity: float) -> Optional[int]:
    all_patterns: List[TableTopPattern] = TableTopPatternService.read_all()
    min_similarity = 1000.0
    result_id = None

    for pattern in all_patterns:
        if compare_sizes(width, height, perimeter, pattern.width, pattern.height, pattern.perimeter):
            pattern_colors_rgb: np.ndarray = np.array([
                [float(c) / 255.0 for c in hex_to_rgb(color.hex_color)]
                for color in ColorPalletPatternService.read_all_by_ttp_id(pattern.id)
            ])

            color_similarity: float = calculate_color_similarity(colors_rgb, pattern_colors_rgb)

            if color_similarity < min_similarity:
                min_similarity = color_similarity
                result_id = pattern.id

    if min_similarity < similarity:
        return result_id
    else:
        return None
