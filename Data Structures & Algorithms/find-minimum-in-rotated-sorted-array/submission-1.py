class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            # if left > mid --> ignore right
            if nums[mid] < nums[l]:
                r = mid
            # if mid > right --> ignore left
            elif nums[mid] > nums[r]:
                l = mid + 1
            # if left < mid < right
            else:
                return nums[l]
            



