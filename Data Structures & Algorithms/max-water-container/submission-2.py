class Solution:
    def maxArea(self, heights: List[int]) -> int:
        total = 0
        for i in range(len(heights)):
            j = i+1
            while j < len(heights):
                if heights[i]<heights[j]:
                    temp_total = heights[i]*(j-i)
                else:
                    temp_total = heights[j]*(j-i)
                if total < temp_total:
                    total = temp_total
                j += 1    
        return total