
def dict_sort(dict_in):
	#sort_res = sorted(dict_in.items(),key=lambda item:item[1],reverse=True)
	#sort_res = sorted(dict_in.keys(),reverse=True)
	sort_res = sorted(dict_in.values(),reverse=True)
	return sort_res

if __name__ == '__main__':
	d = {'mike': 10, 'lucy': 2, 'ben': 30}
	d_tmp = dict_sort(d)
	print(d_tmp)