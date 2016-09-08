# A B C
# A ---> C

count = 0
def panzi(n,A,B,C):
	global count
	if n == 1:
		print("move ",n,"from ",A,"to ",C)
		count +=1
	else:
		panzi(n-1,A,C,B)
		print("move ",n,"from ",A,"to ",C)
		count +=1
		panzi(n-1,B,A,C)
		# print("move ",n,"from ",A,"to ",C)
		# count +=1
		
panzi(2, "left","mid","right")
print count