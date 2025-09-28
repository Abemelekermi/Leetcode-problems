class Solution(object):
    def mergeTwoLists(self, list1, list2):
        length = len(list1) + len(list2)
        i = 0
        index = 0
        newList = []
        while True:
            if(i == len(list1)):
                if(list1[index+1]>list2[i]):
                    newList.append(list1[0])
                else:
                    newList.append(list2[index+1])
            i+=1
            if(i == length):
                print(newList)
                break
            
        
soln = Solution()
print(soln.mergeTwoLists([1, 2, 4],[2, 5,4]))
        