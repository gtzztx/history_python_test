a=[1,1]

'''
5,3,4,6,2,3
Q:找出1个丢失的数字和1个重复的数字

先用循环找出重复的数字
这里必然需要一个if判别，一个循环for
之后我们要确定它是正序还是逆序，确定再次添加的是正1还是负1

这数组要是没有任何规律，这种正序逆序反而没有用了，
这么说我还得重新写一个排序，整理一下，然后在挑出来这个断开的位置。
m,k=[],[]
for i in a:
    if i in m:
        k.append(i)
    else:
        m.append(i)
k.append(sum(range(1,len(a)+1))-sum(m))
print(k)

#转化成数学题,求和,做差,累加
n=len(a)           #列表长度
a_sum=n*(n+1)//2   #正确的总和
n_sum=sum(a)       #现在的总和
c_sum=sum(set(a))  #去重的总和
print([n_sum-c_sum,a_sum-c_sum])

#现在-去重=重复,正确-去重=遗漏

我再总和一下，不能让它变成纯粹的数学解法
*莫名的有种在抄袭的感觉
建立两个储存，
将给出的数组分类找出了重复，
再用数学的方法找出遗漏
'''
m, k = set(), []
for i in a:
    if i in m:
        k.append(i)
    else:
        m.add(i)
n=len(a)
k.append(n*(n+1)//2-sum(m))
print(k)
