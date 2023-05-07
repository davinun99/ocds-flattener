import sys
sys.path.append('./src')
import helpers

BATCH_SIZE = 1000
QUERY_FILE_PATH = './Query.sql'
COUNT_MAP_FILENAME = 'saved_count_map.pkl'

count_map = {}
index_map = {}

main_map_70: dict = {}

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
	
def load_70(counted_map: dict, total_count: int):
	count = 0
	index_c = 0
	for (id, appearances_count) in counted_map.items():
		if count <= total_count * 0.7:
			main_map_70[id] = index_c
			index_c += 1
		else:
			break
		count += appearances_count

def process_row(row: tuple):
	idArr = [0] *( len(list(main_map_70)) + 1 )
	if row[1]:
		if('items' in row[1]):
			for item in row[1]['items']:
				if('classification' in item):
					id = item['classification']['id'][0:2]
					if id in main_map_70:
						index = main_map_70[id]
						idArr[index] += 1
					else:
						idArr[-1] += 1
					
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
			data['compiledRelease']['planning'] as "planning"
		FROM RECORD r join data d on d.id = r.data_id
	"""
	rows = helpers.get_rows(query)
	total_count = get_count_and_load_map(rows)
	print_dict('counted_map.txt', count_map)

	sorted_by_count = sorted(count_map.items(), key=lambda x:x[1], reverse=True) #reverse True to really work
	converted_dict = dict(sorted_by_count)
	
	print_dict('sorted_counted_map.txt', converted_dict)
	
	load_70(converted_dict, total_count)

	print_dict('70%.txt', main_map_70)

	for row in rows:
		idArr = process_row(row)
		print(row[0], ',', idArr)
	
	
if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))