Author	: owen_water
Version	: 0.1
Email	: owen200104@gmail.com
Webpage : https://github.com/owenwater/codebook

Get the lastest version via:
git://github.com/owenwater/codebook.git

How to use it:
Get the printable version of the codebook:
	make
	-It will merge all files in the list and write to file "codebook".

Get the the codebook with auto highlight:
	make copy
	-It will copy "codebook"to "codebook.cpp".


How to add your own code into this codebook:
	0)programing...
	1)mark the part of your code will be put into codebook.
	2)add your code's name and description into file "list".

How to mark your program:
	Only the part which between tag:
		/*codebook start*/ and /*codebook end*/
	will be put into codebook.
	There can be multiple pairs of tags and the last ending-tag is not
	necessary.
	-See more details in sample_code.

How to modify list file:
	the format of each chunk:
	
[chunk-name]
	file:[program-file-name]
	[
		The description of program
	]
-

	The chunk-name and description will be put into codebook as comment
	Each chunk MUST end with '-'
	The blank line outside the chunk will be ignore
	No blank line allowed between the first and second line in each chunk.
	All prefix and suffix will be ignore.
	-See more details in sample_list

TODO LIST:
	0) output the codebook as a latex file.
	1) make an index of the codebook which can let the user manage their
	   codes more easily, incluing:
	   1.a) Change the order of codes.
	   1.b) classify the codes.
