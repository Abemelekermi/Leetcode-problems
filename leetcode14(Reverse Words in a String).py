class Solution:
    def reverseWords(self, s: str) -> str:
        sL = s.split(" ")
        sL1 = []
        for i in range(len(sL)):
            if sL[i] != "":
                sL1.append(sL[i])
        k = len(sL1) - 1
        ans = ["" for i in range(len(sL1))]

        for i in range(len(sL1)):
            if type(sL1[i]) == str:
                ans[k] = sL1[i]

                k-=1
        return  " ".join(ans)

s = "  hello world  "

# Output =  "world hello"

soln = Solution()
answer = soln.reverseWords(s)
print(answer)