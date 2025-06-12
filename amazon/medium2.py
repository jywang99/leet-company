from collections import defaultdict, deque
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BTreeDistanceK:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        adj = defaultdict(list)
        q = deque([root])
        while q:
            n = q.popleft()
            if n.left:
                adj[n].append(n.left)
                adj[n.left].append(n)
                q.append(n.left)
            if n.right:
                adj[n].append(n.right)
                adj[n.right].append(n)
                q.append(n.right)

        q = deque([target])
        visit = set()
        while q and k > 0:
            for _ in range(len(q)):
                n = q.popleft()
                visit.add(n)
                for nei in adj[n]:
                    if nei in visit:
                        continue
                    q.append(nei)
            k -= 1

        return [ n.val for n in q ]


class NumberOfWays:
    def numberOfWays(self, s: str) -> int:
        rs = 0
        t0, t1 = s.count("0"), s.count("1")
        c0, c1 = 0, 0
        for c in s:
            if c == "0":
                c0 += 1
                rs += c1 * (t1 - c1)
            else:
                c1 += 1
                rs += c0 * (t0 - c0)
        return rs


class GoodDaysToRobBank:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)

        left, right = [0] * n, [0] * n
        for i in range(1, n):
            if security[i] <= security[i-1]:
                left[i] = left[i-1] + 1
        for i in range(n-2, -1, -1):
            if security[i] <= security[i+1]:
                right[i] = right[i+1] + 1

        rs = []
        for i in range(n):
            if min(left[i], right[i]) >= time:
                rs.append(i)
        return rs


class getMaxLen:
    def getMaxLen(self, nums: List[int]) -> int:
        nlen, plen = 0, 0
        rs = 0

        for n in nums:
            if n > 0:
                plen += 1
                nlen = nlen + 1 if nlen else 0
            elif n < 0:
                plen, nlen = nlen + 1 if nlen else 0, plen + 1
            else:
                nlen = plen = 0

            rs = max(rs, plen)

        return rs

