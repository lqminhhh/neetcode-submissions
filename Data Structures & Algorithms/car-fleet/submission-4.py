class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        
        stack = []
        
        for i in range(len(cars)):
            miles_left = target - cars[i][0]
            finish = miles_left/cars[i][1]

            if not stack:
                stack.append(finish)
            elif finish <= stack[-1]:
                continue
            else:
                stack.append(finish)
        return len(stack)