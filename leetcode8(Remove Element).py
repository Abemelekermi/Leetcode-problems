class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                k+=1
                if "_" in nums:
                    nums[nums.index("_")] = nums[i]
                    nums[i] = "_"
            else:
                nums[i] = "_"
        return k

nums = [0,1,2,2,3,0,4,2]
val = 2
soln = Solution()
answer = soln.removeElement(nums, val)
print(answer)