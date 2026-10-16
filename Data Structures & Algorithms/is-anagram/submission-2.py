class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        seen = {}
        for char1 in s:
            if char1 not in seen:
                seen[char1] = 1
            else:
                seen[char1] += 1
        
        for char2 in t:
            if char2 in seen:
                seen[char2] -= 1
            else:
                return False
        
        for key, val in seen.items():
            if val != 0:
                return False

        return True