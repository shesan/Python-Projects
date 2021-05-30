# 1281. Subtract the Product and Sum of Digits of an Integer

class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        product = 1
        sump = 0
        

        while n > 0:
            val = n % 10
            product *= val
            sump += val
            n = int(n / 10)
            result = product - sump

        return result

if __name__ == "__main__":
    test = Solution()
    print(test.subtractProductAndSum(234))