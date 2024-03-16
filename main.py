from pathlib import Path
from PIL.Image import Image, open
from typing import List

from classes import Hold, Route
from mocks import mock_holds_detection



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
    holds = detect_holds(image)
    routes = detect_routes(image, holds)
    route = select_route(routes)

    similar_routes = find_similar_routes(route, database)



if __name__ == "__main__":
    main()