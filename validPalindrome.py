class Solution:
    def isPalindrome(self, s: str) -> bool:
        # ok this is too easy
        newstr = ""

        for c in s:
            if c.isalnum():  # built in python method for checking if somegthing is alpan
                newstr += c.lower()
        return newstr == newstr[::-1]

    # add the pointer ones next

    def isPalindrome2(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphanum(s[l]):
                l += 1
            while r > l and not self.alphanum(s[r]):
                r -= 1
            if  s[l].lower() != s[r].lower():
                 return False
            l, r = l + 1, r - 1
        return True

    def alphanum(self, c) -> bool:
        if ord(c) >= 48 and ord(c) <= 57:
            return True
        elif ord(c.lower()) >= 97 and ord(c.lower()) <= 122:
            return True
        else:
            return False


solution = Solution()
result = solution.alphanum("d")

print(result)
