class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Want to use a two pointer approach by sorting the 
        # array, iterating from the start of the array, then
        # having two pointers to see if the addition of all 
        # three values adds up to 0
        #
        # Handle/Move pointers based on summation of the three 
        # elements

        result = []
        nums = sorted(nums)

        for i in range(len(nums)):

            p1 = i + 1
            p2 = len(nums) - 1

            while p1 < p2:

                if nums[i] + nums[p1] + nums[p2] == 0:
                    triplet = [nums[i], nums[p1], nums[p2]]

                    if triplet not in result:
                        result.append(triplet)
                    
                    # Duplicates are adjacent due to sorted array
                    while p1 < p2 and nums[p1] == nums[p1 + 1]:
                        p1 += 1

                    while p1 < p2 and nums[p2] == nums[p2 - 1]:
                        p2 -= 1
                    
                    p1 += 1
                    p2 -= 1
                
                elif nums[i] + nums[p1] + nums[p2] > 0:
                    p2 -= 1
                
                else:
                    p1 += 1
        
        return result