import time

def find_unique_price_list(products):
	unique_price_list= []
	for price in products:
		if price not in unique_price_list:
			unique_price_list.append(price)
	return len(unique_price_list)

def find_unique_price_set(products):
	unique_price_list= set()
	for price in products:
		if price not in unique_price_list:
			unique_price_list.add(price)
	return len(unique_price_list)

if __name__ == '__main__':
	# products=[
	# 	(1,1111111),
	# 	(2,2222222),
	# 	(3,3333333),
	# 	(1, 1111111)
	# ]
	# print("num of price is,",format(find_unique_price_list(products)))
	id = [x for x in range(1,10000)]
	price = [y for y in range(20000,30000)]
	products = list(zip(id,price))

	#计算列表版本的时间
	start_using_list = time.perf_counter()
	find_unique_price_list(products)
	end_using_list = time.perf_counter()
	print("The time of list:", format(end_using_list - start_using_list))

	#计算集合版本时间
	start_using_set = time.perf_counter()
	find_unique_price_set(products)
	end_using_set = time.perf_counter()
	print("The time of set:", format(end_using_set - start_using_set))



