class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda x: x[1])
        count = 0
        ref = []

        for interval in intervals:
            if len(ref) == 0:
                ref = interval
            else:
                c, d = interval
                a, b = ref

                if b > c:
                    count = count + 1
                else:
                    ref = interval

        return count