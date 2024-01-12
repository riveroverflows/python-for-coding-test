def solution(queue1, queue2):
    q = queue1 + queue2
    n = len(queue1)
    left, mid = 0, n
    sum1, sum2 = sum(queue1), sum(queue2)

    for i in range(n * 4 + 1):
        if sum1 == sum2:
            return i
        if sum1 < sum2:
            num = q[mid]
            sum1 += num
            sum2 -= num
            mid += 1
            if mid >= n * 2:
                mid = 0
            continue
        if sum1 > sum2:
            num = q[left]
            sum1 -= num
            sum2 += num
            left += 1
            if left >= n * 2:
                left = 0
    return -1


print(solution([3, 2, 7, 2], [4, 6, 5, 1]))  # 2
print(solution([1, 2, 1, 2], [1, 10, 1, 2]))  # 7
print(solution([1, 1], [1, 5]))  # -1
