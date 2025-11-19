nums = [1,1,0,1,1,1,1,1,1,1,1,1]
max_len,k=0,0
for i in nums:
    if i==1:
        k+=1
        if k>max_len:
            max_len=k
    else:
        k=0
print(max_len)   
'''
这里由于是简单的操作所以耗时反而少了；提供一些简化的内容

简化if判别，k=(k+i)*i    乘法耗时超过加减法

简化两只比较

max(k,max_len)     
调用内部的比较函数，耗时超过比较+赋值

max_len=k if k>max_len else max_len  
python里面的三目运算，感觉还是不如c的直观,用它不如用if-else语句，一点没少打字

''' 
