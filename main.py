from code_density import *
from source_code import * 
from window_analyzer import *

def main():
	path = 'reviews/perfect.py'
	source_code = all_source_code(path)
	LOC =  get_LOC(source_code)
	CLOC = get_CLOC(source_code)
	CD = get_code_density(CLOC, LOC)
	windows = make_windows(path, 20)

	part_dict = code_density_per_window(windows)

	print 'CD over hele file:', CD
	for k,v in part_dict.items():
		print '========================='
		print '========================='
		print v['Part']

if __name__ == '__main__':
	main()
