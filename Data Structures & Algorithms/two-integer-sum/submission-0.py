class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            val = target - nums[i]
            if val not in seen:
                seen[nums[i]] = i
                seen[val] = i
            else:
                return [min(seen[val], i), max(seen[val], i)]

                

        return 
            