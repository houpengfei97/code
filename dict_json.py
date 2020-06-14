import os
import json

data_str = '{"aaa":123,"bbb":234,"ccc":345}'
data_dict = {"xxx": 555, "zzz": 666, "ggg": 777}

#json字符串to字典对象
dict_from_str = json.loads(data_str)
print(f"dict_from_str : {dict_from_str}, tpye : {type(dict_from_str)}")
#字典对象to json字符串
str_from_dict = json.dumps(data_dict)
print(f"str_from_dict : {str_from_dict}, tpye : {type(str_from_dict)}")

file_name = "data_json"
is_file_exists = os.path.exists(file_name)

if is_file_exists:
	print("File is exists!")
	with open(file_name) as f:
		dict_from_str_file = json.load(f)
		print(f"dict_from_str_file : {dict_from_str_file}")
else:
	print("File is not exists!")
	with open(file_name, mode="w") as f:
		json.dump(data_dict, f)


