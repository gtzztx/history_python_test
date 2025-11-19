#nums = [7,7,7,7]
#nums = [6,5,4,8]
nums = [8,1,2,2,3]
'''
n=len(nums)
m=0
k=[]
for i in range(n):
    m=0
    for j in nums:
        if nums[i] >j:
            m+=1
    k.append(m)
print(k)

这是暴力破解的思路，耗时几乎是两倍
答案给出了一个特别的答案，
非常相似的归类思路，然后统计范围。
*严格来说后面三行还可以压缩到一行，除了看着有些头晕。
'''
m,k=[0]*101,[]
for i in nums:
    m[i]+=1
for n in nums:
    k.append(sum(m[0:n]))
print(k)



