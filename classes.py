from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class BoundingBox:
    top: int
    left: int
    bottom: int
    right: int

@dataclass
class Hold:
    bounding_box: BoundingBox
    dominant_color: Tuple[int]

@dataclass
class Route:
    holds: List[Hold]