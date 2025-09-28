# my first leetcode two sum
#it only works for positive values
class Solution(object):
    def twoSum(self, nums, target):
        index = len(nums)-1
        left = 0
        answer = []
        while True:
            for i,num in enumerate(nums):
                print(f'left: {left}')
                print(f'index: {index}')
                print(f'num: {num}')
                print(f'left num: {nums[left]} nums index:{nums[index]}')
                if num + nums[left] == target:
                    if left != i:
                        print('found the answer')
                        answer = [nums[i], nums[left]]
                        break
                    else: 
                        print('same index')
                        pass
                elif(nums[left] == nums[index]):
                    print('left num and index num are equal')
                    left+=1
                    print(left)
                    if num + nums[left] == target:
                        if left != i:
                            print('found')
                            answer = [i, left]
                            break
                        else:
                            print('same index')
                    else:
                        if (nums[left] == nums[index]):
                            print('again left num and index num are equal')
                            left+=1
                        else:
                            print('not equal')
                            print(nums[left])
                            print(nums[index])
                            if (nums[left] == nums[index]):
                                left+=1
                            else:
                                print('not incrementing 1 in to left')
                else:
                    print(num)
                    print('left num and index num are not euqal')
                index-=1
            return answer
            
x = Solution()
print(x.twoSum(nums=[2,5,5,2,11],target=10))