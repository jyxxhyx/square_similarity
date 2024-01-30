import random

from shapely.geometry import MultiPoint

from output_handler.drawer import draw_two_polygons
from similartiy.similarity import calculate


def main():
    random.seed(1)
    for i in range(10):
        node_num = random.randint(15, 25)
        nodes = [(random.random(), random.random()) for _ in range(node_num)]
        polygon = MultiPoint(nodes).convex_hull
        polygon = list(polygon.exterior.coords)
        min_distance, square = calculate(polygon)
        draw_two_polygons(f'data/output/{i}', polygon, square, min_distance)
    return


if __name__ == '__main__':
    main()
