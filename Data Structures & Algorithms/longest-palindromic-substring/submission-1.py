class Solution:
    def longestPalindrome(self, s: str) -> str:
            answer = ""

            for i in range((2 * len(s)) - 1):

                if i % 2 == 0:
                    left = i // 2
                    right = i // 2
                else:
                    left = (i - 1) // 2
                    right = (i + 1) // 2


                while left >= 0 and right < len(s):

                    if s[left] == s[right]:
                        left = left - 1
                        right = right + 1
                    else:
                        break

                if right - left - 1 > len(answer):
                    answer = s[left + 1 : right]

            return answer