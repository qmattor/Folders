#Quincy Mattor
#3/31/22
#programming for it
#anaylizing the folders and returning the proper python code back

from reading_dirs import *

#tabs out strings to properly place them in subroutines
def tab_out(str, tabs):
	ret = "\t" * tabs
	ret = ret + str
	return ret

'''
Commands

if			0 folders		Second sub-folder holds expression, third holds list of commands
while		1 folder		Second sub-folder holds expression, third holds list of commands
declare		2 folders		Second sub-folder holds type, third holds var name (in number of folders)
let			3 folders		Second holds var name (in number of folders), third holds expression
print		4 folders		Second sub-folder holds expression
input		5 folders		Second sub-folder holds var name
'''



#ifs and whiles
def if_statement(folder, num_tabs, flag):
	folders = read_from_dir(folder)
	ret = ""
	if flag == 0:											#solid code reuse imo
		ret = "if ("
	else:
		ret = "while ("
	ret += analyze_expr(folder + "/" + folders[1]) + "):\n"
	commands = folder + "/" + folders[2]
	tab_out(ret, num_tabs)
	for f in read_from_dir(commands):
		ret += analyze_command(commands + "/" + f, num_tabs + 1)
	return ret

'''
int		0 folders
float	1 folder
string	2 folders
char	3 folders
'''
#ig this declares variables? 
def declare_statement(folder):
	folders = read_from_dir(folder)
	typ = len(read_from_dir(folder + "/" + folders[1]))
	var = len(read_from_dir(folder + "/" + folders[2]))
	match typ:
		case 0:
			return "var" + str(var) + " = 0"
		case 1:
			return "var" + str(var) + " = 0"
		case 2:
			return "var" + str(var) + " = \"\""
		case 3:
			return "var" + str(var) + " = chr(0)"

def let_statement(folder):
	folders = read_from_dir(folder)
	return ("var" + str(num_sub(folders[1], folder)) + " = " + analyze_expr(folder + "/" + folders[2]) + "\n")


def print_statement(folder):
	return ("print(" + analyze_expr(folder + "/" + read_from_dir(folder)[1]) + ", end=\"\")\n")

def input_statement(folder):
	folders = read_from_dir(folder)
	var = num_sub(folders[1], folder)
	return "var"+ str(var) + " = input(\"\")\n"


#https://stackoverflow.com/questions/11479816/what-is-the-python-equivalent-for-a-case-switch-statement
#^^^ match statement code
def analyze_command(folder, num_tabs):							#folder is full path
	folders = read_from_dir(folder)
	match num_sub(folders[0], folder):							#folder 0 is command folder
		case 0:
			return if_statement(folder, num_tabs, 0)			#if
		case 1:
			return if_statement(folder, num_tabs, 1)			#while
		case 2:
			return tab_out(declare_statement(folder), num_tabs)
		case 3:
			return tab_out(let_statement(folder), num_tabs)
		case 4:
			return tab_out(print_statement(folder), num_tabs)
		case 5:
			return tab_out(input_statement(folder), num_tabs)
		case _:
			return "__COMMAND_ERROR__"



'''
Expressions

Variable		0 folders		Second sub-folder holds var name
Add				1 folder		Second sub-folder holds first expression to add, third holds second expression
Subtract		2 folders		Second sub-folder holds first expression to subtract, third holds second expression
Multiply		3 folders		Second sub-folder holds first expression to multiply, third holds second expression
Divide			4 folders		Second sub-folder holds first expression to divide, third holds second expression
Literal Value	5 folders		Second sub-folder holds the type of the value (eg two folders for a string), third holds the value
Equal To		6 folders		Second and third folders hold expressions to compare
Greater Than	7 folders		Second and third folders hold expressions to compare (returns true if the second folder holds a larger value than the third folder)
Less Than		8 folders		Second and third folders hold expressions to compare

*** NOTE: so I was reading thought the list of expressions and noticed that it's missing both greater than or equaled to
*** as well as less than or equaled to. On top of this it's missing an "and" or "or" boolean expression. I could actually
*** fix this quite easily, but I'm not going to to keep this legacy.
*** the fix would be simply to add a couple extra cases for the match statement so that 9 folders is "or" with second
*** sub folder being left, and third being right, etc for the rest.
'''



#Literal Value	5 folders		Second sub-folder holds the type of the value
#(eg two folders for a string), third holds the value

'''
int		0 folders
float	1 folder
string	2 folders
char	3 folders
'''

def hex_packet_reader(folder):
	folders = read_from_dir(folder)
	ret = ""
	for item in folders:
		if len(read_from_dir(folder + "/" + item)) == 1:
			ret += "1"
		else:
			ret += "0"
	return ret

def get_int(data):
	folders = read_from_dir(data)
	bin_val = hex_packet_reader(data + "/" + folders[0]) + hex_packet_reader(data + "/" + folders[1])
	return int(bin_val, 2)

def get_char(data):
	folders = read_from_dir(data)
	bin_val = hex_packet_reader(data + "/" + folders[0]) + hex_packet_reader(data + "/" + folders[1])
	return chr(int(bin_val, 2))



#don't use this, pretty sure it's broken, but I'm also not sure what "fixed" looks like
def get_str(data):
	string = read_from_dir(data)
	ret = ""
	string.pop(0)
	for thing in string:
		ret += get_char(data + "/" + thing)				#<-- ????? not sure how strings are formated
	return ret


#so funny story, they original version is in c# so I think that's why the typing is kinda wonky
def l_val(folder):
	folders = read_from_dir(folder)
	match len(read_from_dir(folder + "/" + folders[1])):
		case 0:
			return str(get_int(folder + "/" + folders[2]))					#funny story, because it's only one byte there
		case 1:																#aren't any values higher than 255 and no negatives
			#uhhhh flooaaatttsss, yessssss.... I know how to do that, definetly.....
			return str(get_int(folder + "/" + folders[2])) + ".0"			#so basically what I can tell is that floats r a lie
		case 2:																#they're just int's recast
			return "\"" + get_str(folder + "/" + folders[2]) + "\""			#my guess is that asking someone to not only understand 
		case 3:																#but impliment the mantis exp thing is too much
			return "\"" + str(get_char(folder + "/" + folders[2])) + "\""	#<-- yeahhhh..... char....


def analyze_expr(folder):
	folders = read_from_dir(folder)
	typ = len(read_from_dir(folder + "/" + folders[0])) #first sub has type
	if typ == 0:										#special cases
		return "var" + str(num_sub(folders[1], folder))
	if typ == 5:
		return  str(l_val(folder))


	eprs1 = analyze_expr(folder + "/" + folders[1])
	eprs2 = analyze_expr(folder + "/" + folders[2])
	match typ:
		case 1:
			return ("(" + eprs1 + "+" + eprs2 + ")")		#I don't think the parenthises are nessicary,
		case 2:												#but I'm adding them anyways
			return ("(" + eprs1 + "-" + eprs2 + ")")
		case 3:
			return ("(" + eprs1 + "*" + eprs2 + ")")
		case 4:
			return ("(" + eprs1 + "/" + eprs2 + ")")
		case 6:
			return ("(" + eprs1 + "==" + eprs2 + ")")
		case 7:
			return ("(" + eprs1 + ">" + eprs2 + ")")
		case 8:
			return ("(" + eprs1 + "<" + eprs2 + ")")
		case _:
			return "__EXPR_ERROR__"
