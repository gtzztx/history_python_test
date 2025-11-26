#ransomNote = "aa" magazine = "aab"
ransomNote = "aca"
magazine = "abca"

'''
如果只是裁剪名句,判断有无这个名言
print(ransomNote in magazine)

赎买信
逐字拆解,逐一查阅
字典的运用
循环记录，循环减少，不存在即报错
'''
k={}
construct="True"
for i in magazine:
    k[i]=k.get(i,0)+1
for i in ransomNote:
    if k.get(i,0)<=0:
        construct=False
        break
    k[i]-=1
print(construct)
