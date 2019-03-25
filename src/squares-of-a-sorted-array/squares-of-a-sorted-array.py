class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        temp = []
        for i in A:
            temp.append(i*i)
        temp.sort()
        return temp
