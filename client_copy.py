from shutil import copyfile
import os
import time

source = input("Enter source path:")
target = input("Enter target path:")

def client():
	while True:
		filenames = os.listdir(source)

		for i,filename in enumerate(filenames):
			print('Copying file () into base dir...{}/{}'.format(filename, i + 1, len(filenames)))
			copyfile(source + filename, target + filename)
			print('Copied file () into base dir...{}/{}'.format(filename, i + 1, len(filenames)))
			os.remove(source + filename)
			print('download {} into client. {}/{}'.format(filename, i + 1, len(filenames)))
		if os.path.exists(source + filename):
			continue
		else:
			break

	time.sleep(3)
if __name__ == '__main__':
		client()