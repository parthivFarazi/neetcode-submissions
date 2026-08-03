
# Pattern: Sliding window problem but make a dictionary and don't use multiple loop, drop left, put in right

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s2) < len(s1):
            return False

        adict = {}

        for char in s1:
            if char not in adict:
                adict[char] = 1
            else:
                adict[char] += 1


        left = 0
        right = len(s1) - 1

        for i in range(right + 1):
            if s2[i] in adict:
                adict[s2[i]] -= 1

        matchedOut = True

        for val in adict.values():
            if val != 0:
                matchedOut = False

        if matchedOut:
            return True

        while right < len(s2):
            if s2[left] in adict:
                adict[s2[left]] += 1

            left = left + 1

            if right + 1 < len(s2):
                right = right + 1
            else:
                return False

            if s2[right] in adict:
                adict[s2[right]] -= 1

            matched = True

            for val in adict.values():
                if val != 0:
                    matched = False
                    break

            if matched:
                return True

        return False

# O(n) time and O(1) space
# 11 mins 52 secs