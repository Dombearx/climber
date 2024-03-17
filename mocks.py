from typing import List
from PIL.Image import Image
import json
from classes import BoundingBox, Hold


def mock_holds_detection() -> List[Hold]:
    holds_bboxes = json.load(open("data/examples_wall.json"))
    return [
        Hold(
            bounding_box=BoundingBox(
                top=bbox["bounding_box"]["top"],
                left=bbox["bounding_box"]["left"],
                bottom=bbox["bounding_box"]["bottom"],
                right=bbox["bounding_box"]["right"]
            ),
            dominant_color=None
        ) for bbox in holds_bboxes
    ]

mock_holds_detection()