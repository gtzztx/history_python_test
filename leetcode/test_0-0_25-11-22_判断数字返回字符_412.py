n = 3
answer=[]
'''
for i in range(1,n+1):
    if i%3==0 and i%5 ==0:
        answer.append("FizzBuzz")    
    elif i%3==0:
        answer.append("Fizz")
    elif i%5==0:
        answer.append("Buzz")
    else:
        answer.append(str(i))
print(answer)

非常直观的写法,我们优化一下
太奇怪了优化后的效果尽然不如最开始的，这是为什么？
'''

def FizzBuzz(i):
    return "Fizz"*(i%3==0) + "Buzz"*(i%5==0) or str (i)
print( [FizzBuzz(i) for i in range(1,n+1)])
