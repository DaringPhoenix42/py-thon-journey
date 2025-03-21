def page_rank(graph, damping_factor=0.85, max_iterations=100, tolerance=1.0e-6): 
    # Initialize the number of pages 
    ranks = {page: 1 for page in graph}  # Initial rank of 1 for all pages 
    new_ranks = ranks.copy() 
    
    for iteration in range(max_iterations): 
        for page in graph: 
            incoming_links = [node for node in graph if page in graph[node]] 
            new_rank = (1 - damping_factor) + damping_factor * sum(ranks[link] / 
len(graph[link]) for link in incoming_links) 
            new_ranks[page] = new_rank 
        
        # Check for convergence 
        if all(abs(new_ranks[page] - ranks[page]) < tolerance for page in ranks): 
            break 
        
        ranks = new_ranks.copy() 
    
    return ranks 

# Define the graph based on the provided diagram 
web_graph = { 
    'A': ['B', 'C'], 
    'B': ['C'], 
    'C': ['A'] 
} 

# Compute PageRank 
page_ranks = page_rank(web_graph) 

# Print results 
print("Final PageRanks:") 
for page, rank in page_ranks.items(): 
    print(f"Page {page}: {rank:.6f}")  # ✅ Correctly indented

# Manual Calculation of Iteration 1 
initial_ranks = {'A': 1, 'B': 1, 'C': 1} 
d = 0.85 
pr_A = (1 - d) + d * (initial_ranks['C'] / 1)  # C links to A 
pr_B = (1 - d) + d * (initial_ranks['A'] / 2)  # A links to B and C 
pr_C = (1 - d) + d * ((1 / 2) + (0.575 / 1))  # A and B link to C 

print("\nIteration 1 Calculations:") 
print(f"PR(A) = {pr_A:.6f}") 
print(f"PR(B) = {pr_B:.6f}") 
print(f"PR(C) = {pr_C:.6f}")  
