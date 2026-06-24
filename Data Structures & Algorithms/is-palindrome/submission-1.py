class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        for char in s:
            if char.isalnum():
                clean = clean + char.lower()
        
        left = 0
        right = len(clean) - 1
        while left < right:
            if clean[left] != clean[right]:
                return False
            else:
                left = left + 1
                right = right - 1
        return True