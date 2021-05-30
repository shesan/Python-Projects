# 53. Maximum Subarray

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current = float('-inf')
        globe = float('-inf')
        for i in range (len(nums)):
            current = max(nums[i], current + nums[i])
            globe = max(current, globe)
        return globe

test = Solution()
print(test.maxSubArray([1,2,3,-3,-5, 5]))            
                
        