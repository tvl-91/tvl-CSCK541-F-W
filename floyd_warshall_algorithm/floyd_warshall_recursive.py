# Floyd-Warshall Algorithm Recursion in Python by Taras

"""Floyd-Warshall Algorithm that executes recursively."""
# Geeksforgeeks.com step by step illustration
# Programiz.com for more understanding

# Define function & calculate the number of vertices
def floyd_warshall(dist):
    num_vertices = len(dist)

    # find shortest distance i and j through k
    def shortest_path(i, j, k):
        # Check for intermediary vertices for path i to j
        if k == -1:
            return dist[i][j]
        # If no intermediary vertices, create shortest distance i and j
        # considering all paths.
        return min(shortest_path(i, j, k - 1),
                   shortest_path(i, k, k - 1) + shortest_path(k, j, k - 1))

    # update distance between i and j, with k as shortest distance
    def updatedist(k):
        if k == num_vertices: # checks that all intermediary vertices have been considered
            return
        # shortest path computed with k considered
        for i in range(num_vertices):
            for j in range(num_vertices):
                dist[i][j] = shortest_path(i, j, k)
        updatedist(k+1) # function continues until k reaches num_vertices

    updatedist(0)

    return dist
