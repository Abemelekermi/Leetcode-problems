#1475. Final Prices With a Special Discount in a Shop
class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        hm = {}
        stack = []
        for i in range(len(prices)):
            while stack and prices[stack[len(stack)-1]] >= prices[i]:
                hm[stack[-1]] = prices[i]
                stack.pop()

            stack.append(i)
            hm[i] = 0
        return [prices[i]- hm[i] for i in range(len(prices))]

prices = [8,7,4,2,8,1,7,7,10,1]

# answer =  [4,2,4,2,3]

soln = Solution()
answer = soln.finalPrices(prices)
print(answer)