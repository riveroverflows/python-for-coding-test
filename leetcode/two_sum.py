from typing import List


def two_sum(nums: List[int], target: int) -> bool:
    nums_dict = dict()
    for i, num in enumerate(nums):
        nums_dict[num] = i

    for i, num in enumerate(nums):
        need = target - num
        need_index = nums_dict.get(need, None)
        i_index = nums_dict.get(num)
        if num == need and nums.count(num) == 2:
            return True
        if need_index and need_index != i_index:
            return True
    return False


print(two_sum([4, 1, 9, 7, 5, 3, 16], 14))
print(two_sum([2, 1, 5, 7], 4))
print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 2, 4], 6))
print(two_sum([3, 3], 6))
print(two_sum([3, 5, 2, 2, 3, 9], 10))
print(two_sum([3, 5, 2, 2, 1, 9], 10))
