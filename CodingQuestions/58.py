# 58. Length of Last Word

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s.split()) > 0:
            result = s.split()
            print(result)
            return len(result[-1])
        else:
            return 0

if __name__ == "__main__":

    Input= "Hello"
    Input1= ""
    Input2= " "

    test = Solution()
    print(test.lengthOfLastWord(Input))
    print(test.lengthOfLastWord(Input1))
    print(test.lengthOfLastWord(Input2))