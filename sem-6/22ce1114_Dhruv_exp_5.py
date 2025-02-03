from queue import PriorityQueue

# Define graph with heuristic values
graph = {
    'A': [('B', 1), ('C', 3), ('D', 7)],
    'B': [('D', 5)],
    'C': [('D', 12)],
    'D': []  # Ensure 'D' is a key in the graph
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 2,
    'D': 0
}

# A* Search Algorithm
def a_star_search(graph, start, goal):
    open_list = PriorityQueue()
    open_list.put((0, start))  # (f(n), node)
    came_from = {}
    
    # Initialize g_cost for all nodes
    g_cost = {node: float('inf') for node in graph}
    g_cost[start] = 0

    while not open_list.empty():
        _, current = open_list.get()

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        for neighbor, cost in graph[current]:
            new_g = g_cost[current] + cost  # Calculate g(n)

            if new_g < g_cost.get(neighbor, float('inf')):  # Use .get() to avoid KeyError
                g_cost[neighbor] = new_g
                f_cost = new_g + heuristic[neighbor]  # f(n) = g(n) + h(n)
                open_list.put((f_cost, neighbor))
                came_from[neighbor] = current

    return None  # No path found

# Run A* Search
start_node = 'A'
goal_node = 'D'
path = a_star_search(graph, start_node, goal_node)

print("Shortest Path using A* Search:", path)
