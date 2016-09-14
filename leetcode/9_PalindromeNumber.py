"""
Determine whether an integer is a palindrome. Do this without extra space.
"""



class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        low = 0
        high = len(str(x))-1
        while low < high:
            if str(x)[low] != str(x)[high]:
                return False
            low+=1
            high-=1
        return True
		
		
		
a=123321
b=0
c=-123321
s=Solution()
print s.isPalindrome(c)
