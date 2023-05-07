import sys
sys.path.append('./src')

BATCH_SIZE = 1000
QUERY_FILE_PATH = './Query.sql'
COUNT_MAP_FILENAME = 'saved_count_map.pkl'

class N1_1PlanningItemsClassification:
	def load_count_map(self, row: tuple) -> int:
		count = 0
		if row[self.colNumber]:
			if('items' in row[self.colNumber]):
				for item in row[self.colNumber]['items']:
					if('classification' in item):
						id = item['classification']['id'][0:2]
						if id in self.count_map:
							self.count_map[id] += 1
						else:
							self.count_map[id] = 1
						count += 1
		return count

	def get_count_and_load_map(self, rows: list[tuple]) -> int:
		total_count: int = 0
		for row in rows:
			total_count += self.load_count_map(row)
		return total_count
		
	def load_indexed_map(self, counted_map: dict, ):
		index_c = 0
		for (id, _) in counted_map.items():
			self.index_map[id] = index_c
			index_c += 1

	def process_row(self, row: tuple, colNumber: int):
		idArr = [0] *( len(list(self.index_map)) + 1 )
		if row[colNumber]:
			if('items' in row[colNumber]):
				for item in row[colNumber]['items']:
					if('classification' in item):
						id = item['classification']['id'][0:2]
						index = self.index_map[id]
						idArr[index] += 1
		return idArr

	def print_dict(self, file_name:str, dict: dict):
		with open(f'__out/{file_name}', 'w') as f:
			sys.stdout = f # Change the standard output to the file we created.
			# print('This message will be written to a file.')
			for (a, b) in dict.items():
				print(a, ',', b)
			sys.stdout = sys.__stdout__ # Reset

	def __init__(self, rows: list[tuple], colNumber: int):
		self.colNumber = colNumber
		self.count_map = {}
		self.index_map = {}

		total_count = self.get_count_and_load_map(rows)
		sorted_by_count = sorted(self.count_map.items(), key=lambda x:x[1], reverse=True) #reverse True to really work
		converted_dict = dict(sorted_by_count)
		
		self.load_indexed_map(converted_dict)