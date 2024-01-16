def solution(queue1, queue2):
    n = len(queue1)
    left, mid = 0, 0
    sum1, sum2 = sum(queue1), sum(queue2)
    q1lo, q2lo = 'l', 'r'
    for i in range(n * 4 + 1):
        if sum1 == sum2:
            return i
        if sum1 < sum2:
            num = queue2[mid] if q2lo == 'r' else queue1[mid]
            sum1 += num
            sum2 -= num
            mid += 1
            if mid >= n:
                mid = 0
                q2lo = 'l' if q2lo == 'r' else 'r'
            continue
        if sum1 > sum2:
            num = queue1[left] if q1lo == 'l' else queue2[left]
            sum1 -= num
            sum2 += num
            left += 1
            if left >= n:
                left = 0
                q1lo = 'r' if q1lo == 'l' else 'l'
    return -1


print(solution([3, 2, 7, 2], [4, 6, 5, 1]))  # 2
print(solution([1, 2, 1, 2], [1, 10, 1, 2]))  # 7
print(solution([1, 1], [1, 5]))  # -1
