class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        ans = [1] * len(nums)

        preFix = 1
        for i in range(len(nums)):
            ans[i] = preFix
            preFix *= nums[i]

        postFix = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= postFix
            postFix *= nums[i]

        return ans

nums = [1,2,3,4]

# Output = [24,12,8,6]

soln = Solution()
answer = soln.productExceptSelf(nums)
print(answer)