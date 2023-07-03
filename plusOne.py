from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        hold = "" #converts to string
        for i in digits:
            hold += str(i)

        hold2 = str(int(hold) + 1)

        final = []
        for i in hold2:
            final.append(int(i))
        return final
