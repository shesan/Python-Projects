# 1186. Maximum Subarray Sum with One Deletion

# class Solution:
#     def maximumSum(self, arr: List[int]) -> int:
#         result = []
#         val = 0
#         for num in arr:
#             if num > 0:
#                 result.append(num)
#         if not result:
#             result.append(max(arr))
#         for num in result:
#             val += num
#         return val

class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        x = y = res = float('-inf')
        for a in arr:
            x, y = max(a, x + a), max(x, y + a)
            res = max(res, x, y)
        return res