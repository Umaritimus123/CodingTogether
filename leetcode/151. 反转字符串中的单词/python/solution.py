class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))


class Solution:
    def reverseWords(self, s: str) -> str:
        def reverse(s: list, start: int, end: int) -> None:
            p, q = start, end
            while p < q:
                s[p], s[q - 1] = s[q - 1], s[p]
                p += 1
                q -= 1
        string = []
        status = -1
        for c in s:
            if c != ' ':
                if status == 1:
                    string.append(' ')
                status = 0
                string.append(c)
            elif status != -1:
                status = 1
        string.reverse()
        start = 0
        for i, c in enumerate(string):
            if c == ' ':
                reverse(string, start, i)
                start = i + 1
        reverse(string, start, i + 1)
        return ''.join(string)


if __name__ == '__main__':
    s = "the sky is blue "
    print(Solution().reverseWords(s))
