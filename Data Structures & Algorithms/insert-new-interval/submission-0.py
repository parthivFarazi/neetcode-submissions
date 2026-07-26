class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        answer = []
        isMerged = False

        for interval in intervals:
            c, d = interval
            a, b = newInterval

            if d < a:
                answer.append(interval)

            elif d >= a and c <= b:
                newInterval = [min(a, c), max(b, d)]

            elif c > b:
                if not isMerged:
                    answer.append(newInterval)
                    isMerged = True
                answer.append(interval)

        if not isMerged:
            answer.append(newInterval)

        return answer