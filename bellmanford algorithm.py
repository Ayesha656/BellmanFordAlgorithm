# -*- coding: utf-8 -*-
"""Copy of Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Y03kNBoyU33PmncM0qyrPaS_Uxc1V5p5
"""

import time
import random
import matplotlib.pyplot as plt
import networkx as nx

class Graph:
    def __init__(self, vertices):
        self.V = vertices   # Total number of vertices in the graph
        self.graph = []      # List of edges

    def add_edge(self, s, d, w):
        self.graph.append([s, d, w])

    def print_solution(self, dist, parent):
        print("Shortest paths from the source:")
        for i in range(self.V):
            if dist[i] == float("Inf"):
                print(f"{i + 1} is unreachable from source")
            else:
                path = self.get_path(parent, i)
                path_str = " → ".join(map(str, path))
                print(f"1 → {path_str} (distance {dist[i]})")

    def get_path(self, parent, vertex):
        path = []
        while vertex != -1:
            path.append(vertex + 1)  # Convert to 1-based indexing
            vertex = parent[vertex]
        path.reverse()
        return path

    def visualize_graph(self, title):
        G = nx.DiGraph()
        for u, v, w in self.graph:
            G.add_edge(u + 1, v + 1, weight=w)  # Using 1-based indexing for visualization

        pos = nx.spring_layout(G)
        plt.figure(figsize=(8, 6))
        nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=12, font_weight='bold', edge_color='gray')
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        plt.title(title)
        plt.show()

    def bellman_ford(self, src):
        start_time = time.time()  # Start the timer

        dist = [float("Inf")] * self.V
        parent = [-1] * self.V
        dist[src] = 0  # Set the source distance to 0

        # Visualize the initial graph
        self.visualize_graph(f"Initial Graph - Source: {src + 1}")

        # Relaxation Process: For each vertex, repeat V-1 times
        for i in range(self.V - 1):
            for s, d, w in self.graph:
                if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w
                    parent[d] = s  # Record the predecessor of the vertex

            # Visualize the graph after each iteration
            self.visualize_graph(f"Graph after iteration {i + 1}")

        # Negative Cycle Detection
        for s, d, w in self.graph:
            if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                print("Graph contains negative weight cycle")
                return

        end_time = time.time()
        execution_time = end_time - start_time

        # Print the results
        self.print_solution(dist, parent)
        print(f"\nExecution Time: {execution_time:.6f} seconds")


def test_dataset_1():
    g = Graph(4)
    g.add_edge(0, 1, 5)
    g.add_edge(0, 2, 4)
    g.add_edge(1, 3, 3)
    g.add_edge(2, 1, 6)
    g.add_edge(3, 2, 2)
    print("Dataset 1 (Passes):")
    g.bellman_ford(0)

def test_dataset_2():
    g = Graph(4)
    g.add_edge(0, 1, 1)
    g.add_edge(1, 2, -1)
    g.add_edge(2, 3, -1)
    g.add_edge(3, 1, -1)
    print("\nDataset 2 (Fails):")
    g.bellman_ford(0)



def test_dataset_4():
    g = Graph(5)
    g.add_edge(0, 1, 5)
    g.add_edge(1, 2, 3)
    g.add_edge(3, 4, 2)
    print("\nDataset 4 (Disconnected Graph):")
    g.bellman_ford(0)

def test_dataset_5():
    g = Graph(5)
    g.add_edge(0, 1, -5)
    g.add_edge(1, 2, 4)
    g.add_edge(2, 3, 3)
    g.add_edge(3, 4, -2)
    print("\nDataset 5 (Negative Weight Edges but No Negative Cycle):")
    g.bellman_ford(0)

def test_dataset_6():
    g = Graph(1)
    print("\nDataset 6 (Single Vertex Graph):")
    g.bellman_ford(0)

def test_dataset_7():
    g = Graph(2)
    g.add_edge(0, 1, 7)
    print("\nDataset 7 (Single Edge Graph):")
    g.bellman_ford(0)


# Run all tests
test_dataset_1()
test_dataset_2()

test_dataset_4()
test_dataset_5()
test_dataset_6()
test_dataset_7()