#coding= utf-8

def loaddict(dict):
	d=open(dict).read().decode("utf-8").split()
	# d = open(dict)
	maxlen=1
	worddict=set()
	for word in d:
		# word = unicode(word.strip(),'utf-8')
		worddict.add(word)
		if len(word) > maxlen:
			maxlen = len(word.strip())
	return worddict, maxlen

def fenci(sent,worddict,maxlen):
	sent=unicode(sent,'gbk')
	begin=0
	wordlist=[]	
	while begin < len(sent):
		for end in range(begin+maxlen,begin,-1):
			if sent[begin:end] in worddict:
				wordlist.append(sent[begin:end])
				break
		begin = end
	return wordlist
				
	
worddict, maxlen = loaddict("lexicon.dic")
sent="你好美女搭车吗"
wordlist=fenci(sent,worddict,maxlen)
for word in wordlist:
	print word





