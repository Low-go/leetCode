class Solution(object):
   def containsDuplicate(self, nums):
    for i in range(len(nums)):
        if nums.count(nums[i]) > 1:
            return True
        else:
            continue
    return False

solution = Solution()
result = solution.containsDuplicate([1,2,3,1])
print (result)