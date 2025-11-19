nums=[1,2,3,4,5,6]
n=3
ans=[]
for i in range(n):
    ans.append(nums[i])
    ans.append(nums[i+n])
print(ans)
#同样是数组排序，这是初步思考了

#=============================================

nums[0::2],nums[1::2]=nums[:n],nums[n:]
print(nums)


'''
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums[::2],nums[1::2]=nums[:n],nums[n:]
        return nums
这个是最简洁的
a=1,b=2
a,b=1,2
格外简单的赋值
nums[开始:结束:间隔],对于数组的理解。
'''




