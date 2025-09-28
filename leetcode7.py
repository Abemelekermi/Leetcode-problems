#1475. Final Prices With a Special Discount in a Shop
class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        hm = {}
        stack = []
        reversedPrice = [prices[len(prices)-1-i] for i in range(len(prices))]
        print(reversedPrice)
        for i in range(len(reversedPrice)):
            print(f"current stack: {stack[len(stack)-1] if len(stack) !=0 else None}")
            print(f"current reversed price: {reversedPrice[i]}")
            while stack and stack[len(stack)-1] > reversedPrice[i]:
                print("here")
                hm[stack.pop()] =  reversedPrice[i]
            stack.append(reversedPrice[i])
            print(f"stack got updated {stack}")
            hm[reversedPrice[i]] = 0
            print(f"hm got updated with 0{hm}")
        return hm

prices = [8,4,6,2,3]
# answer =  [4,2,4,2,3]

soln = Solution()
answer = soln.finalPrices(prices)
print(answer)