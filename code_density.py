from __future__ import division
import re

from source_code import *

def get_LOC(source):
	''' 
	Get lines of code in certain file: int
	Does not count blank lines or comment lines
	'''
	result = 0
	for line in source.splitlines():
		if (line.strip() != '') and not line.strip().startswith('#'):
			result += 1
	return result

def get_CLOC(source):
	'''
	Get amount of comments in certain file: int
	Does not count docstrings
	'''
	comments = re.findall(r'\#(.*)', source)
	return len(comments)

def get_code_density(CLOC, LOC):
	return CLOC / LOC

