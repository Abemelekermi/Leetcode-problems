class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        li = []
        tempNum = nums
        for i, num in enumerate(tempNum):
            li.append(tempNum[i])
            if(len(tempNum)!= i+1):
                if(tempNum[i+1] in li):
                    nums.remove(tempNum[i+1])
            else:
                return print(nums)
                
nums =[1,1,2]

removeDuplicated = Solution()
print(removeDuplicated.removeDuplicates(nums))