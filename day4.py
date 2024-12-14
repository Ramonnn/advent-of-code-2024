with open('test.txt') as f:
    lines = f.read().splitlines()

grid = [['' for _ in range(len(lines[0])+6)] for _ in range(len(lines)+6)]

for i, line in enumerate(lines):
    for j in range(0, len(line)):
        grid[i+3][j+3] = line[j]

print(grid)

def find_xmas(grid):
    count = 0
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if grid[i][j] == 'X':
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if grid[i+x][j+y] == 'M' and grid[i+x*2][j+y*2] == 'A' and grid[i+x*3][j+y*3] == 'S':
                            count += 1
    print(count)


def find_masx(grid):
    count = 0
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if grid[i][j] == 'A':
                if (grid[i+1][j+1] == 'M' and grid[i-1][j-1] == 'S') or (grid[i+1][j+1] == 'S' and grid[i-1][j-1] == 'M'):
                    if (grid[i-1][j+1] == 'M' and grid[i+1][j-1] == 'S') or (grid[i-1][j+1] == 'S' and grid[i+1][j-1] == 'M'):
                        count += 1
    print(count)

find_xmas(grid)

find_masx(grid)
