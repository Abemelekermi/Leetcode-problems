class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        hm = {}
        vInS = []
        answer = list(s)
        for i in range(len(s)):
            if s[i].lower() in vowels:
                hm[i] = s[i]
                vInS.append(i)

        print(vInS)
        smallest = 0
        k = len(vInS)-1
        newHm = {}
        for i in hm:
            smallest = i
            newHm[smallest] = hm[vInS[k]]
            k -=1

        print(f"new hm: {hm}")
        print(f"new hm: {newHm}")

        for i in vInS:
            answer[i] = newHm[i]

        return "".join(answer)


s = "IceCreAm"

# answer "AceCreIm"

soln = Solution()
answer = soln.reverseVowels(s)
print(answer)