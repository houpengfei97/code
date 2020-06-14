def last_sort(list_sort):
	list_sort.sort()
	last_item = list_sort[-1]
	#print(range(len(list_sort)-2,-1,-1))
	for i in range(len(list_sort)-2,-1,-1):
		if last_item == list_sort[i]:
			#print(last_item)
			del list_sort[i]
		else:
			last_item = list_sort[i]
	print(list_sort)

if __name__ == '__main__':
	list_t = [1,2,3,4,5,3,2,6,10,5,3,8,9,0]
	last_sort(list_t)