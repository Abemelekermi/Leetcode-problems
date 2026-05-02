class Solution:
    def compress(self, chars: list[str]) -> int:
        s = ""
        charLen = 1
        for i in range(len(chars)):
            if s != "" and chars[i] == s[len(s)-2]:
                print(f"{s} not empty and {chars[i]} == {s[len(s) - 2]} so adding 1 to {charLen}")
                charLen = int(s[len(s) - 1]) + 1
                if len(s) >= 4:
                    print(s)
                    print(s[len(s) - 2:])
                    print(s[:2])
                    s =  s[:len(s) - 2] + s[len(s) - 2:].replace(s[len(s) - 1], str(charLen), 1)
                    print(f"s at len(s) ?= 4: {s}")
                else:
                    print(f"{s} less than 4")
                    s = s.replace(s[len(s) - 1], str(charLen), 1)
                    print(f"s: {s}")

            else:
                print(f"s empty so resesting charLen and adding {chars[i]} and 1 to s:{s}")
                charLen = 1
                s += chars[i]
                s += '1'
                print(f"s: {s}")
                print("----------------- \n")
        return len(s)

chars = ["a","a","b","b","c","c","c"]
soln = Solution()
answer = soln.compress(chars)
print(answer)