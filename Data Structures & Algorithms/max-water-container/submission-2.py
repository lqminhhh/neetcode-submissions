class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_area = 0
        skip_left = 1
        skip_right = 1
        while l < r:
            width = r - l
            height = min(heights[l], heights[r])
            max_area = max(max_area, width * height)
            if heights[l] < heights[r]:
                if l + skip_left < len(heights):
                    if heights[l] < heights[l + skip_left]:
                        l += skip_left
                        skip_left = 1
                    else:
                        skip_left += 1
                else:
                    break
            else:
                if r - skip_right >= 0:
                    if heights[r] < heights[r - skip_right]:
                        r -= skip_right
                        skip_right = 1
                    else:
                        skip_right += 1
                else:
                    break
        return max_area


"""
1,7,1,1,1,1,2,5,12,3,500,50,7,8,4,7,38,9,10,12,6
                l                   r
                l                   
"""