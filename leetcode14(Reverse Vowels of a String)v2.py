class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        k = len(s)-1
        v1 = []
        answer = list(s)
        for i in range(len(s)):
            if s[i].lower() in vowels:
                v1.append(i)

            if v1:
                if s[k].lower() in vowels:
                    lastV = v1[0]
                    v1.pop(0)
                    answer[lastV] = s[k]
                    answer[k] = s[lastV]
                k-=1
        return "".join(answer)


s = "IceCreAm"

# answer "AceCreIm"

soln = Solution()
answer = soln.reverseVowels(s)
print(answer)