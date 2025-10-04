class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                nums[i] = ''
                k+=1

        return nums

nums =  [3, 2, 2, 3]
val = 3
soln = Solution()
answer = soln.removeElement(nums, val)
print(answer)