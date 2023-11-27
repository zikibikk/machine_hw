import numpy as np
import matplotlib.pyplot as plt
import random


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def random_points(n):
    points = []
    for i in range(n):
        points.append(Point(random.randint(0, 100), random.randint(0, 100)))
    return points


def dist(pointA, pointB):
    return np.sqrt((pointA.x - pointB.x) ** 2 + (pointA.y - pointB.y) ** 2)


def first_centroids(points, n):
    pointCenter = Point(0, 0)
    for elem in points:
        pointCenter.x += elem.x
        pointCenter.y += elem.y
    pointCenter.x /= len(points)
    pointCenter.y /= len(points)

    R = 0
    for elem in points:
        distCurr = dist(elem, pointCenter)
        if distCurr > R:
            R = distCurr
    centroids = []

    for i in range(n):
        centroids.append(Point(R * np.cos(2 * np.pi * i / n) + pointCenter.x,
                               R * np.sin(2 * np.pi * i / n) + pointCenter.y))

    for i in range(n):
        plt.scatter(centroids[i].x, centroids[i].y, color="r")


def show_points(points):
    for elem in points:
        plt.scatter(elem.x, elem.y, color="g")
    plt.show()


if __name__ == "__main__":
    n = 180  # кол-во кластеров
    points = random_points(100)
    first_centroids(points, n)
    show_points(points)