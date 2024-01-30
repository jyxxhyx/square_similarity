import math
from typing import List, Tuple


def calculate(polygon: List[Tuple[float, float]]):
    square = _gen_closest_square(polygon)
    distance = _calculate_hausdorff_distance(polygon, square)
    return distance, square


def _gen_closest_square(polygon: List[Tuple[float, float]]):
    polygon_area = _calculate_area_shoelace(polygon)
    barycenter = _calculate_barycenter(polygon)
    square_length = math.sqrt(polygon_area)
    square = _find_best_fit_square(polygon, barycenter, square_length)
    return square


def _calculate_hausdorff_distance(polygon1, polygon2) -> float:
    max_distance = 0
    for node1 in polygon1:
        min_distance = float('inf')
        for node2 in polygon2:
            distance = math.sqrt((node2[0] - node1[0])**2 + (node2[1] - node1[1])**2)
            min_distance = min(distance, min_distance)
        max_distance = max(max_distance, min_distance)
    return max_distance


def _calculate_area_shoelace(polygon) -> float:
    area = 0
    length = len(polygon)
    for idx, node in enumerate(polygon):
        next_idx = (idx + 1) % length
        next_node = polygon[next_idx]
        area += (node[0] * next_node[1] - node[1] * next_node[0])
    return abs(area) / 2


def _calculate_barycenter(polygon):
    x, y = 0, 0
    length = len(polygon)
    for node in polygon:
        x += node[0]
        y += node[1]
    return x / length, y / length


def _find_best_fit_square(polygon, square_barycenter, square_length):
    dist_barycenter_to_corner = square_length / math.sqrt(2)
    min_dist = float('inf')
    min_node = None
    for node in polygon:
        dist = abs((node[0] - square_barycenter[0])**2 +
                   (node[1] - square_barycenter[1])**2 -
                   dist_barycenter_to_corner**2)
        if dist < min_dist:
            min_dist = dist
            min_node = node
    if min_node is None:
        raise ValueError(f'{min_node}')
    initial_direction = (min_node[0] - square_barycenter[0], min_node[1] - square_barycenter[1])
    direction_dist = math.sqrt(initial_direction[0]**2 + initial_direction[1]**2)
    normalized_direction = (initial_direction[0] / direction_dist, initial_direction[1] / direction_dist)
    square = _gen_a_square(square_barycenter, normalized_direction, dist_barycenter_to_corner)
    return square


def _gen_a_square(barycenter, direction, distance):
    node0 = (barycenter[0] + direction[0] * distance, barycenter[1] + direction[1] * distance)
    node1 = (barycenter[0] + direction[1] * distance, barycenter[1] - direction[0] * distance)
    node2 = (barycenter[0] - direction[0] * distance, barycenter[1] - direction[1] * distance)
    node3 = (barycenter[0] - direction[1] * distance, barycenter[1] + direction[0] * distance)
    return [node0, node1, node2, node3]
