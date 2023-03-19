def two_sum(nums: list[int], target: int) -> bool:
    # 오름차순 정렬
    # left: 0 right: nums 마지막 인덱스
    # left + right == target: return
    # left + right > target: right--
    # left + right < target: left++
    right = len(nums) - 1
    left = 0
    nums.sort()
    while left != right:
        if nums[left] + nums[right] > target:
            right -= 1
            continue
        if nums[left] + nums[right] < target:
            left += 1
            continue
        if nums[left] + nums[right] == target:
            return True
    return False


print(two_sum([4, 1, 9, 7, 5, 3, 16], 14))
print(two_sum([2, 1, 5, 7], 4))
print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 2, 4], 6))
print(two_sum([3, 3], 6))
