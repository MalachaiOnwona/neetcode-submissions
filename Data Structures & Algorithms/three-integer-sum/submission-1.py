class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Want to use a two pointer approach by sorting the 
        # array, iterating from the start of the array, then
        # having two pointers to see if the addition of all 
        # three values adds up to 0

        result = []
        nums = sorted(nums)

        for i in range(len(nums)):

            p1 = i + 1
            p2 = len(nums) - 1

            while p1 != p2 and p1 in range(len(nums)) and p2 != i:

                if nums[i] + nums[p1] + nums[p2] == 0:
                    triplet = sorted([nums[i], nums[p1], nums[p2]])

                    if triplet not in result:
                        result.append(triplet)
                    
                    p2 -= 1
                    p1 += 1
                
                elif nums[i] + nums[p1] + nums[p2] > 0:
                    p2 -= 1
                
                elif nums[i] + nums[p1] + nums[p2] < 0:
                    p1 += 1
        
        return result