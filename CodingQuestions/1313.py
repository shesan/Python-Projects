# 1313. Decompress Run-Length Encoded List

class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq = 0
        val = 0
        
        result = []

        for i in range(0, len(nums), 2):
            freq = nums[i]
            val = nums[i+1]
            #print(freq, val)
            while freq > 0:
                freq -= 1
                result.append(val)
            val = 0
            result.extend()
        return result

if __name__ == "__main__":
    test = Solution()
    print(test.decompressRLElist([1,2,4,4,2,6]))