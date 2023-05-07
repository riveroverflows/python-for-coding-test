def solution(n, t, m, p):
    # n: 진법         t: 구할 숫자 개수
    # m: 참가 인원     p: 순서
    answer = ''
    digits = ''
    for i in range(t * m):
        digits += convert(i, n)
    i = p - 1
    while len(answer) < t:
        answer += digits[i]
        i += m
    return answer


def convert(n, base):
    digits = '0123456789ABCDEF'
    reversed_mod = ''
    if n == 0:
        return '0'

    while n > 0:
        n, mod = divmod(n, base)
        reversed_mod += digits[mod]

    return reversed_mod[::-1]


print(solution(2, 4, 2, 1))
print(solution(16, 16, 2, 1))
print(solution(16, 16, 2, 2))
