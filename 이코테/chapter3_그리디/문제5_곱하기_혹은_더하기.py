numbers = input()
result = int(numbers[0])
for i in range(1, len(numbers)):
    num = int(numbers[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
print(result)
