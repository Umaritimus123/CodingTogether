from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p = 1
        for index, num in enumerate(nums[1:], start=1):
            if num == nums[index - 1]:
                continue
            nums[p] = num
            p += 1
        return p