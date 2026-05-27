class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # MOST EFFICIENT SOLUTION
        # Use a hashmap (Time Complexity: O(n) and Space Complexity: O(n))
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False
        
        