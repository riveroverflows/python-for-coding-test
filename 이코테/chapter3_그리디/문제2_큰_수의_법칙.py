n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
first = numbers[n - 1]
second = numbers[n - 2]

summary = 0
while m > 0:
    for i in range(k):
        if m <= 0:
            break
        summary += first
        m -= 1
    if m <= 0:
        break
    summary += second
    m -= 1

print(summary)
