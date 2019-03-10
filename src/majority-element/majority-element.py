class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count={}
        for i in nums:
            count.setdefault(i,0)
            count[i]=count[i]+1
            if count[i]>len(nums)/2:
                return i
