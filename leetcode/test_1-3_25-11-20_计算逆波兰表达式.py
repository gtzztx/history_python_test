tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
#tokens = ["4","13","5","/","+"]
#tokens = ["18"]
'''
一种四则运算计算器？
手写规则/调用规则，按照指定的方式完成计算任务
先入后出，后入先出
append pop pop(0)?
*还是不太熟悉
'''
k,x,y=[],0,0
s={
    '+':lambda y,x:float(x)+float(y), 
    '-':lambda y,x:float(x)-float(y),
    '*':lambda y,x:float(x)*float(y),
    '/':lambda y,x:float(x)/float(y)
}
for i in tokens:
    if i not in s:
        k.append(int(i))
    else:
        x,y=k.pop(),k.pop()
        k.append(int(s[i](x,y)))
print(k.pop())
