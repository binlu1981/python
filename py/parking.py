import random

def parking(start,end):
	if end-start < 1.0:
		return 0
	else:
		x=random.uniform(start,end-1)
		num = parking(start,x)+1+parking(x+1,end)
		return num
print parking(0,5)

s=0
for i in range(1000):
	s+=parking(0,5)
print s/1000.0
