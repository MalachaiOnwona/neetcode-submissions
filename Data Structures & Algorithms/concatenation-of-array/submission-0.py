class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        ans = {}

        for i, num in enumerate(nums):
            if num in ans:
                ans[i + len(nums)] = num
            else:
                ans[i] = num
        
        return list(ans.values()) + list(ans.values())
        