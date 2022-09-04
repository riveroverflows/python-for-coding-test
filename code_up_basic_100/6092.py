n = int(input())
a = map(int, input().split())
d = dict()
for i in a:
    d.update({i: (d.get(i, 0) + 1)})

for i in range(1, 24):
    print(d.get(i, 0), end=' ')
