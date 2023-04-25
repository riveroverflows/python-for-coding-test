from math import trunc


def solution(str1, str2):
    separated_str1 = [str1[i:i + 2].lower() for i in range(len(str1) - 1) if str1[i:i + 2].isalpha()]
    separated_str2 = [str2[i:i + 2].lower() for i in range(len(str2) - 1) if str2[i:i + 2].isalpha()]
    if not separated_str1 and not separated_str2:
        return 65536

    intersection = set(separated_str1) & set(separated_str2)
    union = set(separated_str1) | set(separated_str2)
    intersection_quantity = 0
    union_quantity = 0
    for element in intersection:
        intersection_quantity += min(separated_str1.count(element), separated_str2.count(element))
    for element in union:
        union_quantity += max(separated_str1.count(element), separated_str2.count(element))
    answer = (intersection_quantity / union_quantity) * 65536
    return trunc(answer)


print(solution("FRANCE", "french"))
print(solution("handshake", "shake hands"))
print(solution("aa1+aa2", "AAAA12"))
print(solution("E=M*C^2", "e=m*c^2"))
