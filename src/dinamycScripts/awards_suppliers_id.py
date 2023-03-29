import sys
sys.path.append('./src')
import pickle
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
	count = 0
	if row[1]:
		for award in row[1]:
			if('suppliers' in award):
				for supplier in award['suppliers']:
					id = supplier['id']
					count += 1
					if id in count_map:
						count_map[id] += 1
					else:
						count_map[id] = 1
	return count


def get_count_map_and_count(rows: list[tuple]) -> tuple[dict, int]:
	count_map: dict = {}
	total_count: int = 0
	for row in rows:
		total_count += load_count_map(row)
	return (count_map, total_count)
	
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
	if row[1]:
		for award in row[1]:
			if('suppliers' in award):
				for supplier in award['suppliers']:
					id = supplier['id']
					if id in first_quantile:
						idArr[0] += 1
					elif id in second_quantile:
						idArr[1] += 1
					elif id in third_quantile:
						idArr[2] += 1
					else:
						idArr[3] += 1
	return idArr

def main(arguments):
	query = """
		SELECT
			data['compiledRelease']['ocid'] as "id",
			data['compiledRelease']['awards'] as "awards"
		FROM RECORD r join data d on d.id = r.data_id
	"""
	rows = helpers.get_rows(query)
	(counted_map, total_count) = get_count_map_and_count(rows)
	sorted_by_count = sorted(counted_map.items(), key=lambda x:x[1], reverse=True) #reverse True to really work
	converted_dict = dict(sorted_by_count)
	load_quartiles(converted_dict, total_count)
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