
word1 = "abc"
word2 = "pqr"

res=[]

'''
while i<len(word1) and j<len(word2):
    res.append(word1[i])
    res.append(word2[j])
if i<len(word1):
    res.append(word1[i:])
if j<len(word2):
    res.append(word2[j:])
ans=''.join(res)
print(ans)

双循环，不够优美，没有体现到注意力

注意到，循环本质是在最小值处停止
'''
n=min(len(word1),len(word2))
for i in range(n):
    res.append(word1[i])
    res.append(word2[i])
res.append(word1[i:])
res.append(word2[i:])
ans=''.join(res)
print(ans)

