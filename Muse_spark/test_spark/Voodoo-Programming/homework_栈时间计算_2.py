'''
日志序号     日志内容     栈操纵(填:压栈/弹栈/忽略)      栈状态(示例:[(0,0)]/[])      时间计算依据(进程id+计算逻辑+时长)                      dict_ans(示例:{0:1})
1           "1:start:1"         压栈                        [(1,1)]                       进程1,开始运行,时长0                                      {1:0}
2           "2:start:3"         压栈                        [(1,1),(2,3)]                 进程2,开始运行;1中止运行,1时长3-1=2                       {1:2,2:0}
3           "2:end:6"           弹栈                        [(1,1)]                       2停止,2时长6-3+1=4;1调整时间为(当前时间+1)恢复运行        {1:2,2:4}
4           "1:end:8"           弹栈                        []                            1停止,1时长8-(6+1)+1=2                                    {1:4,2:4}

'''
n=2
stack=[]
ans={id:0 for id in range(1,n+1)}
logs=["1:start:1","2:start:3","2:end:6","1:end:8"]
for i in logs:
    id,action,time=i.split(":")
    id,time=int(id),int(time)
    if action == "start":
        if stack:
            id_now,time_now=stack[-1]
            ans[id_now] += time - time_now 
        stack.append((id,time))
    else:
        id_now,time_now = stack.pop()
        ans[id] += time - time_now +1
        if stack:
            id_now = stack[-1][0]
            stack[-1]=(id_now,time+1)
print(ans)
