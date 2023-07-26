import sys
sys.path.append('./src')
import helpers

BATCH_SIZE = 1000
QUERY_FILE_PATH = './Query.sql'

count_map = {}

first_quantile: dict = {}
second_quantile = {}
third_quantile = {}	

class AwardSuppliers:
	def __init__(self, rows: list[tuple], colNumber:int):
		self.rows = rows
		self.colNumber = colNumber
		self.count_map = {}

		self.first_quantile = {}
		self.second_quantile = {}
		self.third_quantile = {}
		
		total_count = self.get_count_and_load_map(rows)
		# print_dict('counted_map.txt', count_map)

		sorted_by_count = sorted(self.count_map.items(), key=lambda x:x[1], reverse=True) #reverse True to really work
		converted_dict = dict(sorted_by_count)

		# print_dict('sorted_counted_map.txt', converted_dict)
		
		self.load_quartiles(converted_dict, total_count)

		# print_dict('first_quartile.txt', first_quantile)
		# print_dict('second_quartile.txt', second_quantile)
		# print_dict('third_quartile.txt', third_quantile)

	def load_count_map(self, row: tuple) -> int:
		supplier_ids = set()
		count = 0
		if row[self.colNumber]:
			for award in row[self.colNumber]:
				if('suppliers' in award):
					for supplier in award['suppliers']:
						id = supplier['id']
						supplier_ids.add(id)
		for id in supplier_ids:
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
	
	def load_quartiles(self, counted_map: dict, total_count: int):
		count = 0
		for (id, appearances_count) in counted_map.items():
			if count <= total_count * 0.25:
				self.first_quantile[id] = appearances_count
			elif count <= total_count * 0.5:
				self.second_quantile[id] = appearances_count
			elif count <= total_count * 0.75:
				self.third_quantile[id] = appearances_count
			count += appearances_count


	def process_row(self, row: tuple, colNumber: int):
		idArr = [0, 0, 0, 0]
		supplier_ids = set()
		if row[colNumber]:
			for award in row[colNumber]:
				if('suppliers' in award):
					for supplier in award['suppliers']:
						id = supplier['id']
						supplier_ids.add(id)
		for id in supplier_ids:
			if id in self.first_quantile:
				idArr[0] += 1
			elif id in self.second_quantile:
				idArr[1] += 1
			elif id in self.third_quantile:
				idArr[2] += 1
			else:
				idArr[3] += 1
		return ";;;".join(map(str, idArr))

def print_dict(file_name:str, dict: dict):
	with open(f'__out/{file_name}', 'w') as f:
		sys.stdout = f # Change the standard output to the file we created.
		# print('This message will be written to a file.')
		for (a, b) in dict.items():
			print(a, ',', b)
		sys.stdout = sys.__stdout__ # Reset

# get all values with counts
# get 25 %
# get 50 %
# get 75 %
# get 100 %
# iterate through all values and get the count with quantiles

# map to array