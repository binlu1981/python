def kaolazi(n):
	while n != 1:
		if n%2==0:
			n/=2
		else:
			n=n*3+1
	return n
for i in range(2,30):
	print kaolazi(i)