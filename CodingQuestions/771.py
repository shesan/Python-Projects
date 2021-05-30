# 771. Jewels and Stones

class Solution(object):
    def numJewelsInStones(self, J, S):
        result = 0
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        for s in S:
            for j in J:
                if s == j:
                    result += 1
        return result

            
    

if __name__ == "__main__":
    test = Solution()
    print(test.numJewelsInStones("aA", "aAAAbbbb"))
