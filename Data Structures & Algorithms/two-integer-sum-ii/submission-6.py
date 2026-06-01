class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Given a sorted array, trying to find indeces which elements
        # add up to target

        # Two Pointer -> One pointer at start of array and one at the
        # end of array. If sum of elements at these indeces are greater
        # than the target value, then decrement the right pointer. If sum
        # is less than target value, increment left pointer.

        left_pointer = 0
        right_pointer = len(numbers) - 1

        while left_pointer != right_pointer:

            if numbers[left_pointer] + numbers[right_pointer] == target:
                return [left_pointer + 1, right_pointer + 1] # +1 to pointers for 1-indexed array
            
            if numbers[left_pointer] + numbers[right_pointer] > target:
                right_pointer -= 1
            
            if numbers[left_pointer] + numbers[right_pointer] < target:
                left_pointer += 1

            


        