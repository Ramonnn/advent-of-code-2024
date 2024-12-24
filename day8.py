with open('test.txt') as f:
    lines = f.read().splitlines()

grid = [['' for _ in range(len(lines[0]))] for _ in range(len(lines))]

for i, line in enumerate(lines):
    for j in range(0, len(line)):
        grid[i][j] = line[j]

def find_unique(grid):
    unique = set()
    for line in grid:
        for symbol in line:
            if symbol != '.':
                unique.add(symbol)
    return unique

def find_antenna(grid):
    unique_signs = find_unique(grid)
    coordinates = {}
    for sign in unique_signs:
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == sign:
                    if not sign in coordinates:
                        coordinates[sign] = [(x, y)]
                    else:
                        coordinates[sign].append((x, y))
    return coordinates

def find_antinodes(coordinates):
    nodes = set()
    for i in range(0, len(coordinates)-1):
        for j in range(i+1, len(coordinates)):
            sub_nodes = []
            difference = (coordinates[i][0] - coordinates[j][0], coordinates[i][1] - coordinates[j][1])
            sub_nodes.append((coordinates[i][0] - difference[0], coordinates[i][1] - difference[1]))
            sub_nodes.append((coordinates[j][0] - difference[0], coordinates[j][1] - difference[1]))
            sub_nodes.append((coordinates[i][0] + difference[0], coordinates[i][1] + difference[1]))
            sub_nodes.append((coordinates[j][0] + difference[0], coordinates[j][1] + difference[1]))

            for node in sub_nodes:
                if not node == coordinates[i] and not node == coordinates[j]:
                    if 0 <= node[0] < len(grid[0]) and 0 <= node[1] < len(grid):
                        nodes.add(node)
    return nodes

#print(*grid, sep='\n')
#print(find_unique(grid))
#print(find_antenna(grid))
#print(find_antinodes([(42, 6), (31, 7), (34, 15), (47, 22)]))
#print(len(find_antinodes([(42, 6), (31, 7), (34, 15), (47, 22)])))
all_antenna = find_antenna(grid)
flat_coordinates = []
all_antinodes = set()

for coordinates in all_antenna.values():
    for coordinate in coordinates:
        flat_coordinates.append(coordinate)

for antenna, coordinates in all_antenna.items():
    antinodes = find_antinodes(coordinates)
    for antinode in antinodes:
        all_antinodes.add(antinode)

    #print(antenna, find_antinodes(coordinates))
print(all_antinodes)
print(len(all_antinodes))
