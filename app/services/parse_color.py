from typing import Sequence, Annotated, List


def rgb_to_hex(rgb: Sequence[int]) -> str:
    return f"#{rgb[0]:02X}{rgb[1]:02X}{rgb[2]:02X}"


def convert_rgb_to_hex_list(rgb_sequence: Sequence[Annotated[Sequence[int], 3]]) -> List[str]:
    return [rgb_to_hex(rgb) for rgb in rgb_sequence]


def hex_to_rgb(hex_color: str) -> Sequence[int]:
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
