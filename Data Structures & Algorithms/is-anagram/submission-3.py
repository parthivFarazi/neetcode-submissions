class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        inDict = {}
        for letter in s:
            if letter in inDict:
                inDict[letter] += 1
            else:
                inDict[letter] = 1
        
        for letter in t:
            if letter not in inDict or inDict[letter] <= 0:
                return False
            else:
                inDict[letter] -= 1
        
        return True