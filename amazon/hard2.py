from collections import deque
import heapq
from typing import List


class MaximumRobots:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        cost = 0
        l, rs = 0, 0
        n = len(chargeTimes)
        q = deque()

        for r in range(n):
            cost += runningCosts[r]

            while q and chargeTimes[q[-1]] <= chargeTimes[r]:
                q.pop()
            q.append(r)

            while q and chargeTimes[q[0]] + (r - l + 1) * cost > budget:
                if q[0] == l:
                    q.popleft()
                cost -= runningCosts[l]
                l += 1

            rs = max(rs, r - l + 1)

        return rs


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
        for _ in range(k-1):
            n, i = heapq.heappop(hp)
            if i >= len(nums):
                continue

            heapq.heappush(hp, (n + nums[i], i + 1))
            if i:
                heapq.heappush(hp, (n + nums[i] - nums[i - 1], i + 1))

        return mx - hp[0][0]

