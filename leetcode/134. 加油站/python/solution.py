from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = total_cost = 0
        start = 0
        for index in range(2 * len(gas) - 1):
            i = index % len(gas)
            total_gas += gas[i]
            total_cost += cost[i]
            if total_gas < total_cost:
                total_gas = total_cost = 0
                start = index + 1
                if start >= len(gas):
                    return -1
                continue
            elif (i + 1) % len(gas) == start:
                return start


if __name__ == '__main__':
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    gas = [2,3,4]
    cost = [3,4,3]
    gas = [4,5,2,6,5,3]
    cost = [3,2,7,3,2,9]
    gas = [3,1,1]
    cost = [1,2,2]
    print(Solution().canCompleteCircuit(gas, cost))