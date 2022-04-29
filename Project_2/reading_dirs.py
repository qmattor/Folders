#Quincy Mattor
#3/24/22
#programming for IT
#Defining read functions for the folders interperter project

import os

def read_from_dir(url):
	list = os.listdir(url)
	list = sort_folders(list)
	return list


#sort by alphebetical order (not sure if leaving up to "whatever the placement might be" is a great idea, plus wikipedia said to)
def sort_folders(list):
	new_list = list.sort()
	return (list)


def num_sub(folder, path):
	list = read_from_dir(path + "/" + folder)
	return len(list)
