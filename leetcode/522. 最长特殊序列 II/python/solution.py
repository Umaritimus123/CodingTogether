from typing import List


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        rslt = -1
        for index1, str1 in enumerate(strs):
            for index2, str2 in enumerate(strs):
                if index1 == index2: # 自己不能和自己比。
                    continue
                if len(str1) > len(str2): # 长度比对方大，肯定不是对方的子序列。
                    continue
                start = 0
                for c in str1:
                    start = str2.find(c, start) + 1
                    if start == 0: # 在考虑顺序的前提下，某字符在对方找不到，说明不是对方的子序列。
                        break
                else: # 每个字符都依次在对方找到，说明是对方的子序列。
                    break
            else: # str1不是任何其他字符串的子序列。
                rslt = max(len(str1), rslt)
        return rslt



if __name__ == '__main__':
    strs = ["aba","cdcd","eae"]
    print(Solution().findLUSlength(strs))
