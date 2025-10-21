class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = ['a', 'e', 'i', 'o', 'u']
        left = 0
        right = len(s) - 1
        while right > left:
            if s[left].lower() in vowels and s[right].lower() in vowels:
                s[left], s[right] = s[right], s[left]
                left +=1
                right -=1
            if s[left].lower() not in vowels:
                left +=1
            if s[right].lower() not in vowels:
                right -=1
        return "".join(s)

s = "IceCreAm"

# answer "AceCreIm"

soln = Solution()
answer = soln.reverseVowels(s)
print(answer)