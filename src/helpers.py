import settings 
def read_query_from_file (file_path: str) -> str:
	"""
	Read the contents of a file and return it as a string.
	
	:param file_path: The path to the file you want to read
	:type file_path: str
	:return: A string
	"""
	data = ''
	with open(file_path, 'r') as file:
		data = file.read()
	return data

def get_rows(query: str) -> list[tuple]:
	if(settings.con is None):
		return []
	cursor = settings.con.cursor()
	cursor.execute(query)
	rows = cursor.fetchall()
	return rows