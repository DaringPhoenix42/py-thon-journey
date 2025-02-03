from collections import defaultdict

# Define the maximum capacities of the jugs
jug1, jug2, target = 4, 3, 2  

# Dictionary to track visited states
visited = defaultdict(lambda: False)  

# BFS function to solve the water jug problem
def waterJugSolver(amt1, amt2):  
    if (amt1 == target and amt2 == 0) or (amt2 == target and amt1 == 0):
        print(f"Solution Found: ({amt1}, {amt2})")
        return True  

    # Skip if state is already visited
    if visited[(amt1, amt2)] == False:
        print(f"Current State: ({amt1}, {amt2})")  
        visited[(amt1, amt2)] = True  

        # Apply possible state transitions (as per the PDF)
        return (waterJugSolver(0, amt2) or  # Empty Jug1
                waterJugSolver(amt1, 0) or  # Empty Jug2
                waterJugSolver(jug1, amt2) or  # Fill Jug1
                waterJugSolver(amt1, jug2) or  # Fill Jug2
                waterJugSolver(amt1 - min(amt1, (jug2 - amt2)), amt2 + min(amt1, (jug2 - amt2))) or  # Pour Jug1 → Jug2
                waterJugSolver(amt1 + min(amt2, (jug1 - amt1)), amt2 - min(amt2, (jug1 - amt1))))   # Pour Jug2 → Jug1

    return False  

# Run the function with initial state (0, 0)
print("Steps:")
waterJugSolver(0, 0)
