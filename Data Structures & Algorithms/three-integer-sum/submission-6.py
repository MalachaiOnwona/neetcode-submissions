class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)
        result = []

        for i in range(len(nums)):

            left = i + 1
            right = len(nums) - 1

            while left < right:

                curr_sum = nums[i] + nums[left] + nums[right]

                if curr_sum == 0:
                    if [nums[i], nums[left], nums[right]] not in result:
                        result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                if curr_sum < 0:
                    left += 1
                
                if curr_sum > 0:
                    right -= 1

        return result