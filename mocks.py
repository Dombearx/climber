from typing import List
from PIL.Image import Image

from classes import BoundingBox, Hold


def mock_holds_detection() -> List[Hold]:
    return [
        Hold(
            bounding_box=BoundingBox(
                top=10,
                left=10,
                bottom=110,
                right=110
            ),
            dominant_color=(255, 0, 0)
        )
    ]