def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        number = bin(i | j)[2:]
        number = number.zfill(n)
        number = number.replace("1", "#")
        number = number.replace("0", " ")
        answer.append(number)
    return answer


print(solution(n=5, arr1=[9, 20, 28, 18, 11], arr2=[30, 1, 21, 17, 28]))
print(solution(n=6, arr1=[46, 33, 33, 22, 31, 50], arr2=[27, 56, 19, 14, 14, 10]))
