import sys

import networkx as nx
import matplotlib.pyplot as plt
import random


def generate_graph(n=5, max_weight=10):
    g = nx.Graph()
    nodes = range(n)
    g.add_nodes_from(nodes)
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            edges.append((i, j, random.randint(1, max_weight)))
    g.add_weighted_edges_from(edges)
    return g


def draw(graph):
    print(graph)
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, edge_color="blue")
    edge_labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_color='blue')
    plt.show()


def find_lonely_nodes(graph):
    isolated_nodes = []
    for node in graph.nodes():
        if not list(graph.neighbors(node)):
            isolated_nodes.append(node)
    return isolated_nodes


def add_edge(new_graph, edge):
    new_graph.add_weighted_edges_from([(edge[0], edge[1], edge[2]['weight'])])
    return new_graph


def min_weight_edge(graph):
    min_weight = sys.maxsize
    min_weight_edge = 0
    for u, v, data in graph.edges(data=True):
        if 'weight' in data and data['weight'] < min_weight:
            min_weight = data['weight']
            min_weight_edge = (u, v, data)
    return min_weight_edge


def max_weight_edge(graph):
    max_weight = 0
    max_weight_edge = 0
    for u, v, data in graph.edges(data=True):
        if 'weight' in data and data['weight'] > max_weight:
            max_weight = data['weight']
            max_weight_edge = (u, v, data)
    return max_weight_edge


def shortest_path(graph, num_of_clusters):
    result = nx.Graph()
    result.add_nodes_from(graph.nodes)
    # draw(result)
    min_edge = min_weight_edge(graph)
    result = add_edge(result, min_edge)
    # draw(result)
    joined_nodes = [min_edge[0], min_edge[1]]
    isolated_nodes = find_lonely_nodes(result)
    while len(isolated_nodes) > 0:
        min_weight = sys.maxsize
        min_edge = 0
        for isolated in isolated_nodes:
            for joined in joined_nodes:
                data = graph.get_edge_data(isolated, joined)
                weight = data['weight']
                if weight < min_weight:
                    min_weight = weight
                    min_edge = (isolated, joined, data)
        if min_edge == 0:
            return
        result = add_edge(result, min_edge)
        joined_nodes.append(min_edge[0])
        isolated_nodes.remove(min_edge[0])
        # draw(result)
    draw(result)
    for i in range(num_of_clusters - 1):
        max_edge = max_weight_edge(result)
        result.remove_edge(max_edge[0], max_edge[1])
        # draw(result)
    draw(result)
    return result


if __name__ == "__main__":
    graph = generate_graph(5, 7)
    draw(graph)
    num_of_clusters = 4
    new_g = shortest_path(graph, num_of_clusters)
