from typing import List


class MinOperations:
    def minimumOperations(self, nums: List[int]) -> int:
        nums = list(filter(lambda x: x != 0, nums))
        return len(set(nums))

