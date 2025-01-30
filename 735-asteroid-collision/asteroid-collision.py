class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
            else:
                if len(stack) == 0 or stack[-1] < 0:
                    stack.append(asteroid)

                else:
                    while len(stack) > 0 and stack[-1] > 0:
                        if abs(asteroid) > stack[-1]:
                            stack.pop(-1)
                            if len(stack) == 0 or stack[-1] < 0:
                                stack.append(asteroid)
                                break
                        elif abs(asteroid) == stack[-1]:
                            stack.pop(-1)
                            break
                        else:
                            break
                    
        return stack