class Solution:
    def isValid(self, s: str) -> bool:
        aDict = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char not in aDict.keys():
                stack.append(char)
            else:
                if len(stack) > 0:
                    x = stack.pop()
                    if x != aDict[char]:
                        return False
                else:
                    return False
        return len(stack) == 0
            