"""
设计一个算法，计算出n阶乘中尾部零的个数


样例
11! = 39916800，因此应该返回 2
"""


class Solution:
    # @param n a integer
    # @return ans a integer
    def trailingZeros(self, n):
        c=0
        while n > 1:
            n=n//5
            c+=1
        return c

s=Solution()	
print s.trailingZeros(5)