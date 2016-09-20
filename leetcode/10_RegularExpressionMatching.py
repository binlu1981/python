class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m = len(s)
        n = len(p)
        # Init dp
        dp = [[False for i in range(n + 1)] for i in range(m + 1)]
        # When string and pattern are all None
        dp[m][n] = True
        # When the string is None, pattern like "a*" can still match it
        for i in range(n - 1, -1, -1):
            if p[i] == "*":
                dp[m][i] = dp[m][i + 1]
            elif i + 1 < n and p[i + 1] == "*":
                dp[m][i] = dp[m][i + 1]
            else:
                dp[m][i] = False

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # When the current character is "*"
                if p[j] == "*":
                    if j - 1 >= 0 and p[j - 1] != "*":
                        dp[i][j] = dp[i][j + 1]
                    # If the pattern is starting with "*" or has "**" in it
                    else:
                        return False
                # When the the second character of pattern is "*"
                elif j + 1 < n and p[j + 1] == "*":
                    # When the current character matches, there are three possible situation
                    # 1. ".*" matches nothing
                    # 2. "c*" matches more than one character
                    # 3. "c*" just matches one character
                    if s[i] == p[j] or p[j] == ".":
                        dp[i][j] = dp[i][j + 2] or dp[i + 1][j] or dp[i + 1][j + 2]
                    # Ignore the first two characters("c*") in pattern since they cannot match
                    # the current character in string
                    else:
                        dp[i][j] = dp[i][j + 2]
                else:
                    # When the current character is matched
                    if s[i] == p[j] or p[j] == ".":
                        dp[i][j] = dp[i + 1][j + 1]
                    else:
                        dp[i][j] = False
        return dp[0][0]


if __name__ == "__main__":
    assert Solution().isMatch("aa", "a") == False
    assert Solution().isMatch("aa", "aa") == True
    assert Solution().isMatch("aaa", "aa") == False
    assert Solution().isMatch("aa", "a*") == True
    assert Solution().isMatch("aa", ".*") == True
    assert Solution().isMatch("ab", ".*") == True
    assert Solution().isMatch("aab", "c*a*b") == True
	
	
	
	
"""
解题思路：正则表达式匹配的判断。网上很多的解法是用递归做的，用java和c++都可以过，但同样用python就TLE，说明这道题其实考察的不是递归。而是动态规划，使用动态规划就可以AC了。这里的'*'号表示重复前面的字符，注意是可以重复0次的。

先来看递归的解法：

如果P[j+1]!='*'，S[i] == P[j]=>匹配下一位(i+1, j+1)，S[i]!=P[j]=>匹配失败；

如果P[j+1]=='*'，S[i]==P[j]=>匹配下一位(i+1, j+2)或者(i, j+2)，S[i]!=P[j]=>匹配下一位(i,j+2)。

匹配成功的条件为S[i]=='\0' && P[j]=='\0'。
"""
class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        if len(p)==0: return len(s)==0
        if len(p)==1 or p[1]!='*':
            if len(s)==0 or (s[0]!=p[0] and p[0]!='.'):
                return False
            return self.isMatch(s[1:],p[1:])
        else:
            i=-1; length=len(s)
            while i<length and (i<0 or p[0]=='.' or p[0]==s[i]):
                if self.isMatch(s[i+1:],p[2:]): return True
                i+=1
            return False

"""
动态规划的解法
"""
class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        dp=[[False for i in range(len(p)+1)] for j in range(len(s)+1)]
        dp[0][0]=True
        for i in range(1,len(p)+1):
            if p[i-1]=='*':
                if i>=2:
                    dp[0][i]=dp[0][i-2]
        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if p[j-1]=='.':
                    dp[i][j]=dp[i-1][j-1]
                elif p[j-1]=='*':
                    dp[i][j]=dp[i][j-1] or dp[i][j-2] or (dp[i-1][j] and (s[i-1]==p[j-2] or p[j-2]=='.'))
                else:
                    dp[i][j]=dp[i-1][j-1] and s[i-1]==p[j-1]
        return dp[len(s)][len(p)]