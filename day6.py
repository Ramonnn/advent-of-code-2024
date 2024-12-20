from collections import deque
import unittest

with open('test.txt') as f:
    lines = f.read().splitlines()

grid = [['' for _ in range(len(lines[0]))] for _ in range(len(lines))]

count = 0
for i, line in enumerate(lines):
    for j in range(0, len(line)):
        grid[i][j] = line[j]
        count += 1

def find_position(grid):
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if grid[i][j] in ['<', '>', '^', 'v']:
                return i, j, grid[i][j]
    return None

def find_path(grid, i, j, direction):

    if not grid:
        print("grid is empty")
        return 0 

    path = []
    directions = deque(['>', 'v', '<', '^'])
    directions.rotate(-directions.index(direction))
    position = (i, j)
    path.append(position)

    while True:
        if directions[0] == '>' and j+1 < len(grid[i]) and grid[i][j+1] != '#':
            j += 1
            position = (i, j)
            path.append(position)

        elif directions[0] == '<' and j-1 >= 0 and grid[i][j-1] != '#':
            j -= 1
            position = (i, j)
            path.append(position)

        elif directions[0] == '^' and i-1 >= 0 and grid[i-1][j] != '#':
            i -= 1
            position = (i, j)
            path.append(position)

        elif directions[0] == 'v' and i+1 < len(grid) and grid[i+1][j] != '#':
            i += 1
            position = (i, j)
            path.append(position)

        elif (directions[0] == '>' and j+1 == len(grid[i])) or \
           (directions[0] == '<' and j-1 < 0) or \
           (directions[0] == '^' and i-1 < 0) or \
           (directions[0] == 'v' and i+1 == len(grid)):
            break
        else:
            directions.rotate(-1)

    distinct_positions = len(set(path))

    return distinct_positions

def find_infinite_path(grid, i, j, direction):

    if not grid:
        print("grid is empty")
        return 0 

    path = set()
    directions = deque(['>', 'v', '<', '^'])
    directions.rotate(-directions.index(direction))

    while True:
        position = (i, j, directions[0])
        if position in path:
            return None
        path.add(position)

        if directions[0] == '>' and j+1 < len(grid[i]) and grid[i][j+1] != '#':
            j += 1

        elif directions[0] == '<' and j-1 >= 0 and grid[i][j-1] != '#':
            j -= 1

        elif directions[0] == '^' and i-1 >= 0 and grid[i-1][j] != '#':
            i -= 1

        elif directions[0] == 'v' and i+1 < len(grid) and grid[i+1][j] != '#':
            i += 1

        elif (directions[0] == '>' and j+1 == len(grid[i])) or \
           (directions[0] == '<' and j-1 < 0) or \
           (directions[0] == '^' and i-1 < 0) or \
           (directions[0] == 'v' and i+1 == len(grid)):
            break
        else:
            directions.rotate(-1)
    return len(path)

def find_critical_positions(grid):
    """Find positions where adding obstacles causes infinite loops."""
    critical_positions = []
    start_position = find_position(grid)
    if not start_position:
        print("No starting position found.")
        return []

    start_i, start_j, direction = start_position
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            count += 1 
            if grid[i][j] == '.':
                original_value = grid[i][j]
                grid[i][j] = '#'
                result = find_infinite_path(grid, start_i, start_j, direction)
                print(f'iteration: {count} - unique positions: {result}')
                grid[i][j] = original_value

                if result is None:
                    critical_positions.append((i, j))

    return critical_positions

class TestPathFinding(unittest.TestCase):

    def test_find_position_single_direction(self):
        grid = [
            ['.', '.', '.', '>'],
            ['.', '#', '.', '.'],
            ['.', '.', '.', '.']
        ]
        i, j, direction = find_position(grid)
        self.assertEqual((i, j, direction), (0, 3, '>'))

    def test_find_position_multiple_directions(self):
        grid = [
            ['.', '<', '.', '>'],
            ['.', '^', '.', '.'],
            ['.', '.', 'v', '.']
        ]
        i, j, direction = find_position(grid)
        self.assertEqual((i, j, direction), (0, 1, '<'))  # First directional character found

    def test_find_path_clear_path(self):
        grid = [
            ['.', '.', '.', '>'],
            ['.', '.', '.', '.'],
            ['.', '.', '.', '.']
        ]
        i, j, direction = find_position(grid)
        distinct_positions = find_path(grid, i, j, direction)
        self.assertEqual(distinct_positions, 1)  # Moves immediately off the map

    def test_find_path_with_obstacles(self):
        grid = [
            ['.', '.', '#', 'v'],
            ['.', '#', '#', '.'],
            ['.', '.', '.', '#']
        ]
        i, j, direction = find_position(grid)
        distinct_positions = find_path(grid, i, j, direction)
        self.assertEqual(distinct_positions, 2)  # Can only move 2 steps before turning around

    def test_find_path_boundary_stop(self):
        grid = [
            ['>', '.', '.', '.'],
            ['.', '#', '.', '.'],
            ['.', '.', '.', '.']
        ]
        i, j, direction = find_position(grid)
        distinct_positions = find_path(grid, i, j, direction)
        self.assertEqual(distinct_positions, 4)  # Moves right until it exits

    def test_find_path_full_cycle(self):
        grid = [
            ['.', '.', '.', '.'],
            ['#', '>', '.', '#'],
            ['#', '#', '#', '#']
        ]
        i, j, direction = find_position(grid)
        distinct_positions = find_path(grid, i, j, direction)
        self.assertEqual(distinct_positions, 3)  # Moves right, returns, and exits at the top

if __name__ == '__main__':
    critical_positions = find_critical_positions(grid)
    print(len(critical_positions))

    unittest.main()


