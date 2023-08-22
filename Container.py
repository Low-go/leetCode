from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:

        # it will always be the seccond biggest and the base
        # want to choose an optimal second height, with the biggest possible outcome
        # lenght of n will be no lower than 2

        top_height = max(height) # should return the first variable
        top_height_index = height.index(top_height) #its index number
        final = 0
        bottom = 1

        for i in range(top_height_index + 1, len(height)):

            if height[i] * bottom > final:

                final = height[i] * bottom
            bottom += 1

        return final
        # dosent work


    def maxArea2(self, height: List[int]) -> int: # time limit exceeded
        #brute force using pointers
        result = 0

        for l in range(len(height)):
            for r in range(1+ l, len(height)):
                area = (r - l) * min(height[l], height[r])
                result = max(result, area)
        return result

    def maxArea3(self, height: List[int]) -> int:

        l, r = 0, len(height) - 1
        result = 0

        while l < r:
            area = (r - l) * min(height[l], height[r])
            result = max(result, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return result






solution = Solution()
result = solution.maxArea3([4, 6, 2, 1, 5, 7])
print(result)


