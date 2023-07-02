import random

def objective_function(x, y):
    """
    Objective function to evaluate the state.
    """
    return (1 - x)**2 + 100*(y - x**2)**2

def generate_neighbor(x, y):
    """
    Generates a random neighbor state by making a small change to the current state.
    """
    neighbor_x = x + random.uniform(-0.1, 0.1)
    neighbor_y = y + random.uniform(-0.1, 0.1)
    return neighbor_x, neighbor_y

def hill_climbing(initial_x, initial_y):
    """
    Hill Climbing algorithm implementation.
    """
    current_x = initial_x
    current_y = initial_y
    current_score = objective_function(current_x, current_y)
    
    while True:
        neighbor_x, neighbor_y = generate_neighbor(current_x, current_y)
        neighbor_score = objective_function(neighbor_x, neighbor_y)
        
        if neighbor_score < current_score:
            current_x = neighbor_x
            current_y = neighbor_y
            current_score = neighbor_score
        else:
            break
    
    return current_x, current_y, current_score

# Example usage
initial_x = random.uniform(-2, 2)
initial_y = random.uniform(-2, 2)
final_x, final_y, final_score = hill_climbing(initial_x, initial_y)
print("Final State (x, y):", final_x, final_y)
print("Final Score:", final_score)
