class Solution:
    def getRange(self, arr, target):
        if target not in arr:
            return [-1, -1]
        else:
            return [arr.index(target), arr.count(target) + arr.index(target) - 1]


# Test program
arr = [1, 3, 2, 2, 2, 3, 4, 7, 8, 8]

x = 2
print(Solution().getRange(arr, x))
# [1, 4]
