'''
模拟栈操作
栈是黑盒子，只能知道空和顶部
最大的难点是看懂题目
先塞进去再进行比较，
因为限制条件是最大数
所以它必然存在
如果它不存在数组内
就将它删除
*怎么越写越感觉我才是机器人？？
'''
target = [1,2]
n,m=4,[]

for i in range(1,n+1):
    m.append("push")
    if i >=max(target):
        break
    elif i not in target:
        m.append("pop")
print(m)
      
  
