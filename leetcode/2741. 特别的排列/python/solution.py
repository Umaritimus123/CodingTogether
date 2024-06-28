from typing import List
from functools import cache


class Solution:
    mod = 10 ** 9 + 7
    def specialPerm(self, nums: List[int]) -> int:
        @cache
        def dp(state: int, i: int) -> int:
            sub_state = state ^ (1 << i)
            if sub_state == 0:
                return 1
            return sum(dp(sub_state, j) % self.mod
                       for j, num in enumerate(nums)
                       if sub_state & (1 << j) != 0 and (num % nums[i] == 0 or nums[i] % num == 0))
        state = (1 << len(nums)) - 1 # 所有 num 都用上。
        return sum(dp(state, i) % self.mod for i in range(len(nums))) % self.mod


if __name__ == '__main__':
    nums = [2,3,6]
    print(Solution().specialPerm(nums))
