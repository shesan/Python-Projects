#Week 1 Two City Sch

class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        result = 0
        for item in costs:
            result += min(item)
        return result

        
test = Solution()
Input =  [[10,20],[30,200],[400,50],[30,20]]
print(test.twoCitySchedCost(Input))
