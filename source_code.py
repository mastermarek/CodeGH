def all_source_code(path):
	with open(path, 'r') as source:
		result = source.read()
	return result

def window_of_source_code(path, start, end):
	with open(path, 'r') as source:
		string_of_code = ''
		for i, line in enumerate(source):
			if (i < end) and (i > start):
				string_of_code += line

	return string_of_code
