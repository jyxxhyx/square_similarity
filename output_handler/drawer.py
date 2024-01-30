import itertools
import math

import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from matplotlib.patches import Polygon


def draw_two_polygons(file_name, polygon1, polygon2, min_distance):
    fig, ax = plt.subplots()
    # Draw two polygons
    p1 = Polygon(polygon1, fc=(0, 0, 0, 0), ec=(0, 0, 1, 0.8), lw=2)
    ax.add_artist(p1)

    p2 = Polygon(polygon2, fc=(0, 0, 0, 0), ec=(0, 0.8, 0.8, 0.8), lw=2)
    ax.add_artist(p2)

    # Draw barycenter (with text of coordinates)
    barycenter = (sum(node[0] for node in polygon1) / len(polygon1),
                  sum(node[1] for node in polygon1) / len(polygon1))

    plt.scatter(barycenter[0], barycenter[1], marker='o', color='k', s=64)
    plt.text(barycenter[0] + 0.01, barycenter[1] + 0.01,
             f'({barycenter[0]:.4f},{barycenter[1]:.4f})')

    # Draw the corners of the two polygons
    x = [node[0] for node in polygon1 + polygon2]
    y = [node[1] for node in polygon1 + polygon2]

    plt.scatter(x, y, marker='o', color='k', s=36, alpha=0.6)

    # Draw the arc corresponding to the hausdorff distance
    min_arcs = list()
    for node1, node2 in itertools.product(polygon1, polygon2):
        distance = math.sqrt((node2[0] - node1[0])**2 +
                             (node2[1] - node1[1])**2)
        if abs(distance - min_distance) < 1e-5:
            min_arcs.append((node1, node2))

    for node1, node2 in min_arcs:
        x = [node1[0], node2[0]]
        y = [node1[1], node2[1]]
        plt.plot(x, y, marker='', color='r', linewidth=3, linestyle=(0, (1, 1)))
    ax.set_xlim([-0.2, 1.2])
    ax.set_ylim([-0.2, 1.2])
    ax.axis('equal')
    # ax.set_axis_off()
    ax.set_title(f'Hausdorff dist.: {min_distance:.4f}')
    plt.margins(0, 0)
    plt.savefig('{}.jpg'.format(file_name), bbox_inches='tight', pad_inches=0)
    plt.savefig('{}.pdf'.format(file_name), bbox_inches='tight', pad_inches=0)
    return
