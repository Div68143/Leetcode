class Solution:
    def maximumProduct(self, num):
        num.sort()
        return max(num[-1] * num[-2] * num[-3],num[0] * num[1] * num[-1])
