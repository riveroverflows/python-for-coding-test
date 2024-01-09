def solution(queue1, queue2):
    n = len(queue1)
    sum1, sum2 = sum(queue1), sum(queue2)
    answer = 0
    while answer < 4 * n + 1:
        if sum1 == sum2:
            return answer
        if sum1 < sum2:
            x = queue2[0]
            del queue2[0]
            sum1 += x
            sum2 -= x
            queue1.append(x)
            answer += 1
            continue
        if sum1 > sum2:
            x = queue1[0]
            del queue1[0]
            sum1 -= x
            sum2 += x
            queue2.append(x)
            answer += 1
    return -1


print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
