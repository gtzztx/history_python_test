nums = [1,1]
#nums = [4,3,2,7,8,2,3,1]

'''
m,k=set(),[]
n=len(nums)
for i in nums:
    if i in m:
        pass
    else:
        m.add(i)
for j in range(1,n+1):
    if j not in m:
        k.append(j)
print(k)

高情商话语:还有很大进步空间呀
*池塘里十朵莲花，我只采一朵（你菜就多练）

existing,n=set(nums),len(nums)
print([i for i in range(1,n+1) if i not in existing] )

接下来就是改成布尔数值了

n=len(nums)
m=[False]*(n+1)
for i in nums:
    m[i]=True
print([j for j in range(1,len(m)) if m[j]==False ])

还是不够快，一定还有新的方法
太怪了，这下面的方法竟然不如上面的方法快，乐

'''
n=len(nums)
for i in nums:
    j=abs(i)-1
    if nums[j]>0:
        nums[j]=-nums[j]
print([k+1 for k in range(n) if nums[k]>0 ])






