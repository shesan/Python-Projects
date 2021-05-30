# 1370. Increasing Decreasing String


# class Solution(object):
#     def sortString(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         res = []
#         res[:] = s
#         res = sorted(res)
#         print(res, "MAIN")
#         anws = ""
#         dir = 2
#         while len(res) != 0:
#             a = ""
#             b = ""
#             # Go direction
#             for num in res:
#                 a = num
#                 if a != b:
#                     anws += a
#                     res.remove(num)
#                 b = num
#             dir *= -1
#             if dir > 1:
#                 res = sorted(res)
#                 print(res, "POS")
#             else:
#                 res = sorted(res, reverse=True)
#                 print(res, "NEG")

#         return anws

#         pass
class Solution:
    def sortString(self, s: str) -> str:
        result = ""
        arr = sorted([i for i in s])
        while len(arr) > 0:
            mini = arr[0]
            result = result + mini
            arr.pop(0)
            i = 0
            while i < len(arr):
                if mini < arr[i]:
                    mini = arr[i]
                    result = result + mini
                    arr.pop(i)
                else:
                    i = i + 1
            if len(arr) > 0:
                maxi = arr[-1]
                result = result + maxi
                arr.pop(-1)
                i = len(arr)-1
                while i >= 0:
                    if maxi > arr[i]:
                        maxi = arr[i]
                        result = result + maxi
                        arr.pop(i)
                    i = i - 1
        return result



test = Solution()
s = "rat"
res = []
res[:] = s
print(test.sortString(s), "RESULT")
res.append(s)

