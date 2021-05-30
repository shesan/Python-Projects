# 1365. How Many Numbers Are Smaller Than the Current Number

import collections

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        result = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    count += 1
            result.append(count)
        return result


        

if __name__ == "__main__":
    test = Solution()
    tester = [8,1,2,2,3]
    print(test.smallerNumbersThanCurrent(tester))