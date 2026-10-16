class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for val in nums:
            if val not in seen:
                seen[val] = 1
            else:
                return True
        return False
        