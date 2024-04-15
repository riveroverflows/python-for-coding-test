grid = [[0] * 19 for _ in range(19)]
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    grid[x - 1][y - 1] = 1

for i in grid:
    for j in i:
        print(j, end=" ")
    print()
