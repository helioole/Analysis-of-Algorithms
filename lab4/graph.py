import networkx as nx
import matplotlib.pyplot as plt
import random
import timeit

import numpy as np
from prettytable import PrettyTable


def balanced(num_vertices):
    G = nx.complete_graph(num_vertices)

    num_edges = num_vertices * (num_vertices - 1) // 4

    for i, (u, v) in enumerate(G.edges()):
        if i >= num_edges:
            G.remove_edge(u, v)
            break

    return G


def unbalanced(num_vertices):
    G = nx.Graph()
    G.add_nodes_from(range(num_vertices))

    for u in range(num_vertices):
        num_edges = random.randint(0, num_vertices-1)
        for _ in range(num_edges):
            v = random.randint(0, num_vertices-1)
            if u != v:
                G.add_edge(u, v)

    return G

def dfs(G, start_node, visited=None):
    if visited is None:
        visited = set()
    visited.add(start_node)
    print(start_node)

    for neighbor in G.neighbors(start_node):
        if neighbor not in visited:
            dfs(G, neighbor, visited)

def bfs(G, start_node):
    visited = set()
    queue = [start_node]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(node)
            visited.add(node)
            for neighbor in G.neighbors(node):
                queue.append(neighbor)

first_node = 0

inputs = [
    {
        "name": "BFS",
        "algo": lambda arr: bfs(balanced(arr), first_node),
        "color": "b"
    },
    {
        "name": "DFS",
        "algo": lambda arr: dfs(balanced(arr), first_node),
        "color": "r"
    }
]
plt.title('Balanced Graph')
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
ts = [timeit.timeit('bfs(unbalanced({}), first_node)'.format(n),
                    globals=globals(),
                    number=1)
      for n in ns]

ts1 = [timeit.timeit('dfs(unbalanced({}), first_node)'.format(n),
                    globals=globals(),
                    number=1)
      for n in ns]

plt.plot(ns, ts, '-b', marker='o', label = 'BFS')
plt.plot(ns, ts1, '-r', marker='o', label = 'DFS')
plt.show()

x = PrettyTable()
x.title = "Unbalanced Graph"
x.field_names = [i*25 for i in range(1, 17)]
elements1_r = np.round(ts, 5)
x.add_row(elements1_r)
elements2_r = np.round(ts1, 5)
x.add_row(elements2_r)
print(x)

inputs = [
    {
        "name": "BFS",
        "algo": lambda arr: bfs(unbalanced(arr), first_node),
        "color": "b"
    },
    {
        "name": "DFS",
        "algo": lambda arr: dfs(unbalanced(arr), first_node),
        "color": "r"
    }
]
plt.title('Unbalanced Graph')
plt.xlabel('Number of vertices')
plt.ylabel('Execution Time(s)')

for algo in inputs:
    elements = list()
    elements1 = list()
    start_all = timeit.default_timer()
    for i in range(1, 81):
        start = timeit.default_timer()
        a = i*5
        algo["algo"](a)
        end = timeit.default_timer()
        elements.append(a)
        elements1.append(end - start)

    plt.plot(elements, elements1, label=algo["name"], color=algo["color"])

plt.plot(ns, ts, '-b', marker='o', label = 'BFS')
plt.plot(ns, ts1, '-r', marker='o', label = 'DFS')
plt.show()
