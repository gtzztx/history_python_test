'''
日志序号     日志内容     栈操纵(填:压栈/弹栈/忽略)      栈状态(示例:[(0,0)]/[])      时间计算依据(进程id+计算逻辑+时长)      dict_ans(示例:{0:1})
1           "0:start:0"          压栈                     [(0,0)]                       进程0,开始运行,时长0                     {0:0}
2           "0:start:2"       弹栈 -> 压栈                [(0,2)]                       进程0,再次运行,时长2-0=2                 {0:2}
3           "0:end:5"            弹栈                      []                           进程0,终止运行,时长5-2+1=4               {0:6}

'''
n=1
logs=["0:start:0","0:start:2","0:end:5"]
dict_ans,stack={0:0},[]
for i in logs:
    id,action,time=i.split(':')
    id,time=int(id),int(time)
    if action == "start":
        if stack:
            id_now,time_now=stack[-1]
            dict_ans[id_now] += time - time_now
        stack.append((id,time))
    else:
        id_now,time_now=stack.pop()
        dict_ans[id] += time - time_now + 1
print(dict_ans)

