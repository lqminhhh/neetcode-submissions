class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            diff = target - numbers[l]
            if diff == numbers[r]:
                return [l+1, r+1]
            elif diff < numbers[r]:
                r-=1
            else:
                l+=1
        return [l+1, r+1]


