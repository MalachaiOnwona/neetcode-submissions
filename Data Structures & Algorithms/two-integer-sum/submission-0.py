class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        # enumerate() keeps track of the index and
        # the value at that index as we iterate through
        # the array
        for index, num in enumerate(nums):
            # diff is equal to the a value in the 
            # hashmap that sums with the current 
            # value in the nums array to the target value
            diff = target - num
            if diff in hashmap:
                return [hashmap[diff],index]
            hashmap[num] = index
        return

        