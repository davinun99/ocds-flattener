
QUERY_FILE_PATH = './Query.sql'
def read_query_from_file ():
	data = ''
	with open(QUERY_FILE_PATH, 'r') as file:
		data = file.read()
	return data