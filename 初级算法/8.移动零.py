#给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
#示例:
#输入: [0,1,0,3,12]
#输出: [1,3,12,0,0]
#说明:
#必须在原数组上操作，不能拷贝额外的数组。
#尽量减少操作次数。
#type nums:List[int]
#rtype nums:List[int]
class Solution:
    #耗时284ms  暴力破解所得   提交去除return
    def moveZeroes(self, nums):
        for i in range(len(nums)):
            if(nums[i]!=0):
                continue
            else:
                for j in range(i+1,len(nums)):
                    if (nums[j]!=0):
                        nums[i],nums[j]=nums[j],nums[i]
                        break
                    else:
                        continue
        return
    #自己优化了一下耗时64ms  暴力破解所得   提交去除return
    def moveZeroes1(self, nums):
        judge=0
        for i in range(len(nums)):
            if(nums[i]!=0):
                continue
            else:
                if judge==0:
                    indexj=i+1
                    judge=1
                for j in range(indexj,len(nums)):
                    if (nums[j]!=0):
                        nums[i],nums[j]=nums[j],nums[i]
                        indexj=j
                        break
                    else:
                        continue
        return
    #网站上耗时最少的代码44ms  ，学习下
    def moveZeroes3(self, nums):
        index = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[index]=nums[i]
                index+=1
        for i in range(index,len(nums)):
            nums[i]=0
s=Solution()
print(s.moveZeroes([0,1,1,1,2,0,3]))