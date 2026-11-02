class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        x = len(nums)

        idx = 0
        
        # if nums[idx] < x -> move idx to 1 index and decrease x by 1
        # if nums[idx] >= x -> check prev
        while idx < len(nums) and x > 0:
            if nums[idx] < x:
                idx += 1
                x -= 1
            else:
                if idx > 0:
                    if nums[idx - 1] >= x:
                        idx += 1
                        x -= 1
                    else:
                        return x
                else:
                    return x
        return -1            



