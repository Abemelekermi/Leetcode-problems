class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        ans = []
        modified = []
        for i in range(len(nums)):
            currentNum = 1
            modified = nums.copy()
            modified.pop(i)
            for j in range(len(modified)):
                currentNum = currentNum * modified[j]
            ans.append(currentNum)
        return ans


nums = [1,2,3,4]

# Output = [24,12,8,6]

soln = Solution()
answer = soln.productExceptSelf(nums)
print(answer)