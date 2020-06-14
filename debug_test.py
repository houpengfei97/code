import os
import json

file_name = "data.json"
is_file_exists = os.path.exists(file_name)
dictobj = [
	{
		'userName' : 'huawei',
		'info' : 'huawei123123'
	},
	{
		'userName': 'nokia',
		'info': 'nokia123'
	},
	{
		'userName': 'local',
		'info': 'local123'
	}
]
if is_file_exists:
	print("File is exists!")
	file = open(file_name, mode='r', encoding="utf-8")
	content = file.read()
	print(content)
else:
	print("File is not exists!")
	file = open(file_name, mode='w', encoding="utf-8")
	json.dump(dictobj, file)
	# file.write(json.dump({"userName": "huawei","info" : "huawei123123"}),file)
	# file.write("test2222\n")
