class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq

        h = []
        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]

            dist = (x * x) + (y * y)

            if len(h) < k:
                heapq.heappush(h, (-dist, i))
            else:
                negDist, index = h[0]
                if -dist > negDist:
                    heapq.heappop(h)
                    heapq.heappush(h, (-dist, i))
        
        answer = []
        for negDist, index in h:
            answer.append(points[index])
        return answer