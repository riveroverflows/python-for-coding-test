def solution(n, lost, reserve):
    students = [0] * (n + 2)
    for r in reserve:
        students[r] += 1
    for l in lost:
        students[l] -= 1

    for i in range(1, n + 1):
        if students[i] > 0:
            front = i - 1
            back = i + 1
            if students[front] < 0:
                students[front] += 1
                students[i] -= 1
            elif students[back] < 0:
                students[back] += 1
                students[i] -= 1
    answer = 0
    for s in students:
        if s >= 0:
            answer += 1

    return answer - 2


if __name__ == "__main__":
    print(solution(5, [2, 4], [1, 3, 5]))
    print(solution(5, [2, 4], [3]))
    print(solution(3, [3], [1]))
