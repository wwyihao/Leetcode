class Solution:
    def judgeCircle(self, moves: str) -> bool:
        position = [0,0]
        for i in moves:
            if i == 'U':
                position[0]=position[0]+1
            elif i =='D':
                position[0]=position[0]-1
            elif i=='R':
                position[1]=position[1]+1
            elif i =='L':
                position[1]=position[1]-1
        if position==[0,0]:
            return True
        else:
            return False
