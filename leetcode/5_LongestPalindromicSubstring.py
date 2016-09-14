"""
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length 
of S is 1000, and there exists one unique longest palindromic substring.
"""

class Solution(object):
	def longestPalindrome(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		begin=0
		maxlen=0
		pldr_lst=[]
		if not s:
			return ""
		else:
			while begin < len(s):
				for end in range(len(s)-1,begin,-1):
					if s[begin:end]==s[end+end-begin-1:end-1:-1]:
						pldr_subs=s[begin:end+end-begin]
						pldr_lst.append(pldr_subs)
					if s[begin:end]==s[end+end-begin-2:end-2:-1]:
						pldr_subs=s[begin:end+end-begin-1]
						pldr_lst.append(pldr_subs)
						
				begin+=1
			else:
				pldr_lst.append(s[-1])
	#                maxlen=len(plder_subsif) if len(plder_subs)>maxlen
	#        print pldr_lst
			pldr_lst.sort(key = lambda x: len(x), reverse= True)
			return pldr_lst[0]
		
		
		
a="ada"
b="zudfweormatjycujjirzjpyrmaxurectxrtqedmmgergwdvjmjtstdhcihacqnothgttgqfywcpgnuvwglvfiuxteopoyizgehkwuvvkqxbnufkcbodlhdmbqyghkojrgokpwdhtdrwmvdegwycecrgjvuexlguayzcammupgeskrvpthrmwqaqsdcgycdupykppiyhwzwcplivjnnvwhqkkxildtyjltklcokcrgqnnwzzeuqioyahqpuskkpbxhvzvqyhlegmoviogzwuiqahiouhnecjwysmtarjjdjqdrkljawzasriouuiqkcwwqsxifbndjmyprdozhwaoibpqrthpcjphgsfbeqrqqoqiqqdicvybzxhklehzzapbvcyleljawowluqgxxwlrymzojshlwkmzwpixgfjljkmwdtjeabgyrpbqyyykmoaqdambpkyyvukalbrzoyoufjqeftniddsfqnilxlplselqatdgjziphvrbokofvuerpsvqmzakbyzxtxvyanvjpfyvyiivqusfrsufjanmfibgrkwtiuoykiavpbqeyfsuteuxxjiyxvlvgmehycdvxdorpepmsinvmyzeqeiikajopqedyopirmhymozernxzaueljjrhcsofwyddkpnvcvzixdjknikyhzmstvbducjcoyoeoaqruuewclzqqqxzpgykrkygxnmlsrjudoaejxkipkgmcoqtxhelvsizgdwdyjwuumazxfstoaxeqqxoqezakdqjwpkrbldpcbbxexquqrznavcrprnydufsidakvrpuzgfisdxreldbqfizngtrilnbqboxwmwienlkmmiuifrvytukcqcpeqdwwucymgvyrektsnfijdcdoawbcwkkjkqwzffnuqituihjaklvthulmcjrhqcyzvekzqlxgddjoir"
s=Solution()
print s.longestPalindrome(b)
