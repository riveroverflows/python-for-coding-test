n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()
first = numbers[n - 1]
second = numbers[n - 2]

first_count = m // (k + 1) * k + m % (k + 1)
result = first_count * first
if m - first_count > 0:
    result += (m - first_count) * second

print(result)
