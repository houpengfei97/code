from shutil import copyfile
import os
import time

source = input("Enter source path:")
target = input("Enter target path:")

def server():
	filenames = os.listdir(source)
	for i,filename in enumerate(filenames):
		print('Copying file () into net dir...{}/{}'.format(filename,i+1,len(filenames)))
		copyfile(source + filename,target + filename)
		print('Copied file () into net dir...{}/{}'.format(filename, i+1, len(filenames)))

	while os.path.exists(target + filename):
		time.sleep(3)
	print('transferred {} into client. {}/{}'.format(filename, i + 1, len(filenames)))

if __name__ == '__main__':
	server()