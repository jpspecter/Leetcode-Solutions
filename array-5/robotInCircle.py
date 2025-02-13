#Time: O(n)
#Space: O(1)
#Program ran on leetcode successfully

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direction = 0
        x, y = 0, 0
        for c in instructions:
            if c == 'G':
                if direction == 0:
                    y += 1
                elif direction == 1:
                    x -= 1
                elif direction == 2:
                    y -= 1
                else:
                    x += 1
            elif c == 'L':
                direction += 1
            elif c == 'R':
                direction -= 1
            
            # reset direction if 360 degrees
            direction %= 4
        
        return (x == 0 and y == 0) or direction != 0
        