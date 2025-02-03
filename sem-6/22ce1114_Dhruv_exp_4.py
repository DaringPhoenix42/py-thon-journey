# Graph representation using adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C'],
    'H': ['E']
}

# Set to track visited nodes
visited = set()

# Recursive DFS function
def dfs_recursive(node):
    if node not in visited:
        print(node, end=" ")  # Process the node
        visited.add(node)

        for neighbor in graph[node]:  # Explore neighbors
            dfs_recursive(neighbor)

# Run DFS starting from node 'A'
print("Depth-First Search Traversal (Recursive): ", end="")
dfs_recursive('A')
