import time

import numpy as np
import matplotlib.pyplot as plt
import random

class Point:
    def __init__(self, x, y, color="g", distance_to_c=0):
        self.x = x
        self.y = y
        self.color = color
        self.distance_to_c = distance_to_c


def random_points(n):
    points = []
    for i in range(n):
        points.append(Point(random.randint(0, 100), random.randint(0, 100)))
    return points


if __name__ == "__main__":
    points = random_points(100)
    for elem in points:
        plt.scatter(elem.x, elem.y, color="g")
    plt.show()
    for elem in points:
        plt.scatter(elem.x, elem.y, color="y")
    time.sleep(5)
    plt.draw()