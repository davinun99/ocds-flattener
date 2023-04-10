import sys
sys.path.append('./src')
import helpers

BATCH_SIZE = 1000
QUERY_FILE_PATH = './Query.sql'
COUNT_MAP_FILENAME = 'saved_count_map.pkl'

count_map = {}
index_map = {}

def load_count_map(row: tuple) -> int:
	count = 0
	if row[1]:
		if('items' in row[1]):
			for item in row[1]['items']:
				if('classification' in item):
					id = item['classification']['id'][0:2]
					if id in count_map:
						count_map[id] += 1
					else:
						count_map[id] = 1
					count += 1
	return count

def get_count_and_load_map(rows: list[tuple]) -> int:
	total_count: int = 0
	for row in rows:
		total_count += load_count_map(row)
	return total_count
	
def load_indexed_map(counted_map: dict, total_count: int):
	index_c = 0
	for (id, _) in counted_map.items():
		index_map[id] = index_c
		index_c += 1

def process_row(row: tuple):
	idArr = [0] *( len(list(index_map)) + 1 )
	if row[1]:
		if('items' in row[1]):
			for item in row[1]['items']:
				if('classification' in item):
					id = item['classification']['id'][0:2]
					index = index_map[id]
					idArr[index] += 1
	return idArr

def print_dict(file_name:str, dict: dict):
	with open(f'__out/{file_name}', 'w') as f:
		sys.stdout = f # Change the standard output to the file we created.
		# print('This message will be written to a file.')
		for (a, b) in dict.items():
			print(a, ',', b)
		sys.stdout = sys.__stdout__ # Reset

def main(arguments):
	query = """
		SELECT
			data['compiledRelease']['ocid'] as "id",
			data['compiledRelease']['tender'] as "tender"
		FROM RECORD r join data d on d.id = r.data_id
	"""
	rows = helpers.get_rows(query)
	total_count = get_count_and_load_map(rows)
	print_dict('counted_map.txt', count_map)

	sorted_by_count = sorted(count_map.items(), key=lambda x:x[1], reverse=True) #reverse True to really work
	converted_dict = dict(sorted_by_count)
	
	print_dict('sorted_counted_map.txt', converted_dict)
	
	load_indexed_map(converted_dict, total_count)

	print_dict('all_values_map.txt', index_map)

	for row in rows:
		idArr = process_row(row)
		print(row[0], ',', idArr)
	
	
if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))