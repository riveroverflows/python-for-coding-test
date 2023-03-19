def two_sum(nums: list[int], target: int) -> list[int]:
    nums_length = len(nums)
    # nums 길이 만큼 반복.
    for i in range(nums_length):
        for j in range(i + 1, nums_length):
            # 원소들끼리 더했을 때 target이랑 일치하는지 확인
            if nums[i] + nums[j] == target:
                # 일치하면 인덱스 반환
                return [i, j]


print(two_sum([4, 1, 9, 7, 5, 3, 16], 14))
print(two_sum([2, 1, 5, 7], 4))
print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 2, 4], 6))
print(two_sum([3, 3], 6))
