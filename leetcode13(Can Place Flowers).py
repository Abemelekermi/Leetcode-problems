class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if len(flowerbed) > 1:
            k = 1
        else:
            k=0
        answer = flowerbed.copy()
        for i in range(len(flowerbed)):
            if n == 0:
                break
            if str(i - 1)[0] == "-":
                if answer[k] == 0 and answer[i] != 1:
                    answer[i] = 1
                    n-=1
            else:
                if answer[k] == 0 and answer[i] != 1 and answer[i-1] != 1:
                    answer[i] = 1
                    n-=1

            if k != len(flowerbed)-1:
                k+=1
            if len(flowerbed) - 1 == i and n != 0:
                return False
        print(answer)
        j = -1
        for i in range(len(answer)):
            if j != -1:
                if answer[i] == 1 and answer[i] == answer[j]:
                    return False
            j+=1
        return True

flowerbed = [0,0,1,0,0]
n = 1
soln = Solution()
answer = soln.canPlaceFlowers(flowerbed, n)
print(answer)