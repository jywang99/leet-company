from typing import List


class WordBreak2:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dp = { len(s): [""] }

        def recurse(i: int) -> List[str]:
            if i in dp:
                return dp[i]

            rs = []
            for word in wordDict:
                if s[i:].startswith(word):
                    for suf in recurse(i + len(word)):
                        rs.append((word + " " + suf).strip())

            dp[i] = rs
            return rs
        
        return recurse(0)


class NumberToWords:
    SUFS = ["", "Thousand", "Million", "Billion"]
    DIG_0 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    DIG_1 = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    DIG_TEEN = ["", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

    def two(self, n: int) -> str:
        if n == 0:
            return ""
        if 10 < n < 20:
            return self.DIG_TEEN[n - 10]
        rs = self.DIG_0[n % 10]
        n //= 10
        if not n:
            return rs
        return (self.DIG_1[n] + " " + rs).strip()

    def three(self, n: int) -> str:
        if n == 0:
            return ""
        rs = self.two(n % 100)
        n //= 100
        if n:
            rs = self.DIG_0[n] + " Hundred " + rs
        return rs.strip()

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        rs = ""
        si = 0
        while num:
            chunk = num % 1000
            cstr = self.three(chunk)
            if cstr:
                rs = cstr + " " + self.SUFS[si] + " " + rs
            num //= 1000
            si += 1

        return rs.strip()

