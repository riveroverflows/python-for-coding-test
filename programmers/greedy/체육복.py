def solution(n, lost, reserve):
    reserve_only = set(reserve) - set(lost)
    lost_only = set(lost) - set(reserve)

    for r in reserve_only:
        front = r - 1
        back = r + 1
        if front in lost_only:
            lost_only.remove(front)
        elif back in lost_only:
            lost_only.remove(back)

    return n - len(lost_only)


if __name__ == "__main__":
    print(solution(5, [2, 4], [1, 3, 5]))
    print(solution(5, [2, 4], [3]))
    print(solution(3, [3], [1]))
