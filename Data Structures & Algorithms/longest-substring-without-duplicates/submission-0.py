class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maxLen = 0
        seen = set()
        for right in range(len(s)):
            if s[right] not in seen:
                seen.add(s[right])
            else:
                while s[right] in seen:
                    seen.remove(s[left])
                    left = left + 1
                seen.add(s[right])
            maxLen = max(maxLen, right - left + 1)
        return maxLen
        
        