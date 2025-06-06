import heapq
import math
from typing import Counter, List, Optional
from collections import defaultdict


class Node:
    def __init__(self, x: int, next: Optional['Node'] = None, random: Optional['Node'] = None):
        self.val = int(x)
        self.next: Optional[Node] = next
        self.random: Optional[Node] = random


class CopyRandomList:
    def copyRandomList(self, head: Optional['Node']) -> Optional['Node']:
        doppel = defaultdict(lambda: Node(0))
        doppel[None] = None # type: ignore
        n = head
        while n:
            clone = doppel[n]
            clone.val = n.val
            clone.random = doppel[n.random]
            clone.next = doppel[n.next]
            n = n.next
        return doppel[head]
        

class ReorganizeString:
    def reorganizeString(self, s: str) -> str:
        cnt = Counter(s)
        hp = []
        for c, n in cnt.items():
            heapq.heappush(hp, (-n, c))

        if hp and -hp[0][0] > math.ceil(len(s) / 2):
            return ""

        cd = None
        rs = ""
        while hp:
            n, c = heapq.heappop(hp)
            rs += c

            if cd:
                heapq.heappush(hp, cd)
                cd = None

            n += 1
            if n != 0:
                cd = (n, c)

        return rs


class WordBreak2:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dp = { len(s): [""] }

        def recurse(i: int, s: str) -> List[str]:
            if i in dp:
                return list(map(lambda suf: s + " " + suf, dp[i]))

            rs = []
            for word in wordDict:
                if s[i].startswith(word):
                    rs.append(recurse(i + len(word), s + " " + word))
            dp[i] = rs

