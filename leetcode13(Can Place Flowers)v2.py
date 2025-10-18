class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        fb = flowerbed.copy()
        fb.insert(0, 0)
        fb.insert(len(fb), 0)
        ans = flowerbed.copy()
        for i in range(len(flowerbed)):
            if fb[i] != 1 and fb[i+2] != 1 and ans[i] != 1:
                ans[i] = 1
                fb[i+1] = 1
                n-=1
        return n == 0


flowerbed = [1,0,0,0,0,1]
n = 2
soln = Solution()
answer = soln.canPlaceFlowers(flowerbed, n)
print(answer)