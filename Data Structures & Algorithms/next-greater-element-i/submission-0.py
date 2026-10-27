class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1] * len(nums1)
        
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    nums1[i] = j
                    break
        
        for i in range(len(nums1)):
            j = nums1[i] + 1
            while j < len(nums2):
                if nums2[j] > nums2[nums1[i]]:
                    ans[i] = nums2[j]
                    break
                j += 1
        return ans
            