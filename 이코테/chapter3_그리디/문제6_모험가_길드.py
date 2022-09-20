n = int(input())
levels = list(map(int, input().split()))
levels.sort()

result = 0
count = 0

for i in levels:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)
