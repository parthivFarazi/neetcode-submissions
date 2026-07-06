class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            if len(stack) <= 0 or temperatures[stack[-1]] >= temperatures[i]:
                stack.append(i)
            else:
                while len(stack) > 0 and temperatures[stack[-1]] < temperatures[i]:
                    popped = stack.pop()
                    answer[popped] = i - popped
                stack.append(i)
        return answer
        