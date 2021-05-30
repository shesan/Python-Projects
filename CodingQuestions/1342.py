# 1342. Number of Steps to Reduce a Number to Zero

class Solution(object):

    # def numberOfSteps (self, num):
    #     count=0
    #     while num!=1:
    #         if num%2 == 1:
    #             num=num//2
    #             count=count+2
    #         else:
    #             num=num/2
    #             count=count+1
    #     return count+1

    def numberOfSteps (self, num: int) -> int:
        if num == 1:
            return 1
        else: 
            if num % 2 == 0:
                return 1+self.numberOfSteps(num//2)
            else:
                return 1+self.numberOfSteps(num-1)

if __name__ == "__main__":
    test = Solution()
    print(test.numberOfSteps(10))
