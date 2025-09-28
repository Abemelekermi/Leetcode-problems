# my first leetcode two sum
#it only works for positive values
class Solution(object):
    def twoSum(self, nums, target):
        left = 0
        answer = []
        for i,num in enumerate(nums):
            for ii,numm in enumerate(nums):
                print(f'i:{i}')
                print(f'ii:{ii}')
                if num+numm == target:
                    if i==ii:
                        print(f'i:{i}')
                        print(f'ii:{ii}')
                        print('same index')
                        pass
                    else:
                        answer = [num, numm]
                        break
                else:
                    print('not euqls')
                    pass
        return answer
                
            
x = Solution()
print(x.twoSum(nums=[2,5,5,2,11],target=10))