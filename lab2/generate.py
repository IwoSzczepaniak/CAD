import numpy as np
import random

# Define the possible movements: (dx, dy)
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

def is_valid_move(grid, x, y):
    """
    Check if the move is valid within grid bounds and not visited yet.
    """
    rows, cols = grid.shape
    return 0 <= x < rows and 0 <= y < cols and grid[x, y] == 1

def generate_random_labyrinth(rows, cols):
    """
    Generate a labyrinth with a single random path from start to end using
    random movements while avoiding creating dead-ends or loops.
    """
    # Make sure rows and cols are odd numbers
    if rows % 2 == 0:
        rows += 1
    if cols % 2 == 0:
        cols += 1

    # Create the grid filled with walls (1)
    labyrinth = np.ones((rows, cols), dtype=int)
    
    # Start from the top-left (entrance)
    x, y = 1, 0
    labyrinth[x, y] = 0

    # Track the current path
    path_stack = [(x, y)]
    
    while len(path_stack) > 0:
        # Get the current position
        x, y = path_stack[-1]
        
        # Shuffle the directions to introduce randomness
        random.shuffle(DIRECTIONS)
        
        moved = False
        for dx, dy in DIRECTIONS:
            # Calculate the new position
            nx, ny = x + dx * 2, y + dy * 2
            
            # If valid move and the new position has not been visited yet
            if is_valid_move(labyrinth, nx, ny):
                # Carve the path (set intermediate and new position to 0)
                labyrinth[x + dx, y + dy] = 0
                labyrinth[nx, ny] = 0
                
                # Move to the new position
                path_stack.append((nx, ny))
                moved = True
                break
        
        # If no valid moves, backtrack
        if not moved:
            path_stack.pop()
    
    # Ensure there's an exit at the bottom-right
    labyrinth[rows - 2, cols - 1] = 0  # Exit at (rows-2, cols-1)
    
    return labyrinth

def save_labyrinth(labyrinth, filename):
    """
    Save the labyrinth to a file.
    """
    np.savetxt(filename, labyrinth, fmt='%d', delimiter=' ')

if __name__ == "__main__":
    # Dimensions of the labyrinth (rows x cols)
    rows, cols = 32, 32  # Ensure odd dimensions for a valid labyrinth structure
    
    # Generate the labyrinth
    labyrinth = generate_random_labyrinth(rows, cols)
    
    # Save the labyrinth to a file
    save_labyrinth(labyrinth, "labyrinth.txt")
    
    print("Random labyrinth generated and saved to labyrinth.txt")