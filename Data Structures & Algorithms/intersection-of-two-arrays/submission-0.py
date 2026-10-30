class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        store1 = defaultdict(int)

        for num in nums1:
            store1[num] = 1
        
        output = []
        for num in nums2:
            if num in store1 and num not in output:
                output.append(num)
        return output
        