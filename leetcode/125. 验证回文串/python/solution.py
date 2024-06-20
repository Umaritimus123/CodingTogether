class Solution:
    def isPalindrome(self, s: str) -> bool:
        p, q = 0, len(s)
        while p < q:
            while p < q and not s[p].isalnum():
                p += 1
            while p < q and not s[q - 1].isalnum():
                q -= 1
            if p < q:
                if s[p].lower() != s[q - 1].lower():
                    return False
                p += 1
                q -= 1
        return True


if __name__ == '__main__':
    s = "0P"
    print(Solution().isPalindrome(s))
