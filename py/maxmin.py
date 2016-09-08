def max_min(lst):
	max=min=lst[0]
	for i in lst[1:]:
		if i<min:
			min=i
			# lst=lst[1:]
		if i>max:
			max=i
			lst=lst[1:]
	return min,max

	
a=[4,0,3,1,6,5]
print max_min(a)
	