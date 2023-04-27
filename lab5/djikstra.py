import heapq
import timeit
import networkx as nx
import random
import matplotlib.pyplot as plt
import math
import numpy as np
from prettytable import PrettyTable


def weighted_graph(num_nodes):
    G = nx.Graph()

    nodes = range(1, num_nodes + 1)
    G.add_nodes_from(nodes)

    for u in nodes:
        for v in nodes:
            if u < v:
                weight = random.randint(1, 10)
                G.add_edge(u, v, weight=weight)

    # pos = nx.spring_layout(G)
    # nx.draw(G, pos)
    # label_edge = nx.get_edge_attributes(G, 'weight')
    # nx.draw_networkx_labels(G, pos)
    # nx.draw_networkx_edge_labels(G, pos, edge_labels=label_edge)
    # plt.show()

    return G

def dijkstra(graph, start):
    distances = {node: math.inf for node in graph}
    distances[start] = 0

    pq = [(0, start)]

    visited = set()

    while pq:
        curr_distance, curr_node = heapq.heappop(pq)

        if curr_node in visited:
            continue

        visited.add(curr_node)

        for neighbor, edge_attrs in graph[curr_node].items():
            weight = edge_attrs['weight']
            new_distance = curr_distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(pq, (new_distance, neighbor))

    return distances

def floyd_warshall(graph):
    num_nodes = graph.number_of_nodes()
    dist = [[float('inf') if i != j else 0 for j in range(num_nodes)] for i in range(num_nodes)]

    for u, v, weight in graph.edges.data('weight'):
        dist[u-1][v-1] = weight
        dist[v-1][u-1] = weight

    for k in range(num_nodes):
        for i in range(num_nodes):
            for j in range(num_nodes):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


# inputs = weighted_graph(4)
# distances_d = dijkstra(inputs, 1)
# print("Dijkstra Algorithm")
# for v, w in distances_d.items():
#     print("node {}: weight: {}".format(v, w))
#
# print("\nFloyd-Warshall Algorithm")
#
# distances_f = floyd_warshall(inputs)
# for i in range(len(distances_f)):
#     for j in range(len(distances_f)):
#         if distances_f[i][j] == math.inf:
#             print("inf", end="\t")
#         else:
#             print(distances_f[i][j], end="\t")
#     print()

start_node = 1
inputs = [
    {
        "name": "Dijkstra",
        "algo": lambda arr: dijkstra(weighted_graph(arr), start_node),
        "color": "b"
    },
    {
        "name": "Floyd-Warshall",
        "algo": lambda arr: floyd_warshall(weighted_graph(arr)),
        "color": "r"
    }
]
plt.title('Dijkstra and Floyd-Warshall Algorithms')
plt.xlabel('Number of vertices')
plt.ylabel('Execution Time(s)')

for algo in inputs:
    elements = list()
    elements1 = list()
    start_all = timeit.default_timer()
    for i in range(1, 17):
        start = timeit.default_timer()
        a = i*25
        algo["algo"](a)
        end = timeit.default_timer()
        elements.append(a)
        elements1.append(end - start)

    plt.plot(elements, elements1, label=algo["name"], color=algo["color"])

plt.legend()
plt.show()

ns = [i*25 for i in range(1, 17)]
ts = [timeit.timeit('dijkstra(weighted_graph({}), start_node)'.format(n),
                    globals=globals(),
                    number=1)
      for n in ns]

ts1 = [timeit.timeit('floyd_warshall(weighted_graph({}))'.format(n),
                    globals=globals(),
                    number=1)
      for n in ns]

x = PrettyTable()
x.title = "Execution Time Result Table"
x.field_names = [i*25 for i in range(1, 17)]
elements1_r = np.round(ts, 5)
x.add_row(elements1_r)
elements2_r = np.round(ts1, 5)
x.add_row(elements2_r)
print(x)