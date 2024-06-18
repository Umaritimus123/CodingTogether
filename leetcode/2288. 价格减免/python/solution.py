import re


class Solution:
    pattern = re.compile(r'(?:(?<= )\$|^\$)(\d+(?= )|\d+$)')
    def discountPrices(self, sentence: str, discount: int) -> str:
        ratio = 1 - (discount / 100)
        return self.pattern.sub(lambda mobj: '$%.2f' % (int(mobj.group(1)) * ratio), sentence)


class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        ratio = 1 - (discount / 100)
        rslt = []
        for word in sentence.split():
            if word.startswith('$') and (value := word[1:]).isdecimal():
                value = int(value) * ratio
                rslt.append('$%.2f' % value)
            else:
                rslt.append(word)
        return ' '.join(rslt)


if __name__ == '__main__':
    sentence = "$7 there are $1 $2 and 5$ $5$ candies in the shop $7"
    discount = 50
    print(Solution().discountPrices(sentence, discount))