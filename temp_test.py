from functools import reduce
def test_1(l):
	for index in range(0,len(l)):
		l[index]*=2
	return l

def test_2(m):
	tmp_m = []
	for item in m:
		tmp_m.append(item*2)
	return tmp_m

if __name__ == '__main__':
	list_1= [1,3,4,5,6,7]
	tmplist=test_1(list_1)
	print(tmplist)
	tmp_list2= test_2(list_1)
	print(tmp_list2)
	print ([(lambda x : x*2)(x) for x in list_1] )
	L_1=map(lambda x : x*2,list_1)
	print(list(L_1))
	print (list(filter(lambda x: x%2 ==0,list_1)))
	print (list(reduce(lambda x,y:x+y,list_1)))