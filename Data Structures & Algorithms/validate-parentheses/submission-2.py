class Solution:
    def isValid(self, s: str) -> bool:
        stck = []
        for i in range(len(s)):
            if s[i] == "[" or s[i] == "{" or s[i] == "(":
                stck.append(s[i])
            else:
                if len(stck) != 0 and ((s[i] == ")" and stck[-1] == "(") or \
                    (s[i] == "}" and stck[-1] == "{") or \
                    (s[i] == "]" and stck[-1] == "[")):
                    stck.pop()
                else:
                    return False
        return len(stck) == 0
                
            


        