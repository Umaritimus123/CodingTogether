from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p = 0
        current_num = nums[0]
        occurrence_num = 0
        for num in nums:
            if num == current_num:
                occurrence_num += 1
                if occurrence_num > 2:
                    continue
            else:
                current_num = num
                occurrence_num = 1
            nums[p] = num
            p += 1
        return p


if __name__ == '__main__':
    nums = [1,1,1,2,2,3]
    print(Solution.removeDuplicates(nums))
    print(nums)
