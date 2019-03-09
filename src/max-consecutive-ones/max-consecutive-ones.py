class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        final_count=0
        temp=0
        for i in nums:
            if i == 1:
                temp += 1;
                if temp > final_count: #临时计数器大于最终计数器时，赋值给最终计数器
                    final_count = temp
            elif i ==0:
                temp = 0 #遇0，临时计数器归零
        return final_count
