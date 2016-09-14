class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        elif x < 0:
            return -int(str(-x)[::-1])
        else:
            return int(str(x)[::-1])
			
class Solution1(object):
    # @return an integer
    def reverse(self, x):
        answer = 0
        sign = 1 if x > 0 else -1
        x = abs(x)
        while x > 0:
            answer = answer * 10 + x % 10
            x /= 10
        return sign*answer			

a=123		
b=1534236469
s=Solution()
print s.reverse(b)