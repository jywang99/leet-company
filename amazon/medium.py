import heapq
import math
from typing import Counter, List, Optional, cast
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


class LNode:
    def __init__(self, key: int = 0, val: int = 0) -> None:
        self.key = key
        self.val = val
        self.left: Optional[LNode] = None
        self.right: Optional[LNode] = None


class LRUCache:
    def __init__(self, capacity: int):
        self.size = 0
        self.cap = capacity
        self.map: dict[int, LNode] = {}

        self.left = LNode()
        self.right = LNode()
        self.left.right = self.right
        self.right.left = self.left

    def insert(self, n: LNode):
        prev = cast(LNode, self.right.left)
        prev.right = n
        n.left = prev
        self.right.left = n
        n.right = self.right
        self.map[n.key] = n

    def remove(self, n: LNode):
        prev = cast(LNode, n.left)
        next = cast(LNode, n.right)
        prev.right = next
        next.left = prev
        del self.map[n.key]

    def yoink(self, n: LNode):
        self.remove(n)
        self.insert(n)

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        n = self.map[key]
        self.yoink(n)
        return n.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            n = self.map[key]
            n.val = value
            self.yoink(n)
            return

        if self.size == self.cap:
            bye = cast(LNode, self.left.right)
            self.remove(bye)
        else:
            self.size += 1

        n = LNode(key, value)
        self.insert(n)


class TriangularSum:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) > 1:
            nxt = []
            for i in range(0, len(nums)-1):
                nxt.append((nums[i] + nums[i+1]) % 10)
            nums = nxt
        return nums[0]


class NumberOfWaysBuildings:
    def numberOfWays(self, s: str) -> int:
        t0 = s.count('0')
        t1 = len(s) - t0

        c0 = 0
        c1 = 0
        rs = 0

        for c in s:
            if c == "0":
                rs += c1 * (t1 - c1)
                c0 += 1
            if c == "1":
                rs += c0 * (t0 - c0)
                c1 += 1

        return rs


class GetMaxLen:
    def getMaxLen(self, nums: List[int]) -> int:
        rs = plen = nlen = 0

        for n in nums:
            if n > 0:
                plen += 1
                nlen = nlen + 1 if nlen else 0
            elif n < 0:
                plen, nlen = nlen + 1 if nlen else 0, plen + 1
            else:
                plen = nlen = 0

            rs = max(rs, plen)

        return rs


class GoodDaysToRobBank:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        if n <= time * 2:
            return []

        left, right = [0] * n, [0] * n
        for i in range(1, n):
            if security[i] <= security[i-1]:
                left[i] = left[i-1] + 1
        for i in range(n-2, -1, -1):
            if security[i] <= security[i+1]:
                right[i] = right[i+1] + 1

        return [ i for i in range(n) if min(left[i], right[i]) >= time ]

