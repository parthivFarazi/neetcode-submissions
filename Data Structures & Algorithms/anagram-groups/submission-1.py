class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        inDict = {}
        final = []
        count = 0
        for word in strs:
            fixed = "".join(sorted(word))
            if fixed in inDict:
                final[inDict[fixed]].append(word)
            else:
                final.append([word])
                inDict[fixed] = count
                count += 1
        return final
        