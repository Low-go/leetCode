import math
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        final_output = 0
        loopCounter = 0
        increment = 0

        if len(nums) % 2 == 0:
            loopCounter += int(len(nums)/2)
        else:
            loopCounter += int(math.ceil(len(nums)/2))


        while increment < loopCounter:
            max_num = max(nums)
            max_index = nums.index(max_num)

            if max_index == 0:
                if len(nums) > 1 and nums[max_index+1] != -1:
                    final_output += max_num
                    nums[max_index] = -1
                    increment += 1
            elif max_index == len(nums) - 1:
                if len(nums) > 1 and nums[max_index-1] != -1:
                    final_output += max_num
                    nums[max_index] = -1
                    increment += 1
            else:
                if nums[max_index - 1] == -1 or nums[max_index + 1] == -1:   # what to do about u my beaut
                    nums[max_index] = -2

                else:
                    final_output += max_num
                    nums[max_index] = -1
                    increment += 1
        return final_output

    def robbery(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2


solution = Solution()
result = solution.robbery([5, 6, 4, 9, 2, 7])
print(result)



"""
chatGpt

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        return dp[n-1]

solution = Solution()
result = solution.rob([1, 2, 3, 1])
print(result)  # Output will be 4


"""


