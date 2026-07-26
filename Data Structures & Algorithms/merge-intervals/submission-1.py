class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        answer = []

        for interval in intervals:
            if len(answer) == 0:
                answer.append(interval)
            else:
                c, d = interval
                a, b = answer[-1]

                if c > b:
                    answer.append(interval)
                else:
                    temp = [min(a, c), max(b, d)]
                    answer.pop()
                    answer.append(temp)

        return answer