class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        countmap = {}
        orderedmap = {}

        for num in nums:
            if num in countmap:
                countmap[num] += 1
            else:
                countmap[num] = 1
        
        ordered = tuple(sorted(countmap.items(), key=lambda x: x[1], reverse=True))

        result = []

        for i in range(k):
            result.append(ordered[i][0])
        
        return result
        