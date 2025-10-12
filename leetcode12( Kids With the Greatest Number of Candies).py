class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        largerCandy = max(candies)
        answer = [True for i in range(len(candies))]

        for i in range(len(candies)):
            if candies[i] + extraCandies < largerCandy:
                answer[i] =  False
        return answer


candies = [2,3,5,1,3]
extraCandies = 3

# Answer = [true,true,true,false,true]

soln = Solution()
answer = soln.kidsWithCandies(candies, extraCandies)
print(answer)