grid = open("day4.txt").read().splitlines()

height = len(grid)
width = len(grid[0])


# Part 1
directions = [
    [(0, 0), (0, 1),   (0, 2),   (0, 3)],  
    [(0, 0), (1, 1),   (2, 2),   (3, 3)],  
    [(0, 0), (1, 0),   (2, 0),   (3, 0)],  
    [(0, 0), (1, -1),  (2, -2),  (3, -3)], 
    [(0, 0), (0, -1),  (0, -2),  (0, -3)], 
    [(0, 0), (-1, -1), (-2, -2), (-3, -3)],
    [(0, 0), (-1, 0),  (-2, 0),  (-3, 0)], 
    [(0, 0), (-1, 1),  (-2, 2),  (-3, 3)]  
]

count = 0
for j in range(height):
    for i in range(width):
        for d in directions:
            if      0 <= i+d[0][0] < width and 0 <= j+d[0][1] < height and grid[j+d[0][1]][i+d[0][0]] == 'X' \
                and 0 <= i+d[1][0] < width and 0 <= j+d[1][1] < height and grid[j+d[1][1]][i+d[1][0]] == 'M' \
                and 0 <= i+d[2][0] < width and 0 <= j+d[2][1] < height and grid[j+d[2][1]][i+d[2][0]] == 'A' \
                and 0 <= i+d[3][0] < width and 0 <= j+d[3][1] < height and grid[j+d[3][1]][i+d[3][0]] == 'S':
                count += 1
print(count)


# Part 2
patterns = [
    { 'M': [(0, 0), (2, 0)], 'A': [(1, 1)], 'S': [(2, 2), (0, 2)] },
    { 'M': [(2, 0), (2, 2)], 'A': [(1, 1)], 'S': [(0, 2), (0, 0)] },
    { 'M': [(2, 2), (0, 2)], 'A': [(1, 1)], 'S': [(0, 0), (2, 0)] },
    { 'M': [(0, 2), (0, 0)], 'A': [(1, 1)], 'S': [(2, 0), (2, 2)] }
]

count = 0
for j in range(height - 2):
    for i in range(width - 2):
        for pattern in patterns:
            for symbol, coords in pattern.items():
                for c in coords:
                    if not grid[j+c[1]][i+c[0]] == symbol:
                        break
                else:
                    continue
                break
            else:
                count += 1
print(count)
