h, w = map(int, input().split())
grid = [[0] * w for _ in range(h)]
n = int(input())
for _ in range(n):
    l, d, x, y = map(int, input().split())
    if d == 0:
        for i in range(y, y + l):
            grid[x - 1][i - 1] = 1
    else:
        for j in range(x, x + l):
            grid[j - 1][y - 1] = 1

for i in grid:
    for j in i:
        print(j, end=' ')
    print()
