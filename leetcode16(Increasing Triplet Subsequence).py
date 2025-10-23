class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        first = float('inf')
        second = float('inf')

        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False

nums = [15,100,10,12,5,13]

# Output True

soln = Solution()
answer = soln.increasingTriplet(nums)
print(answer)