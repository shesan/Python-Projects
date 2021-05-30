# 1295. Find Numbers with Even Number of Digits

class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       
        result = 0
        for num in nums:
            count = 0
            while num > 0:
                count += 1
                num = int(num / 10)
            if count % 2 == 0:
                result += 1
            print(result)
        return result

if __name__ == "__main__":
    test = Solution()
    print(test.findNumbers([1, 2, 32, 3133, 2]))