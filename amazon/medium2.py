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

