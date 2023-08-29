from typing import List


class Solution:

    # i got a time limit exceded on this one
    def productExceptSelf(self, nums: List[int]):
        final_array = []
        counter = 0
        pointer = 0
        copy = nums.copy()
        value = 1

        while counter < len(nums):

            copy.pop(counter)

            if pointer >= len(copy):
                final_array.append(value)
                value = 1
                pointer = 0
                counter += 1
                copy = nums.copy()

            else:
                value *= copy[pointer]
                pointer += 1
                copy = nums.copy()

        return final_array

    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        output = [1] * (len(nums)) # an array with the length of nums, inside each array is a value of 1

        prefix = 1
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) -1,-1,-1):
            output[i] *= postfix
            postfix *= nums[i]
        return output



hold = [1, 2, 3, 4]
solution = Solution()
result = solution.productExceptSelf(hold)

word = "anagram"
word2 = "nagaram"
result2 = solution.isAnagram(word, word2)
print(result2)

