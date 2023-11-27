import networkx as nx
import matplotlib.pyplot as plt
import random


if __name__ == '__main__':
    G = nx.Graph()
    n = 5
    newNodes = range(n)
    G.add_nodes_from(newNodes) # добавление вершин из массива

    edges = []
    for i in range(n):
        for j in range(i+1, n):
            if random.randint(0,1) == 1:
                edges.append((i,j, random.randint(1, 10)))
    G.add_weighted_edges_from(edges)
    nx.draw(G, with_labels = True, node_color = 'white')
    plt.show()

