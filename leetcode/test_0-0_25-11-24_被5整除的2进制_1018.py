nums = [0,1,1]
#nums =[1,0,1]


ans=[]

'''

for i in range(1,len(nums)+1):
    k=''.join(str(j) for j in nums[:i])
    ans.append(int(k,2)%5==0)
print(ans)

多么野蛮的方法，多个循环并存
要优雅

k=""
for i in nums:
    k+=str(i)
    ans.append(int(k,2)%5==0)
print(ans)
循环是减少了，但还是耗时很长呀

不得不说，还是这种转化成数学公式的方法算的快
循环只是向后读数，最后看一下经典的一行内容

return [n==0 for n in accumulate(nums,lambda x,y :((x<<1)+y)%5)]

果然还是基础不牢固呀
'''

k=0
for i in nums:
    k=(k*2+i)%5
    ans.append(k==0)
print(ans)

