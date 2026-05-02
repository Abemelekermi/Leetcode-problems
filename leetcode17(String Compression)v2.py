class Solution:
    def compress(self, chars: list[str]) -> int:
        currentCharHm = {}
        charCount = 0
        for i in range(len(chars)):
            if currentCharHm:
                currentChar = list(currentCharHm.items())[0][1]
                currentCharIndex = list(currentCharHm.items())[0][0]
                if chars[i] == currentChar:
                    print(f"{chars[i]} == {currentChar} so adding 1 to {charCount}")
                    charCount += 1
                if chars[i] != currentChar or len(chars) - 1 == i:
                    if charCount >= 2:
                        print(f"charcount: {charCount} greater than 2")
                        print(f"{chars[i]} != {currentChar} so modifiying the chars reseting charCount:{charCount} to 1 clearning currentCharHm")
                        for j in range(len(str(charCount))):
                            chars[currentCharIndex + 1 + j] = str(charCount)[j]
                    print(f"modified chars: {chars}")
                    charCount = 1
                    currentCharHm.clear()
                    print(f"currentCharHm: {currentCharHm}")
                    currentCharHm[i] = chars[i]
                    print(f"modified currentCharHm: {currentCharHm}")
            else:
                charCount += 1
                currentCharHm[i] = chars[i]

        print(chars)
        nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        uniqueChars = []
        numFound = False
        k = 0
        for i in range(len(chars)):
            print(f"i: {i}")
            print(f"chars new: {chars}")
            if numFound and chars[k] not in nums and uniqueChars.count(chars[k]) > 1:
                print(f"poopiingg")
                chars.pop(k)
            elif chars[k] in nums:
                print(f'{chars[i]} is in nums')
                numFound = True
                k = 0
                k = i + 1
            elif chars[k] not in uniqueChars:
                print(f"adding {chars[i]} to the uniqueChar")
                uniqueChars.append(chars[i])
            elif chars[k] not in nums:
                numFound = False
                if chars[k] in uniqueChars:
                    chars.pop(k)

        return chars


chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
soln = Solution()
answer = soln.compress(chars)
print(answer)