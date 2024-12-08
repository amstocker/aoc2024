data = open("day8.txt").read().splitlines()

height = len(data)
width = len(data[0])

nodes: dict[str, list[tuple[int, int]]] = dict()
for j in range(height):
    for i in range(width):
        symbol = data[j][i]
        if symbol == '.':
            continue
        if symbol in nodes:
            nodes[symbol].append((i, j))
        else:
            nodes[symbol] = [(i, j)]


# Part 1
antinodes: set[tuple[int, int]] = set()
for coords in nodes.values():
    for n in range(len(coords)):
        for m in range(n + 1, len(coords)):
            delta = (coords[m][0] - coords[n][0], coords[m][1] - coords[n][1])
            antinode1 = (coords[n][0] - delta[0], coords[n][1] - delta[1])
            antinode2 = (coords[m][0] + delta[0], coords[m][1] + delta[1])
            if 0 <= antinode1[0] < width and 0 <= antinode1[1] < height:
                antinodes.add(antinode1)
            if 0 <= antinode2[0] < width and 0 <= antinode2[1] < height:
                antinodes.add(antinode2)
print(len(antinodes))

# Part 2
antinodes = set()
for coords in nodes.values():
    for n in range(len(coords)):
        for m in range(n + 1, len(coords)):
            delta = (coords[m][0] - coords[n][0], coords[m][1] - coords[n][1])
            coord = coords[m]
            while 0 <= coord[0] < width and 0 <= coord[1] < height:
                antinodes.add(coord)
                coord = (coord[0] + delta[0], coord[1] + delta[1])
            coord = coords[n]
            while 0 <= coord[0] < width and 0 <= coord[1] < height:
                antinodes.add(coord)
                coord = (coord[0] - delta[0], coord[1] - delta[1])
print(len(antinodes))