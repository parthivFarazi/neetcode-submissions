"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.end)
        res = None

        for interval in intervals:
            if res is None:
                res = interval
            else:
                c, d = interval.start, interval.end
                a, b = res.start, res.end

                if b > c:
                    return False
                else:
                    res = interval
        
        return True
