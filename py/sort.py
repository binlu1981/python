###way 1
sorted_lst=[]
def sort_new(lst):		
		min=lst[0]
		for n in lst:
			if n < min:
				min=n				
		sorted_lst.append(min)
		lst.remove(min)
		print lst
		while lst !=[]:
			sort_new(lst)
		
		return sorted_lst

a=[4,0,3,1,6,5]	
print sort_new(a)


###way 2

def swap(lst,i,j):
	temp=lst[i]
	lst[i]=lst[j]
	lst[j]=temp
	# return lst
	
# print swap([4,0,3,1,6,5],1,2)	
a=[4,0,3,1,6,5]
def sort_change(lst):
	for i in range(len(lst)):
		min=i
		for j in range(i+1,len(lst)):
			if lst[j] < lst[min]:
				min=j
		# swap(lst,i,min)
		lst.insert(i,lst.pop(min))
	return lst
print sort_change(a)

a=[4,0,3,1,6,5]
def sort_ball(lst):
	exchange=True
	length=len(lst)-1
	while exchange:
		exchange=False
		for n in range(length):
			if lst[n] > lst[n+1]:
				swap(lst,n,n+1)
				exchange=True
		length-=1
	return lst
print sort_ball(a)
	



