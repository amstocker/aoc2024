grid = open("day6.txt").read().splitlines()

height = len(grid)
width = len(grid[0])

start = (0, 0)
obstacles = set()
for j in range(height):
    for i in range(width):
        if grid[j][i] == '#':
            obstacles.add((i, j))
        elif grid[j][i] == '^':
            start = (i, j)

def move():
    global position
    position = next_position()

def rotate():
    global direction
    direction = (-direction[1], direction[0])

def next_position():
    return (position[0] + direction[0], position[1] + direction[1])


# Part 1
position = start
direction = (0, -1)
history = set()
while 0 <= position[0] < width and 0 <= position[1] < height:
    history.add(position)
    if next_position() in obstacles:
        rotate()
    move()
print(len(history))

# Part 2
loops_found = 0
for j in range(height):
    for i in range(width):
        if (i, j) in obstacles or (i, j) == start:
            continue
        obstacles.add((i, j))
        position = start
        direction = (0, -1)
        path = set()
        while 0 <= position[0] < width and 0 <= position[1] < height:
            if (position, direction) in path:
                print("loop found", i, j)
                loops_found += 1
                break
            path.add((position, direction))
            if next_position() in obstacles:
                rotate()
            move() 
        obstacles.remove((i, j))
print(loops_found)