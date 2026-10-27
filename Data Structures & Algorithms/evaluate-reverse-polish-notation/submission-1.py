class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers = []
        for token in tokens:
            # print(token, numbers)
            if token in ("+", "-", "*", "/"):
                
                no1 = int(numbers[-2])
                no2 = int(numbers[-1])
                if token == "+":
                    cal = no1 + no2
                elif token == "-":
                    cal = no1 - no2
                elif token == "*":
                    cal = no1 * no2
                else:
                    cal = int(no1/no2)
                numbers.pop()
                numbers[-1] = cal
            else:
                numbers.append(token)
        return int(numbers[0])