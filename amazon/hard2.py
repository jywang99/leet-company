from collections import deque
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

