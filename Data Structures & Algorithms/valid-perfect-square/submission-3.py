class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        n = num
        n = int(n ** (1/2))
        
        return True if n * n == num else False