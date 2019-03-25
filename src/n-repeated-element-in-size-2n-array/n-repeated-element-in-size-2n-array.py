class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        for i  in range(len(A)):
            if A[i] in A[i+1:]:
                return A[i]
        return None
