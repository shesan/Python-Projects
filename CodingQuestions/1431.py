#1431. Kids With the Greatest Number of Candies

class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        result = []
        for candy in candies:
            if candy + extraCandies >= max(candies):
                result.append(True)
            else:
                result.append(False)
        return result

if __name__ == "__main__":
    a = [-2, 1, 3, 4]
    b = 3
    test = Solution()
    print(test.kidsWithCandies(a, b))
