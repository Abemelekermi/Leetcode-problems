#Next Greater Element I
#Nums 1 is the subset of num 2
class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result = []
        for i in range(len(nums1)):
            indexOfNum1InNum2 = nums2.index(nums1[i])
            if len(range(indexOfNum1InNum2, len(nums2))) == 1:
                result.append(-1)
            else:
                for j in range(indexOfNum1InNum2, len(nums2)):
                    if(nums2[j] != nums2[indexOfNum1InNum2]):
                        if nums2[j] > nums2[indexOfNum1InNum2]:
                            result.append(nums2[j])
                            break
                        else:
                            if len(nums2) == j+1:
                                result.append(-1)
                                break
                    elif (nums2[j] == nums2[indexOfNum1InNum2]) and len(nums1) == i:
                        result.append(-1)
                        break
        return result

nums1 = [4,1,2]
nums2 = [1,3,4,2]

#answer = [-1,2,3]

soln = Solution()
answer = soln.nextGreaterElement(nums1, nums2)
print(answer)