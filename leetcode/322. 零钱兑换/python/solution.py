from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mem = [-1] * (amount + 1)
        mem[0] = 0
        def dp(amount: int) -> int:
            if amount < 0:
                return float('inf')
            ret = mem[amount]
            if ret != -1:
                return ret
            ret = min(dp(amount - coin) for coin in coins) + 1
            mem[amount] = ret
            return ret
        rslt = rslt if (rslt := dp(amount)) != float('inf') else -1
        return rslt


if __name__ == '__main__':
    coins = [1,2147483647]
    amount = 2
    coins = [1,2,5]
    amount = 11
    print(Solution().coinChange(coins, amount))
