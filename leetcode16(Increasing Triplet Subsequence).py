class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        first = nums[0]
        second = 0.0
        third = 0.0
        ans = {}
        ans[first] = 0
        for i in range(len(nums)):
            if type(second) == int and type(third) == int:
                break
            if i>0:
                if type(second) == float and nums[i] > first :

                    second = nums[i]
                    ans[second] = i
                    print(f"{nums[i]} > {first} so adding {second} to the ans")
                elif type(second) != float and type(third) == float and nums[i] > second:
                    third = nums[i]
                    ans[third] = i
                    print(f"{nums[i]} > {second} so adding {third} to the ans")
                else:
                    print(f"In else updating first with {nums[i]}")
                    ans.clear()
                    first = nums[i]
                    ans[first] = i
                    second = 0.0
                    third = 0.0
        print(ans)
        return len(ans) == 3

nums = [20,100,10,12,5,13]

# Output True

soln = Solution()
answer = soln.increasingTriplet(nums)
print(answer)