# 1351. Count Negative Numbers in a Sorted Matrix

class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        for select in grid:
            for num in select:
                if num < 0:
                    count += 1
        return count

test = Solution()
grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
print(test.countNegatives(grid))