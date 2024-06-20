from typing import List
from itertools import pairwise


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        income = 0
        for price1, price2 in pairwise(prices):
            if price2 > price1:
                income += price2 - price1
        return income

if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    print(Solution().maxProfit(prices))
