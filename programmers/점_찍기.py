from math import sqrt


def solution(k, d):
    answer = 0
    # for 풀이
    for x in range(0, d + 1, k):
        y = sqrt(d * d - x * x)
        count = y // k + 1
        answer += count
    # while 풀이
    # x = 0
    # while x <= d:
    #     y = sqrt(d * d - x * x)
    #     answer += y // k + 1
    #     x += k
    return int(answer)


print(solution(2, 4))
print(solution(1, 5))
