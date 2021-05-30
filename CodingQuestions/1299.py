# 1299. Replace Elements with Greatest Element on Right Side

class Solution:
    def replaceElements(self, arr):
        m = -1
        i = len(arr) -1 
        while i >= 0:
            temp = arr[i]
            arr[i] = m
            if temp > m:
                m = temp
            i-= 1
        return arr
            
            

test = Solution()
arr = [17,18,5,4,6,1]
print(test.replaceElements(arr))