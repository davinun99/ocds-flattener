import sys
sys.path.append('./src')
import pickle
import helpers

BATCH_SIZE = 1000
QUERY_FILE_PATH = './Query.sql'
COUNT_MAP_FILENAME = 'saved_count_map.pkl'

count_map = {}
index_map = {}

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


def get_count_map(rows: list) -> dict:
	try: # try to load saved count map
		print('Trying to load saved count map')
		with open(COUNT_MAP_FILENAME, 'rb') as f:
			count_map = pickle.load(f)
			print('Loaded saved count map')
			return count_map
	except:
		count_map: dict = {}
		total_count: int = 0
		print('No saved count map found')

	for row in rows:
		total_count += load_count_map(row)
	
	try:
		with open(COUNT_MAP_FILENAME, 'wb') as f:
			pickle.dump(count_map, f)
			print('Saved count map')
	except:
		print('Could not save count map')
	
	# print(count_map)
	return count_map
	


def main(arguments):
	query = """
		SELECT
			data['compiledRelease']['ocid'] as "id",
			data['compiledRelease']['awards'] as "awards"
		FROM RECORD r join data d on d.id = r.data_id
	"""
	rows = helpers.get_rows(query)
	counted_map = get_count_map(rows)
	
	sorted_by_count = sorted(counted_map.items(), key=lambda x:x[1], reverse=True) #reverse True to really work
	converted_dict = dict(sorted_by_count)

	converted_dict

	
	
	
if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
    
# get all values with counts
# get 25 %
# get 50 %
# get 75 %
# get 100 %
# iterate through all values and get the count with quantiles

# map to array