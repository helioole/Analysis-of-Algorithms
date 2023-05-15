import timeit
import networkx as nx
import random
import matplotlib.pyplot as plt
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

def kruskal(G):
    MST = nx.Graph()
    edges = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    parent = {node: node for node in G.nodes()}
    rank = {node: 0 for node in G.nodes()}

    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    def union(node1, node2):
        root1 = find(node1)
        root2 = find(node2)
        if rank[root1] < rank[root2]:
            parent[root1] = root2
        elif rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root2] = root1
            rank[root1] += 1

    for u, v, attr in edges:
        if find(u) != find(v):
            MST.add_edge(u, v, weight=attr['weight'])
            union(u, v)

    return MST

def prim(G):
    MST = nx.Graph()
    nodes = list(G.nodes())
    start_node = nodes[0]
    visited = {node: False for node in nodes}
    distances = {node: float('inf') for node in nodes}
    previous = {node: None for node in nodes}

    distances[start_node] = 0

    while any(not visited[node] for node in nodes):
        current_node = min((node for node in nodes if not visited[node]), key=lambda x: distances[x])
        visited[current_node] = True

        if previous[current_node] is not None:
            MST.add_edge(previous[current_node], current_node, weight=G[previous[current_node]][current_node]['weight'])

        for neighbor in G[current_node]:
            weight = G[current_node][neighbor]['weight']
            if not visited[neighbor] and weight < distances[neighbor]:
                distances[neighbor] = weight
                previous[neighbor] = current_node

    return MST

inputs = [
    {
        "name": "Kruskal's Algorithm",
        "algo": lambda arr: kruskal(weighted_graph(arr)),
        "color": "b"
    },
    {
        "name": "Prim's Algorithm",
        "algo": lambda arr: prim(weighted_graph(arr)),
        "color": "r"
    }
]
plt.title('Greedy Algorithms')
plt.xlabel('Number of vertices')
plt.ylabel('Execution Time(s)')

for algo in inputs:
    elements = list()
    elements1 = list()
    start_all = timeit.default_timer()
    for i in range(1, 41):
        start = timeit.default_timer()
        a = i*25
        algo["algo"](a)
        end = timeit.default_timer()
        elements.append(a)
        elements1.append(end - start)

    plt.plot(elements, elements1, label=algo["name"], color=algo["color"])

plt.legend()
plt.show()
#
ns = [i*100 for i in range(1, 11)]
ts = [timeit.timeit('kruskal(weighted_graph({}))'.format(n),
                    globals=globals(),
                    number=1)
      for n in ns]

ts1 = [timeit.timeit('prim(weighted_graph({}))'.format(n),
                    globals=globals(),
                    number=1)
      for n in ns]

x = PrettyTable()
x.title = "Execution Time Result Table"
x.field_names = [i*100 for i in range(1, 11)]
elements1_r = np.round(ts, 5)
x.add_row(elements1_r)
elements2_r = np.round(ts1, 5)
x.add_row(elements2_r)
print(x)

