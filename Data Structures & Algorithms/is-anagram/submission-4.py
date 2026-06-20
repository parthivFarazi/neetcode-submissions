class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sFixed = "".join(sorted(s))
        tFixed = "".join(sorted(t))

        return sFixed == tFixed