import heapq
from typing import List
from collections import deque


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


class MaximumRobots:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        n = len(chargeTimes)
        cost = l = 0
        ml = 0
        q = deque()
        for r in range(n):
            cost += runningCosts[r]
            while q and chargeTimes[q[-1]] <= chargeTimes[r]:
                q.pop()
            q.append(r)
            if chargeTimes[q[0]] + (r - l + 1) * cost > budget:
                if q[0] == l:
                    q.popleft()
                cost -= runningCosts[l]
                l += 1
            ml = max(ml, r - l + 1)
        return ml


class KSum:
    def kSum(self, nums: List[int], k: int) -> int:
        mx = 0
        for i, n in enumerate(nums):
            if n > 0:
                mx += n
            else:
                nums[i] = -n
        nums.sort()

        hp = [(0, 0)]
        for _ in range(k - 1):
            s, idx = heapq.heappop(hp)
            if idx >= len(nums):
                continue

            heapq.heappush(hp, (s + nums[idx], idx + 1))
            if idx:
                heapq.heappush(hp, (s + nums[idx] - nums[idx - 1], idx + 1))

        return mx - hp[0][0]


class SORTracker:
    def __init__(self):
        self.data = []
        self.cnt = 0

    def add(self, name: str, score: int) -> None:
        l, r = 0, len(self.data)
        while l < r:
            m = (l + r) // 2
            mscore, mname = self.data[m]
            if score > mscore or (score == mscore and name < mname):
                r = m
            else:
                l = m + 1
        self.data.insert(l, (score, name))

    def get(self) -> str:
        res = self.data[self.cnt][1]
        self.cnt += 1
        return res

