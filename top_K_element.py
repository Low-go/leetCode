from typing import List
class Solution:


    # my solution. Apparently its slow but memory efficient.
    def topKFrequent(self, nums:List[int], k:int) -> List[int]:

        dict = {}
        last = []


        for i in nums: # I should possess a dictionary with the elements and number of occurances
            if i not in dict:
                dict.update({i : 1})
            else:
                dict[i] += 1

        for i in range(0,k):
            max_key = max(dict, key=dict.get)
            last.append(max_key)
            dict.pop(max_key)

        return last

solution = Solution()
result = solution.topKFrequent([1,1,1,2,2,3],2)
print(result)

