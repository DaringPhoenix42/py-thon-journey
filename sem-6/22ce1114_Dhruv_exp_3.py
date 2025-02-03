from collections import deque

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

# Function to implement BFS
def bfs(graph, start_node):
    visited = set()  # Set to store visited nodes
    queue = deque([start_node])  # Initialize queue with start node

    print("Breadth-First Search Traversal: ", end=" ")

    while queue:
        node = queue.popleft()  # Dequeue a node

        if node not in visited:
            print(node, end=" ")  # Process the node
            visited.add(node)  # Mark as visited

            # Add all unvisited neighbors to queue
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Run BFS starting from node 'A'
bfs(graph, 'A')
