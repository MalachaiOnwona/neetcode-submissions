class Solution:

    def binary_search(self, left: int, right: int, nums: List[int], target: int) -> int:

        if left > right:
            return -1

        middle = (left + right)//2

        if nums[middle] == target:

            return middle              

        if nums[middle] < target:

            return self.binary_search(middle + 1, right, nums, target)
        
        if nums[middle] > target:
            
            return self.binary_search(left, middle - 1, nums, target)

    def search(self, nums: List[int], target: int) -> int:

        return self.binary_search(0, len(nums) - 1, nums, target)
        

        
        
        