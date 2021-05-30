# 1323. Maximum 69 Number

class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        # res = str(num)
        # res2 = []
        # res2 [:] = res
        # sample = ""
        # for i in range(len(res2)):
        #     if res2[i] == 6:
        #         res2[i] = 9
        #         break
            
        # for x in res2:
        #     sample += x
        # return int(sample)

        return int(str(num).replace('6', '9', 1))

test = Solution()
num = 9669
print(test.maximum69Number(num))
        