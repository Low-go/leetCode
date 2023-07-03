class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list = []
        if len(s) == len(t):
            for i in s:
                list.append(i)
            for j in t:
                if j in list:
                    list.remove(j)
                    continue
                else:
                    return False
            return True
        else:
            return False

    def isAnagram2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        finalS = ''.join(sorted(s))
        finalT = ''.join(sorted(t))

        if finalS == finalT:
            return True
        else:
            return False