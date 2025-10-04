class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        k = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[k] = nums[i]
                nums[i] = 0
                k+=1
        return nums


nums =  [0,1,0,3,12]
soln = Solution()
answer = soln.moveZeroes(nums)
print(answer)