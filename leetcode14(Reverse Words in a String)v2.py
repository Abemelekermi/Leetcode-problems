class Solution:
    def reverseWords(self, s: str) -> str:
        ans = {}
        k = 0
        sL = s.split(" ")
        for i in range(len(sL)):
            if sL[i] != "":
                k+=1
                ans[k] = sL[i]
        return " ".join([ans[len(ans)-i] for i in range(len(ans))])

s = "  hello world  "

# Output =  "world hello"

soln = Solution()
answer = soln.reverseWords(s)
print(answer)