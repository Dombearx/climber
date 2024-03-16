from pathlib import Path
from dataclasses import dataclass
from PIL.Image import Image
from typing import List

@dataclass
class Point:
    x: int
    y: int

@dataclass
class Hold:
    bounding_box: List[Point]
    dominant_color: List[int]

@dataclass
class Route:
    holds: List[Hold]

def read_image(image_path: Path) -> Image:
    raise NotImplementedError

def detect_holds(image: Image) -> List[Hold]:
    raise NotImplementedError

def detect_routes(image: Image, holds: List[Hold]) -> List[Route]:
    raise NotImplementedError

def select_route(routes: List[Route]) -> Route:
    raise NotImplementedError

def find_similar_routes(route: Route, database) -> List[Route]:
    raise NotImplementedError

def main():
    image_path = Path("")
    database = Path("")
    image = read_image(image_path)
    holds = detect_holds(image)
    routes = detect_routes(image, holds)
    route = select_route(routes)

    similar_routes = find_similar_routes(route, database)



if __name__ == "__main__":
    main()