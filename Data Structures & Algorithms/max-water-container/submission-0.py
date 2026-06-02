class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left = 0
        right = len(heights) - 1
        max = 0

        while left < right:
            
            base = right - left
            if heights[right] < heights[left]:

                curr_max = base*heights[right]

                if curr_max > max:
                    max = curr_max

                right -= 1

            else:
                curr_max = base*heights[left]

                if curr_max > max:
                    max = curr_max
                
                left += 1
        
        return max

