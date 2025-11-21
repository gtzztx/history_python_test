
'''
进程调度算法
时间:时间段(间隔)、时间点(端点)
抢占式、非抢占式(并列式)

0-3,4个端点,3个间隔

*莫名的走了好多弯路
并行的时间计算只看开始和结束
抢占的只要没出声就没工作,每次都要进行结算。

'''
n=2
logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
stack=[]
dict_ans={k:0 for k in range(n)}
for i in logs:
    id,action,time=i.split(":")
    id,time=int(id),int(time)
    if action == "start":
        if stack:
            id_now,time_now=stack[-1]
            dict_ans[id_now] += time - time_now
        stack.append((id,time))
    else:
        id_now,time_now=stack.pop()
        dict_ans[id_now] += time - time_now + 1
        if stack:
            id_now=stack[-1][0]
            stack[-1] = ( id_now, time+1 )
print([dict_ans[k] for k in range(n)])


