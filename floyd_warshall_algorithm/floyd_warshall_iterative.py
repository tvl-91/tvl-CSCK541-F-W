# Floyd-Warshall Algorithm from PDF
"""Floyd Warshall Algorithm provided for Assignment."""


import itertools

def floyd(distance):
    # Alteration made to ensure Index Error is avoided in iterative_test.py
    MAX_LENGTH = num_vertices = len(distance)
    # A simple implementation of Floyd's algorithm
    for intermediate, start_node, end_node \
            in itertools.product(range(MAX_LENGTH),
                                 range(MAX_LENGTH),
                                 range(MAX_LENGTH)):
        # Assume that if start_node and end_node are the same
        # then the distance would be zero
        if start_node == end_node:
            distance[start_node][end_node] = 0
            continue
        # return all possible paths and find the minimum
        distance[start_node][end_node] = min(
            distance[start_node][end_node],
            distance[start_node][intermediate] +
            distance[intermediate][end_node])
    return distance
