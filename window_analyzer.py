from source_code import *
from code_density import *

def make_windows(path, part_size):
	'''
	Returns a list of all windows based on given part size: list
	'''
	start = 0
	end = part_size
	file_size = all_source_code(path).count('\n') + 1

	# Rounded down (only take parts that are as big as the part size)
	amount_of_loops = file_size / part_size
	windows = []

	for i  in range(0, amount_of_loops):
		window = window_of_source_code(path, start, end)
		windows.append(window)
		start += part_size
		end += part_size

	return windows

def code_density_per_window(windows):
	'''
	Code density per code part. Returns a dict with unique ID, Codeblock and
	Code density --> dict = {1: {'CD': 0.1, 'Part': '<code>'}}
	'''
	densities_per_window = {}
	for i, code_part in enumerate(windows):
		LOC = get_LOC(code_part)
		CLOC = get_CLOC(code_part)
		densities_per_window[i] = {
			'CD': get_code_density(CLOC, LOC),
			'Part': code_part
		}
	return densities_per_window