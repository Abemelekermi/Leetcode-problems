class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1 = len(str1)
        len2 = len(str2)
        if str1 + str2 == str2 + str1:
            while len1 != len2:
                if len1 > len2:
                    len1 = len1 - len2
                else:
                    len2 = len2 - len1
            return str1[:len1]

        else:
            return ""


str1 = "ABCABC"
str2 = "ABC"

# Output ABC

soln = Solution()
answer = soln.gcdOfStrings(str1, str2)
print(answer)