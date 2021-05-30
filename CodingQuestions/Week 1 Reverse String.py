class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        for i in range(int(len(s)/2)):
            tmp = s[i]
            s[i] = s[len(s)-(i+1)]
            s[len(s)-(i+1)] = tmp
        print(s)

        s.reverse()
        print(s)




        
        

test = Solution()
Input = ["h","e","a","2","o", "2"]
print(len(Input))
print(Input[0])
print(Input[-1])
print(Input[-2])

print(test.reverseString(Input))