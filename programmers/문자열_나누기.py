def solution(s):
    answer = 0
    x_count = 0
    other_count = 0
    x = s[0]
    i = 0
    while len(s) > 0:
        if len(s) == i:
            answer += 1
            break
        char = s[i]
        if x == char:
            x_count += 1
        else:
            other_count += 1
        if x_count == other_count:
            s = s[i + 1:]
            answer += 1
            x_count = 0
            other_count = 0
            i = 0
            if len(s) > 0:
                x = s[0]
        else:
            i += 1
    return answer


print(solution("apple"))  # 3
print(solution("aabaccgaffdfssaassgt"))  # 5
print(solution("banana"))  # 3
print(solution("pineapple"))  # 5
print(solution("abracadabra"))  # 6
print(solution("aaabbaccccabba"))  # 3
