# 1021. Remove Outermost Parentheses

class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        pos = 0
        result = ""
        for c in S:
            if c == ")":
                pos -= 1           
            if pos:
                result += c
            if c == "(":
                pos += 1
        return result
        
test = Solution()
S = "(()())(())"
print(S)
print(test.removeOuterParentheses(S))



        