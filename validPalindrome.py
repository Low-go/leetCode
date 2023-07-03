class Solution:
    def isPalindrome(self, s: str) -> bool:
        #ok this is too easy
        newstr = ""

        for c in s:
            if c.isalnum():        # built in python method for checking if somegthing is alpan
                newstr += c.lower()
        return newstr == newstr[::-1]


#add the pointer ones next