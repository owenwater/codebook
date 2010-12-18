import sys
def get_file_name(s):
	#remove the first "file: " and blanl
	return s.partition("file:")[2].strip()
		
def perror(line_num,  name, msg):
	sys.stderr.write("merge "+str(line_num)+": error: "+msg+"\n")
	sys.stderr.write("merge: skip the program: "+name[0]+"\n")
	return -2

if __name__=="__main__":
	fp_index = open("list")
	index = fp_index.readlines()
	fp_index.close()
	fp_code = 0
	cnt = 0
	part_line_num = -1
	whole_line_num = 0
	current_name = []
	error_list = []
	in_comment = False

	fp_output = open("codebook" , "w")

	for line in index:
		whole_line_num += 1
		line = line.strip()
		if part_line_num == -1 and line == "":
			#escape the blank
			continue
		elif part_line_num == -1:
			#start
			fp_output.write("/*\n");
			fp_output.write(line+"\n")
			in_comment = True
			part_line_num += 1
			current_name = line, whole_line_num
		elif part_line_num == 0:
			#get the file name and open it
			if "file:" not in line:
				part_line_num = perror(whole_line_num, \
						current_name, "doesn't find file name")
				continue
			#open file
			try:
				file_name = get_file_name(line)
				fp_code = open(file_name)
			except IOError:
				part_line_num = perror(whole_line_num, \
						current_name, "can't open code file: \""
						+file_name+"\"")
				continue
			part_line_num += 1
		elif part_line_num == 1 and line != "-":
			#print code program describe
			fp_output.write(line+"\n")
		elif part_line_num == 1:
			#print code and end
			fp_output.write("*/\n\n")
			in_comment = False
			part_line_num = -1
			code = fp_code.readlines()
			#print code
			print_code = False
			for line_code in code:
				if line_code.strip() == "/*codebook start*/":
					print_code = True
				elif line_code.strip() == "/*codebook end*/":
					print_code = False
				elif print_code:
					fp_output.write(line_code)
			fp_code.close()
		elif part_line_num == -2:
			if line == "-":
				part_line_num = -1
				if in_comment:
					in_comment = False
					fp_output.write("*/\n")

	if (part_line_num != -1):
		perror(whole_line_num, current_name, "missing a \"-\"")
		if in_comment:
			in_comment = False
			fp_output.write("*/\n")
	fp_output.close()


	
