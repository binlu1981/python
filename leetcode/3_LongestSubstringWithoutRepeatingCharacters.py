"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

author: binlu1981
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        stringlen= len(s)
        begin = 0
        maxlen = 0
        substringlist=[]
        while begin < stringlen:
            for end in range(stringlen,begin,-1):
                substring = s[begin:end]
                if substring == ''.join(sorted(set(substring), key=substring.index)):
                    substringlist.append(substring)
#                    sublen=len(substring)
#                    if sublen> maxlen:
#                        maxlen = sublen
                        
            begin+=1
        if not substringlist:
            return 0
        else:
            substringlist.sort(key = lambda x: len(x), reverse= True)
    #        substringdict={}
    #        for n in substringlist:
    #            substringdict[n]=len(n)
    #            if len(n) > maxlen:
    #                maxlen = len(n)
            return len(substringlist[0])


a="abcabcbb"
b="pwwkew"
c=""
d="ngvzdvhwkcgcpljnsatlvuhhkqlfcakpihqlexhocptracgvcz"
s=Solution()
print s.lengthOfLongestSubstring(a)
print s.lengthOfLongestSubstring(d)
print s.lengthOfLongestSubstring(c)




			