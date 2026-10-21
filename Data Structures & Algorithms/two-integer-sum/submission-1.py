class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}
        for i in range(len(nums)):
            diff = target - nums[i]  
            if nums[i] in freq:
                return [freq[nums[i]], i]
            if diff not in freq:
                freq[diff] = i
        