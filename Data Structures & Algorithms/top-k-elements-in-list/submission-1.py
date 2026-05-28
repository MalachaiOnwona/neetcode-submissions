class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Most efficient solution: Bucket Sort Using a Hashmap
        countmap = {}

        # Frequency array of length k + 1 (account for empty frequency 0)
        frequency = [[] for i in range(len(nums) + 1)]

        for num in nums:
            countmap[num] = countmap.get(num, 0) + 1
        
        for num, count in countmap.items():
            # count is the index of the frequency array
            # Ex. index 1 includes nums that have frequency of 1
            # Ex. index 5 includes nums that have frequency of 5 
            frequency[count].append(num)
        
        result = []

        # Make sure to iterate backwards (Greatest to Least freq)
        # Formatting: range("start index, end index, increase/decrease")
        for i in range(len(frequency) - 1, 0, -1):
            for num in frequency[i]:
                result.append(num)
                if len(result) == k:
                    return result


        # My original solution
        countmap = {}
        orderedmap = {}

        for num in nums:
            countmap[num] = countmap.get(num, 0) + 1
        
        ordered = tuple(sorted(countmap.items(), key=lambda x: x[1], reverse=True))

        result = []

        for i in range(k):
            result.append(ordered[i][0])
        
        return result
        