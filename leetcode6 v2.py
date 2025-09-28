class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        hm = {}
        stack = []

        for i in range(len(nums2)):
            while stack and stack[len(stack)-1] < nums2[i]:
                hm[stack.pop()] = nums2[i]
            stack.append(nums2[i])
            hm[nums2[i]] = -1
        return [hm[i] for i in nums1]
nums1 = [4,1,2]

nums2 = [1,3,4,2]

#answer = [-1, 3, -1]

soln = Solution()
answer = soln.nextGreaterElement(nums1, nums2)
print(answer)