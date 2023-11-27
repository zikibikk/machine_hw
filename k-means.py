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


def dist(pointA, pointB):
    return np.sqrt((pointA.x - pointB.x) ** 2 + (pointA.y - pointB.y) ** 2)


def point_center(points):
    pointCenter = Point(0, 0)
    for point in points:
        pointCenter.x += point.x
        pointCenter.y += point.y
    pointCenter.x /= len(points)
    pointCenter.y /= len(points)
    return pointCenter


def first_centroids(points, n):
    pointCenter = point_center(points)

    R = 0
    for elem in points:
        distCurr = dist(elem, pointCenter)
        if distCurr > R:
            R = distCurr
    centroids = []
    colors = ["red", "#88c999", "blue", "yellow", "hotpink", "orange", "purple", "beige", "brown", "gray", "cyan",
              "magenta"]

    for i in range(n):
        centroids.append(Point(R * np.cos(2 * np.pi * i / n) + pointCenter.x,
                               R * np.sin(2 * np.pi * i / n) + pointCenter.y,
                               colors[i]))

    for i in range(n):
        plt.scatter(centroids[i].x, centroids[i].y, color="black")

    for point in points:
        distance = R*R
        for centroid in centroids:
            new_dist = dist(point, centroid)
            if (new_dist < distance):
                distance = new_dist
                point.color = centroid.color
                point.distance_to_c = new_dist
    return centroids


def new_centroids(points, centroids, n):
    for centroid in centroids:
        centroid_points = []
        for point in points:
            if point.color == centroid.color:
                centroid_points.append(point)
        centroid.x = point_center(centroid_points).x
        centroid.y = point_center(centroid_points).y
    for i in range(n):
        plt.scatter(centroids[i].x, centroids[i].y, color="black")
    return repaint_points(points, centroids)


def repaint_points(points, centroids):
    counter = 0
    for point in points:
        for centroid in centroids:
            new_dist = dist(point, centroid)
            if new_dist < point.distance_to_c:
                point.distance_to_c = new_dist
                if point.color != centroid.color:
                    point.color = centroid.color
                    counter += 1
    return counter


def mean_distances(points):
    value = 0
    for point in points:
        value += point.distance_to_c
    return value


def show_points(points):
    for elem in points:
        plt.scatter(elem.x, elem.y, color=elem.color)
    # plt.show()
    plt.show(block=False)
    plt.pause(1)
    plt.close()


if __name__ == "__main__":
    # n = 2
    dists = []
    points = random_points(200)
    for n in range(1, 3, 1):
        show_points(points)
        centroids = first_centroids(points, n)
        show_points(points)
        flag = new_centroids(points, centroids, n)
        while flag > 0:
            print(flag)
            show_points(points)
            flag = new_centroids(points, centroids, n)
        dists.append(mean_distances(points))

    k=1
    n=3
    # while dists[k-2] - dists[k-1] < 1.5 * (dists[k-1] - dists[k]):
    while np.abs((dists[k-1] - dists[k])/(dists[k-2] - dists[k-1])) > 0.4:
        print(np.abs((dists[k-1] - dists[k])/(dists[k-2] - dists[k-1])))
        show_points(points)
        centroids = first_centroids(points, n)
        show_points(points)
        flag = new_centroids(points, centroids, n)
        while flag > 0:
            print(flag)
            show_points(points)
            flag = new_centroids(points, centroids, n)
        dists.append(mean_distances(points))
        k += 1
        n += 1
    print(np.abs((dists[k - 1] - dists[k]) / (dists[k - 2] - dists[k - 1])))
    n -= 1
    # show_points(points)
    plt.close()
    centroids = first_centroids(points, n)
    show_points(points)
    flag = new_centroids(points, centroids, n)
    while flag > 0:
        print(flag)
        show_points(points)
        flag = new_centroids(points, centroids, n)
    for elem in points:
        plt.scatter(elem.x, elem.y, color=elem.color)
    plt.show()
