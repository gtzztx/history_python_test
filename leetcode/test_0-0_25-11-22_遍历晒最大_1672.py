accounts = [[1,5],[7,3],[3,5]]
'''
n=0
for i in accounts:
    if sum(i)>n:
        n=sum(i)
print(n)
遍历读取比大小,简化一下
n=0
for i in accounts:
    n=max(n,sum(i))
print(n)
再简化一下
n=0
print( n:=max( n,max(i) ) for i in accounts )

n=0
print(n:=max(sum(i) for i in accounts))

标准的基础题。。但考虑如何写的行数最少还是很有意思的
'''
print(max(sum(i) for i in accounts) )
