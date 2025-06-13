from collections import defaultdict, deque
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class DistanceK:
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

        q.append(target)
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
        c0 = c1 = 0
        t0 = t1 = 0
        for c in s:
            if c == "0":
                t0 += 1
            else:
                t1 += 1

        rs = 0
        for c in s:
            if c == "0":
                c0 += 1
                rs += c1 * (t1 - c1)
            else:
                c1 += 1
                rs += c0 * (t0 - c0)

        return rs

