class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        prefix[0] = nums[0]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i]
        
        postfix = [1] * len(nums)
        postfix[-1] = nums[-1]
        for k in range(len(nums) - 2, -1, -1):
            postfix[k] = postfix[k + 1] * nums[k]
        
        output = [0] * len(nums)
        output[0] = postfix[1]
        output[-1] = prefix[-2]
        
        for i in range(1, len(nums) - 1):
            output[i] = prefix[i - 1] * postfix[i + 1]
        return output