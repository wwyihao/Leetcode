class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        stack=[] #建立一个stack列表放置已排除其他符号的字母
        result=[] #建立一个列表放置字符串拆分开的各元素
        for i in S: #遍历字符串
            if i.isalpha():  #如果是字母
                stack+=i #将字母存入列表
            result+=i 
        for i in range(len(S)):
            if S[i].isalpha():
                result[i]=stack.pop() #是字母，将stack最后一个元素赋值给结果列表
            else:
                result[i]=S[i] #非字母，将字符串中非支模赋值给结果列表
        return ''.join(result) #将列表转换成字符串
