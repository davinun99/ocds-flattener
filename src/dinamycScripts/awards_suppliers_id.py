import sys
sys.path.append('./src')
import helpers

BATCH_SIZE = 1000
QUERY_FILE_PATH = './Query.sql'
COUNT_MAP_FILENAME = 'saved_count_map.pkl'

count_map = {}
index_map = {}

first_quantile: dict = {}
second_quantile = {}
third_quantile = {}	

def load_count_map(row: tuple) -> int:
	supplier_ids = set()
	count = 0
	if row[1]:
		for award in row[1]:
			if('suppliers' in award):
				for supplier in award['suppliers']:
					id = supplier['id']
					supplier_ids.add(id)
	for id in supplier_ids:
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
	
def load_quartiles(counted_map: dict, total_count: int):
	count = 0
	for (id, appearances_count) in counted_map.items():
		if count <= total_count * 0.25:
			first_quantile[id] = appearances_count
		elif count <= total_count * 0.5:
			second_quantile[id] = appearances_count
		elif count <= total_count * 0.75:
			third_quantile[id] = appearances_count
		count += appearances_count

def process_row(row: tuple):
	idArr = [0, 0, 0, 0]
	supplier_ids = set()
	if row[1]:
		for award in row[1]:
			if('suppliers' in award):
				for supplier in award['suppliers']:
					id = supplier['id']
					supplier_ids.add(id)
	for id in supplier_ids:
		if id in first_quantile:
			idArr[0] += 1
		if id in second_quantile:
			idArr[1] += 1
		if id in third_quantile:
			idArr[2] += 1
		if id in count_map:
			idArr[3] += 1
	return idArr

def print_dict(file_name:str, dict: dict):
	with open(f'out/{file_name}', 'w') as f:
		sys.stdout = f # Change the standard output to the file we created.
		# print('This message will be written to a file.')
		for (a, b) in dict.items():
			print(a, ',', b)
		sys.stdout = sys.__stdout__ # Reset

def main(arguments):
	query = """
		SELECT
			data['compiledRelease']['ocid'] as "id",
			data['compiledRelease']['awards'] as "awards"
		FROM RECORD r join data d on d.id = r.data_id
	"""
	rows = helpers.get_rows(query)
	total_count = get_count_and_load_map(rows)
	print_dict('counted_map.txt', count_map)

	sorted_by_count = sorted(count_map.items(), key=lambda x:x[1], reverse=True) #reverse True to really work
	converted_dict = dict(sorted_by_count)
	
	print_dict('sorted_counted_map.txt', converted_dict)
	
	load_quartiles(converted_dict, total_count)

	print_dict('first_quartile.txt', first_quantile)
	print_dict('second_quartile.txt', second_quantile)
	print_dict('third_quartile.txt', third_quantile)

	for row in rows:
		idArr = process_row(row)
		print(row[0], ',', idArr)
	
	
if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
    
# get all values with counts
# get 25 %
# get 50 %
# get 75 %
# get 100 %
# iterate through all values and get the count with quantiles

# map to array