from pathlib import Path
from PIL.Image import Image, open
from PIL import ImageDraw
import matplotlib.pyplot as plt
from typing import List

from classes import Hold, Route
from mocks import mock_holds_detection
from Pylette import extract_colors

def draw_bboxes(image: Image, holds: List[Hold]) -> Image:
    # Create a drawing object
    new_image = image.copy()
    draw = ImageDraw.Draw(new_image, 'RGBA')
    
    # Define fill color with transparency
    fill_color = (255, 0, 0, 64)  # Red with specified opacity
    
    # Draw each bounding box
    for hold in holds:
        draw.rectangle([hold.bounding_box.left, hold.bounding_box.top, hold.bounding_box.right, hold.bounding_box.bottom], fill=fill_color)
    
    del draw  # Release drawing object
    return new_image

def get_hold_color(image, hold):
    image_part = image.crop([hold.bounding_box.left, hold.bounding_box.top, hold.bounding_box.right, hold.bounding_box.bottom])
    palette = extract_colors(image_part, palette_size=3, resize=True)
    return palette[0].rgb

def read_image(image_path: Path) -> Image:
    return open(image_path)

def detect_holds(image: Image) -> List[Hold]:
    return mock_holds_detection()

def detect_routes(image: Image, holds: List[Hold]) -> List[Route]:
    raise NotImplementedError

def select_route(routes: List[Route]) -> Route:
    raise NotImplementedError

def find_similar_routes(route: Route, database) -> List[Route]:
    raise NotImplementedError

def main():
    image_path = Path("images/example_wall.jpg")
    database = Path("")
    image = read_image(image_path)

    plt.imshow(image)
    plt.axis('off')  # Turn off axis labels
    plt.savefig("image.jpg")

    holds = detect_holds(image)
    new_image = draw_bboxes(image, holds)

    new_image.save("bboxes.jpg")

    colors = [get_hold_color(image, hold) for hold in holds]
    print(colors)
    # routes = detect_routes(image, holds)
    # route = select_route(routes)

    # similar_routes = find_similar_routes(route, database)



if __name__ == "__main__":
    main()