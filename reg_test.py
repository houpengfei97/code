import os

def find_newest_file(file_path):
	file_names = os.listdir(file_path)
	file_and_ctime = {}
	for file_name in file_names:
		if file_name.endswith(".py"):
			c_time = os.path.getctime(file_path + '\\' + file_name)
			file_and_ctime[file_name] = c_time
		elif list(file_name.endswith(".py")).split('.') != "py":
			print("Files not exist!")
			return FileNotFoundError
#dict order by val
	item_list_tmp = [file_and_ctime.items()]
	print(item_list_tmp)
	item_list = [[item[1], item[0]] for item in file_and_ctime.items()]
	item_list.sort()
	print(item_list)
	return item_list[-1][1]


if __name__ == "__main__":
	path = "D:\\2020_workspace\\pythontest\\study_test"
	result_file = find_newest_file(path)
	print(f"The newest files are: {result_file}")