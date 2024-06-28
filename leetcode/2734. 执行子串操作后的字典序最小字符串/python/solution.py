class Solution:
    def smallestString(self, s: str) -> str:
        for i, c in enumerate(s):
            if c != 'a':
                break
        else:
            return s[: -1] + 'z'
        sub_str = []
        for j, c in enumerate(s[i:], i):
            if c == 'a':
                return s[: i] + ''.join(sub_str) + s[j:]
            sub_str.append(chr(ord(c) - 1))
        return s[: i] + ''.join(sub_str)



if __name__ == '__main__':
    s = "cbabc"
    print(Solution().smallestString(s))
