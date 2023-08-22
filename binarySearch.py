from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:   #binarty search algorithm
        low = 0
        high = len(nums)

        while low < high:
            mid = (low + high) // 2

            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid
        if nums[low] == target:
            return low
        else:
            return -1

solution = Solution()
result = solution.search([-1, 0, 3, 5, 9, 12], 2)
print(result)
