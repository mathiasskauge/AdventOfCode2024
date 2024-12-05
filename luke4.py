input_file = open('test.txt', 'r')
input_lines = input_file.readlines()

# Convert to a grid of characters
grid = [list(line.strip()) for line in input_lines]

# Define all 8 possible directions (N, NE, E, SE, S, SW, W, NW)
directions = [(-1, 0), (-1, 1), (0, 1), (1, 1),
              (1, 0), (1, -1), (0, -1), (-1, -1)]

result1 = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "X":  # Check for starting letter "X"
            for dx, dy in directions:
                # Check if all indices are within bounds
                if (0 <= i + (dx * 3) < len(grid) and
                    0 <= j + (dy * 3) < len(grid[0])):
                    # Check if the next characters match "M", "A", "S"
                    if (grid[i + (1 * dx)][j + (1 * dy)] == "M" and
                        grid[i + (2 * dx)][j + (2 * dy)] == "A" and
                        grid[i + (3 * dx)][j + (3 * dy)] == "S"):
                        result1 += 1  # Increment the count

print(f"First answer: {result1}")


##########

# Define all 4 possible directions (NE, SE, SW, NW)
directions2 = [(-1, 1), (1, 1), (1, -1), (-1, -1)]

result2 = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        m_count = 0
        s_count = 0
        if grid[i][j] == "A":  # Check for starting letter "A"
            for dx, dy in directions2:
                # Check if all indices are within bounds
                if  (0 <= i + (dx) < len(grid) and 
                     0 <= j + (dy) < len(grid[0]) and 
                     0 <= i - (dx) < len(grid) and 
                     0 <= j - (dy) < len(grid[0])):
                    if grid[i + (dx)][j + (dy)] == "M" and grid[i - (dx)][j - (dy)] == "M":
                        break
                    if grid[i + (dx)][j + (dy)] == "M":
                        m_count += 1
                    if grid[i + (dx)][j + (dy)] == "S":
                        s_count += 1
        if m_count == 2 and s_count == 2:               
            result2 += 1  # Increment the count
                    
                
print(f"First answer: {result2}")
