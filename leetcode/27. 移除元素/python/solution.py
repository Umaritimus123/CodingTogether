from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p = 0
        for num in nums:
            if num != val:
                nums[p] = num
                p += 1
        return p


if __name__ == '__main__':
    nums = [3,2,2,3]
    val = 3
    Solution().removeElement(nums, val)
