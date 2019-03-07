class Solution:
    def reverse(self, x: int) -> int:
        str_x = str(x)
        new_list =[]
        for i in str_x:
            new_list.insert(0,i)
        if new_list[-1]=='-':
            new_list.insert(0,new_list.pop())
        str_x=''.join(new_list)
        if -2**31<int(str_x)<2**31-1:
            return int(str_x)
        else:
            return 0
