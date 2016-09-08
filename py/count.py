words="abcddsegddasegpddgedaddc"
count={}
for n in words:
	if n in count:
		count[n]+=1
	else:
		count[n]=1
print count