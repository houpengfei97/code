from typing import List

def dict_list_fuzhi(list_a: List[str],list_b:List[str]):
	# dict_res = []
	# for b_v in list_b:
	# 	dict_res.append(dict(zip(list_a,b_v)))
	# return dict_res
	#return list(dict(map(lambda x,y:(x,y),list_a,v_b))for v_b in list_b)

	#return [dict(zip(list_a,b_v))for b_v in list_b]

	return [{attr:value[index] for index,attr in enumerate(list_a)}for value in list_b]
if __name__ == '__main__':
	list_res = []
	attributes = ['name', 'dob', 'gender']
	values = [['jason', '2000-01-01', 'male'], ['mike', '1999-01-01', 'male'], ['nancy', '2001-02-01', 'female']]
	list_res = dict_list_fuzhi(attributes,values)
	print(list_res)