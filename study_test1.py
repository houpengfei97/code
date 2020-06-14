str_list = ['hello', 'world']
str_join1 = ' '.join(str_list)
str_join2 = '-'.join(str_list)
print(str_join1, str_join2)


list1 = list2 = [2,4,7,43,1,2,5,64,34]
list1.sort()
print(list1)
list3 = sorted(list2)
print(list2)
print(list3)


listx = [x*2 for x in range(6)]
print(listx)
listxx = (x*2 for x in range(5))
for num in listxx:
	print(num)