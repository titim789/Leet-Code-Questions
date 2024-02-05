class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1

        max_area = 0

        while start != end:
            curr_area = min(height[start], height[end]) * (end-start)
            if curr_area > max_area:
                max_area = curr_area
            
            if height[start] > height[end]:
                end -= 1
            elif height [start] < height[end]:
                start += 1
            else:
                if height[start+1] > height[end-1]:
                    start += 1
                else:
                    end -= 1
        
        return max_area