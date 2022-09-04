"""
grid = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 1, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 1, 2, 1, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
"""
grid = [list(map(int, input().split())) for _ in range(10)]
x, y = 1, 1

while x < 10 and y < 10:
    if grid[x + 1][y] == 1 and grid[x][y + 1] == 1:
        grid[x][y] = 9
        break
    if grid[x][y] == 2:
        grid[x][y] = 9
        break
    if grid[x][y] == 0:
        grid[x][y] = 9
    if grid[x][y + 1] != 1:
        y += 1
        continue
    if grid[x + 1][y] != 1:
        x += 1
        continue

for i in grid:
    for j in i:
        print(j, end=' ')
    print()
