class Solution(object):
    def isValid(self,s):
        stack = []
        pairs = {
            '{':'}',
            '[':']',
            '(':')',
        }
        for c in s:
            if c in pairs:
                stack.append(c)
            elif len(stack)==0 or c != pairs[stack.pop()]:
                return False
        return len(stack) == 0


soln = Solution()
print(soln.isValid('[]'))