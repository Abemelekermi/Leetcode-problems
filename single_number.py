class Solution(object):
    def singleNumber(self, nums):
        hmm = []
        for i in range(len(nums)):
            hmm.append(nums[i])
            for j in range(len(nums)):
                if i != j:
                    if nums[j] in hmm:
                        hmm.pop(i)
                    else:
                        return nums[i]
           
        
soln = Solution()
print(soln.singleNumber([1,1,2, 2, 3])) # 1