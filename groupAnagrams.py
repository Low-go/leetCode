from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}  #hashmap
        finalList = []
        tempArray = []

        for i in range (len(strs)):
            if strs[i] in tempArray:
                continue
            else:
                tempArray.append(strs[i])
                minorarray = []
                minorarray.append(strs[i])
                for j in range(i+1,len(strs)):
                    if ''.join(sorted(strs[i])) == ''.join(sorted(strs[j])):
                        minorarray.append(strs[j])
                        tempArray.append(strs[j])
                finalList.append(minorarray)

        return finalList


    #Help from chatgpt this next one

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for string in strs:
            sorted_string = ''.join(sorted(string))
            anagram_map[sorted_string].append(string)

        final_list = list(anagram_map.values())

        return final_list