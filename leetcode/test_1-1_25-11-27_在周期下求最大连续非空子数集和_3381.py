
nums = [-1,-2,-3,-4,-5]
k = 4
n=len(nums)

'''
max_num=float('-inf')

for i in range(k,n+1,k):
    for j in range(0,n-i+1):
        num=sum(nums[j:j+i])
        if max_num<num:
            max_num=num
print(max_num)

时间复杂度为o(n^2),需要多次遍历数组，暴力而缺乏美感
结合一下数组的方式，先记录再计算

建立最小数，建立数组，确定第一个数
循环序列数，数组内判断它是否符合两个条件1.已经有数2.属于多次每个周期下的最小数
在有数的情况下判断它最大的连续数差值是多少，
'''
ans,m_sum=float('-inf'),0
m=[10**20]*k
m[0]=0

for i in range(1,n+1):
    r=i%k
    m_sum+=nums[i-1]
    if m[r]!=10**20:
        current_sum=m_sum-m[r]
        if ans<current_sum:
            ans=current_sum
    if m[r]>m_sum:
        m[r]=m_sum
print(ans)
