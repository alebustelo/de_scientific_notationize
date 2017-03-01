# Alejandro Bustelo
# 3/1/2017
# Input: a text file with output from a MATLAB vector copied from the workspace in scientific notation
# Output: a text file with comma-delimited numbers formatted as the arguments of a C-style array of floats with precision to 30 decimal places


import re
import os


with open("input.txt", "r") as f:
	data = f.readlines()

for line in data:
	numbers = line.split(",")

intermediate = []
output = []
for num in numbers:
	intermediate = re.split("e", num)
	
	if len(intermediate) > 1:
		output.append('{0:.30f}'.format(float(intermediate[0])*10**(int(intermediate[1]))))
	else:
		output.append('{0:.30f}'.format(float(intermediate[0])))
	#print output[-1] #debugging

with open("output.txt", "w") as f:
	f.write("{")
	for num in output:
		f.write(num)
		f.write(",")
	f.seek(-1, os.SEEK_END) #remove last comma
	f.truncate()
	f.write("}")
