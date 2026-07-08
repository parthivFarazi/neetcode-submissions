class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        aDict = {}
        answer = 0
        left = 0
        for right in range(len(s)):

            if s[right] in aDict:
                aDict[s[right]] += 1
            else:
                aDict[s[right]] = 1
            
            maxLen = max(aDict.values())
            length = right - left + 1

            while length - maxLen > k:
                aDict[s[left]] -= 1
                left = left + 1
                length = length - 1

            answer = max(answer, length)
            
        return answer 
        