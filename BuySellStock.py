from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) <= 1:
            return 0

        # this is the brute force method
        # it exhausts all combinations. not ideal
        value = 0
        for i in range(0, len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] - prices[i] > value:
                    value = prices[j] - prices[i]
        return value

    #same concept but this has one loop. I copouldve literally coded the same thing but with one loop using two pointers
    def maxProfit2(self, prices: List[int]) -> int:
        l, r = 0, 1
        value = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                money = prices[r] - prices[l]
                value = max(value, money)
            else:
                l = r
            r += 1
        return value







solution = Solution()
result = solution.maxProfit2([7, 6, 4, 3, 1])
print(result)
