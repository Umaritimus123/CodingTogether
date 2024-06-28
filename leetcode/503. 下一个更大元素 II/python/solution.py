from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        max_num_index = 0
        for i, num in enumerate(nums):
            if num > nums[max_num_index]:
                max_num_index = i
        start = max_num_index
        stack = []
        result = [0] * len(nums)
        for i in range(start, start + len(nums)):
            i %= len(nums)
            num = nums[i]
            while len(stack) > 0 and num > nums[stack[-1]]:
                result[stack.pop()] = num
            stack.append(i)
        first_stack_num = nums[stack[0]]
        for index in stack:
            result[index] = first_stack_num if nums[index] < first_stack_num else -1
        return result


if __name__ == '__main__':
    nums = [1,2,3,2,1]
    nums = [1,2,1]
    nums = [5,4,3,2,1]
    print(Solution().nextGreaterElements(nums))
