#Quincy Mattor
#4/28?/22
#programming for it
#main for folders project


import sys
from reading_dirs import *
from analyze import *


prgm = ""

if len(sys.argv) > 1:
	master = sys.argv[1]	#prgm passed through command line

	list = read_from_dir(master)

	for command in list:
		# print(master + "/" + command)
		try:
			prgm += analyze_command(master + "/" + command, 0)
		except:
			print("COMPILE ERROR, FOLDER:" + command)

	try:
		exec(prgm)
	except:
		print("RUN TIME ERROR")