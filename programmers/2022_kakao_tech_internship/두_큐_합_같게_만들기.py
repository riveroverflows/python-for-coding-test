from collections import deque


def solution(queue1, queue2):
    n = len(queue1)
    sum1, sum2 = sum(queue1), sum(queue2)
    deq1, deq2 = deque(queue1), deque(queue2)
    answer = 0
    while answer < 4 * n + 1:
        if sum1 == sum2:
            return answer
        if sum1 < sum2:
            x = deq2.popleft()
            sum1 += x
            sum2 -= x
            deq1.append(x)
            answer += 1
            continue
        if sum1 > sum2:
            x = deq1.popleft()
            sum1 -= x
            sum2 += x
            deq2.append(x)
            answer += 1
    return -1


print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
