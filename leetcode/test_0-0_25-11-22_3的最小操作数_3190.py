nums = [1,2,3,4]
'''
n=0
for i in nums:
    n+=abs(3*(i//3)-i)
print(n)
这里的计算结果是4，但是答案要求的却是3
嗯。。1原本应该+2到3，但它却给出了-1就可以的答案

那么完全可以写出只要有余数，加一次操作就可以了

k=0
for i in nums:
    if i%3>0:
        k+=1
print(k)

'''
print(sum(1 for i in nums if i%3>0))

#或者说

print(sum( i%3>0 for i in nums))

