#pi=4(1-1/3+1/5...+pow(-1,i+1))/(2i-1))
import math

pi=0
for i in range(1,10000):
	pi+=4*(math.pow(-1,i+1)/(2*i-1))
print pi


#e=1+1/1!+1/2!...+1/i!
e=1
factorial=1
for i in range(1,100):
	# e+=1.0/math.factorial(i)
	factorial*=i
	e+=1.0/factorial
print e