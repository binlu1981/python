#1 1 2 3 5 ...
def fib_loop(n):
	if n==1 or n==2:
		return 1
	else:
		f1=1
		f2=1
		i=2
		while i < n:
			f3=f1+f2
			f1=f2
			f2=f3
			i=i+1
		return f3

def fib_loop_rec(n):
	if n==1 or n==2:
		return 1
	else:
		return fib_loop_rec(n-1)+fib_loop_rec(n-2)

print fib_loop(5)
print fib_loop_rec(5)