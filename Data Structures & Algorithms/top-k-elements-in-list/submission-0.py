class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        aDict = {}
        for num in nums:
            if num in aDict:
                aDict[num] += 1
            else:
                aDict[num] = 1
        
        bucket = []
        for i in range(len(nums) + 1):
            bucket.append([])
        
        for key in aDict.keys():
            freq = aDict[key]
            bucket[freq].append(key)
        
        final = []
        for index in range((len(bucket)-1),0,-1):
            for num in bucket[index]:
                final.append(num)
                if len(final) == k:
                    return final