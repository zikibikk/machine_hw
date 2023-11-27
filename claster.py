import matplotlib.pyplot as plt
import numpy as np
import random

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def random_points(n):
    points = []
    for a in range(n):
        points.append(Point(random.randint(0, 100), random.randint(0, 100)))
    return points

def draw_points(points):
    for point in points:
        plt.scatter(point.x, point.y, color = 'g')
    plt.show()

def find_center(points):
    pointC = 0, 0
    x_c, y_c = 0, 0
    for point in points:
        x_c += point.x
        y_c += point.y
    x_c /=len(points)
    y_c /=len(points)
    R = 0
    for point in points:
        distCurr = np.dist(point, pointC)
        if(np.dist > R):
            max_dist = distCurr
        centroids = []


if __name__ == "__main__":
    points = random_points(123)
    draw_points(points)