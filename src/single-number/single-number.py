class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        temp=[]
        for i in nums:
            if i in temp:
                temp.remove(i) #遍历列表，如果数字在临时列表里，就删除。没有就添加
            else:
                temp.append(i)
        return temp[0]
