'''
写点简单的放松一下

1.请返回 nums 的动态和
'''
nums = [1,2,3,4]
'''
for i in range(1,len(nums)):
    nums[i]+=nums[i-1]
print(nums)

这里先限定范围，判断长度，1-4，只出现1-3三个数
变化规律应该是
[1,2,3,4]->[1,2+1,3,4]->[1,3,3+3,4]->[1,3,6,4+6]
[1,1,1,1]->[1,1+1,1,1]->[1,2,1+2,1]->[1,2,3,1+3]
[3,1,2,1]->[3,1+3,2,1]->[3,4,4+2,1]->[3,4,6,1+6]
*超级拼装！
return nums[i]+=nums[i-1] for i in range(1,len(nums))
报错！return不可以直接赋值
'''
n,k=[],0
for i in nums:
    k+=i
    n.append(k)
print(n)
print(len(nums))
