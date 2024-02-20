# Test cases for Algorithm by Taras
# Cases evaluates the Floyd-Warshall Algorithm's performance
# on graphs with 4 & 8 vertices.
# Aim is to validate correctness.
"""
Contains different test cases for the floyd warshall algorithm
function. Function works for all graph types. Below are expected
inputs and outputs for each.
"""

# inf denotes edges that don't exist.
inf = float('inf')

# Test A: 4 Vertices Small Graphs
""" Floyd Warshall in Python (with Pseudocode)
 Author: Yujian Tang
 Date: 17/02/2022
 Available at: https://pythonalgos.com/
 """

# sample_a, showing absence of edges (inf) and weights representing distance between vertices:
sample_a = [[0, 5, inf, inf],
            [50, 0, 15, 5],
            [30, inf, 0, 15],
            [15, inf, 5, 0]]

# Expected output for sample_a, showing the shortest distance from vertex i to j:
output_a = [[0, 5, 15, 10],
            [20, 0, 10, 5],
            [30, 35, 0, 15],
            [15, 20, 5, 0]]

# sample_b, showing absence of edges (inf) and weights representing distance between vertices:
sample_b = [[0, 3, inf, 5],
            [2, 0, inf, 4],
            [inf, 1, 0, inf],
            [inf, inf, 2, 0]]

# Expected output for sample_b, showing the shortest distance from vertex i to j:
output_b = [[0, 3, 7, 5],
            [2, 0, 6, 4],
            [3, 1, 0, 5],
            [5, 3, 2, 0]]

# Test B: 8 Vertices Large Graphs

# sample_c, showing absence of edges (inf) and weights representing distance between vertices:
sample_c = [[0, 5, 2, inf, inf, inf, inf, inf],
            [5, 0, inf, 7, 1, inf, inf, inf],
            [2, inf, 0, 4, inf, inf, 8, inf],
            [inf, 7, 4, 0, inf, 3, inf, inf],
            [inf, 1, inf, inf, 0, 6, inf, inf],
            [inf, inf, inf, 3, 6, 0, inf, 2],
            [inf, inf, 8, inf, inf, inf, 0, 10],
            [inf, inf, inf, inf, inf, 2, 10, 0]]

# Expected output for sample_c, showing the shortest distance from vertex i to j:
output_c = [[0, 5, 2, 6, 6, 9, 10, 11],
            [5, 0, 7, 7, 1, 7, 15, 9],
            [2, 7, 0, 4, 8, 7, 8, 9],
            [6, 7, 4, 0, 8, 3, 12, 5],
            [6, 1, 8, 8, 0, 6, 16, 8],
            [9, 7, 7, 3, 6, 0, 12, 2],
            [10, 15, 8, 12, 16, 12, 0, 10],
            [11, 9, 9, 5, 8, 2, 10, 0]]


# sample_d, showing absence of edges (inf) and weights representing distance between vertices:
sample_d = [[0, 3, inf, inf, inf, inf, 8, inf],
            [3, 0, 5, inf, inf, inf, inf, inf],
            [inf, 5, 0, 2, 7, inf, inf, inf],
            [inf, inf, 2, 0, inf, 4, inf, inf],
            [inf, inf, 7, inf, 0, 1, inf, inf],
            [inf, inf, inf, 4, 1, 0, 6, 5],
            [8, inf, inf, inf, inf, 6, 0, 4],
            [inf, inf, inf, inf, inf, 5, 4, 0]]

# Expected output for sample_d, showing the shortest distance from vertex i to j:
output_d = [[0, 3, 8, 10, 15, 14, 8, 12],
            [3, 0, 5, 7, 12, 11, 11, 15],
            [8, 5, 0, 2, 7, 6, 12, 11],
            [10, 7, 2, 0, 5, 4, 10, 9],
            [15, 12, 7, 5, 0, 1, 7, 6],
            [14, 11, 6, 4, 1, 0, 6, 5],
            [8, 11, 12, 10, 7, 6, 0, 4],
            [12, 15, 11, 9, 6, 5, 4, 0]]

# sample_e is a negative graph, showing absence of edges (inf)
# and weights representing distance between vertices:
sample_e = [[0, 5, inf, inf],
            [3, 0, -4, inf],
            [inf, inf, 0, -6],
            [2, inf, inf, 0]]

# Expected output for sample_e, showing the shortest distance from vertex i to j:
output_e = [[0, 2, -2, -5],
            [-8, 0, -7, -10],
            [-4, 1, 0, -6],
            [2, 7, 3, 0]]

# sample_f is a negative graph, showing absence of edges (inf)
# and weights representing distance between vertices:
sample_f = [[0, 2, 4, inf],
            [-3, 0, 2, inf],
            [inf, -1, 0, 5],
            [inf, inf, -2, 0]]

# Expected output for sample_f, showing the shortest distance from vertex i to j:
output_f = [[0, 2, 3, 8],
            [-3, 0, 1, 6],
            [-4, -1, 0, 5],
            [-6, -3, -2, 0]]
