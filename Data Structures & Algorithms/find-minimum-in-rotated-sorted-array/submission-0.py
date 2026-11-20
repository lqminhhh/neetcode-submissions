class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_val = nums[0]
        for num in nums:
            if min_val > num:
                min_val = num
        return min_val