class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        largest = word1 if len(word1) >= len(word2) else word2
        smallest = word2 if len(word1) >= len(word2) else word1
        answer = ""
        for i in range(len(smallest)):
            answer += word1[i]
            answer += word2[i]
            if len(smallest)-1 == i:
                answer += largest[i+1:]
        return answer


word1 = "abcd"
word2 = "pq"

# answer = a p b q c r

soln = Solution()
answer = soln.mergeAlternately(word1, word2)
print(answer)