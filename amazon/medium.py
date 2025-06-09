import heapq
import math
from typing import Counter, List, Optional
from collections import defaultdict, deque


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


class TreeNode:
    def __init__(self, x):
        self.val: int = x
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None


class BinaryTreeDistK:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        adj: dict[TreeNode, list[TreeNode]] = defaultdict(list)
        q: deque[TreeNode] = deque([root])
        while q:
            for _ in range(len(q)):
                n = q.popleft()
                if n.left:
                    adj[n].append(n.left)
                    adj[n.left].append(n)
                    q.append(n.left)
                if n.right:
                    adj[n].append(n.right)
                    adj[n.right].append(n)
                    q.append(n.right)

        visit = set()
        q.append(target)
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


class OrangesRotting:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        rows, cols = len(grid), len(grid[0])

        q = deque()
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        t = 0
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r+dr, c+dc
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != 1:
                        continue
                    fresh -= 1
                    grid[nr][nc] = 2
                    q.append((nr, nc))
            t += 1

        return t if fresh == 0 else -1

