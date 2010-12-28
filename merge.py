import sys
import copy
import os
from cache import Cache

class Merge(object):
	def get_file_name(self, s):
		"""remove the first "file: " and blanl
		"""
		return s.partition("file:")[2].strip()

	def open_file(self, file_name):
		"""open file
		"""
		try:
			fp_code = open(file_name)
			return fp_code
		except IOError:
			return self.perror(self.whole_line_num, \
					self.current_name, "can't open code file: \""\
					+file_name+"\"")
	def perror(self, line_num,  name, msg):
		"""print error
		"""
		sys.stderr.write("merge "+str(line_num)+": error: "\
				+msg+"\n")
		sys.stderr.write("merge: skip the program: "+name[0]+"\n")
		return -2

	def output(self, fp, s):
		fp.write(s)

	def move_in_comment(self, fp, in_comment):
		"""start print comments
		"""
		if not in_comment:
			in_comment = True
			self.output(fp, "/*\n")
		return in_comment

	def move_out_comment(self, fp, in_comment):
		"""stop print comments
		"""
		if in_comment:
			in_comment = False
			self.output(fp, "*/\n")
		return in_comment

	def output_code(self, fp, file_name, cache, print_flag = True):
		"""open code file and print it to fp
		"""
		fp_code = self.open_file(file_name);
		if fp_code == -2:
			return -2
		if not print_flag:
			return 0
		code = fp_code.readlines()
		print_code = False
		fp.write(cache.get())
		for line_code in code:
			if line_code.strip() == "/*codebook start*/":
				print_code = True
			elif line_code.strip() == "/*codebook end*/":
				print_code = False
			elif print_code:
				fp.write(line_code)
		fp_code.close()
		return 1

	def run(self, list_file_name = "list", output_file_name \
			= "codebook"):
		"""main function
		"""
		fp_index = open(list_file_name)
		index = fp_index.readlines()
		fp_index.close()
		fp_code = 0
		cnt = 0
		part_line_num = -1
		self.whole_line_num = 0
		self.current_name = []
		self.lib = {}
		in_comment = False

		fp_output = open(output_file_name , "w")
		self.cache = Cache()

		for line in index:
			self.whole_line_num += 1
			line = line.strip()
			if part_line_num == -1 and line == "":
				#escape the blank
				continue
			elif part_line_num == -1:
				#start
				self.cache.clear()
				in_comment = self.move_in_comment(self.cache, \
						in_comment)
				self.output(self.cache, line+"\n")
				part_line_num += 1
				self.current_name = line, self.whole_line_num
			elif part_line_num == 0:
				#get the file name and open it
				if "file:" not in line:
					part_line_num = self.perror(\
							self.whole_line_num, \
							self.current_name, \
							"doesn't find file name")
					continue
				file_name = self.get_file_name(line)
				#open file
				part_line_num += 1
			elif part_line_num == 1 and line != "-":
				#print code program describe
				self.output(self.cache, line+"\n")
			elif part_line_num == 1:
				#print code and end
				in_comment = self.move_out_comment(self.cache, \
						in_comment)
				self.output(self.cache, "\n")
				part_line_num = -1
				#print code
				rt = 0
				if not os.path.isfile(file_name):
					self.perror(self.whole_line_num, self.current_name, \
							"can't open code file: \""+file_name+"\"")
					rt = -2
				#TODO: using another way to check the file exist or not
				if rt >= 0:
					self.lib[self.current_name[0]] =\
							file_name, copy.deepcopy(self.cache)
			elif part_line_num == -2:
				if line == "-":
					part_line_num = -1
					in_comment = self.move_out_comment(\
							self.cache, in_comment)

		if (part_line_num != -1):
			self.perror(self.whole_line_num, self.current_name, \
					"missing a \"-\"")
			in_comment =  self.move_out_comment(\
					self.cache, in_comment)

		self.write(fp_output)

		fp_output.close()
	def write(self, fp):
		"""will print as file "index" future
		"""
		for ea in self.lib.values():
			self.output_code(fp, ea[0], ea[1] )

		

if __name__=="__main__":
	merge = Merge()
	merge.run()


	
