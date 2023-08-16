class Solution:
    def reverseBits(self, n: int) -> int:

        bit = format(n, '032b')
        reverse = bit[::-1]
        return int(reverse, 2)





solution = Solution()
hold = 0b00000010100101000001111010011100
result = solution.reverseBits(hold)
print(result)