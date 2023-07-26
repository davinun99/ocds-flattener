import sys
sys.path.append('./src')

BATCH_SIZE = 1000
QUERY_FILE_PATH = './Query.sql'
COUNT_MAP_FILENAME = 'saved_count_map.pkl'

class TenderProcurementIntentionProcuringEntityId:
	def load_count_map(self, row: tuple) -> int:
		count = 0
		if row[self.colNumber]:
			if('procurementIntention' in row[self.colNumber]):
				procurementIntention = row[self.colNumber]['procurementIntention']
				value = procurementIntention['procuringEntity']['id']
				if value in self.count_map:
					self.count_map[value] += 1
				else:
					self.count_map[value] = 1
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
		if row[colNumber]:
			if('procurementIntention' in row[colNumber]):
				procurementIntention = row[colNumber]['procurementIntention']
				value = procurementIntention['procuringEntity']['id']
				if value in self.first_quantile:
					idArr[0] += 1
				elif value in self.second_quantile:
					idArr[1] += 1
				elif value in self.third_quantile:
					idArr[2] += 1
				else:
					idArr[3] += 1
		return ";;;".join(map(str, idArr))

	def print_dict(self, file_name:str, dict: dict):
		with open(f'__out/{file_name}', 'w') as f:
			sys.stdout = f # Change the standard output to the file we created.
			# print('This message will be written to a file.')
			for (a, b) in dict.items():
				print(a, ',', b)
			sys.stdout = sys.__stdout__ # Reset

	def __init__(self, rows: list[tuple], colNumber: int):
		self.colNumber = colNumber;
		self.count_map = {}
		self.first_quantile: dict = {}
		self.second_quantile = {}
		self.third_quantile = {}

		total_count = self.get_count_and_load_map(rows)
		sorted_by_count = sorted(self.count_map.items(), key=lambda x:x[1], reverse=True) #reverse True to really work
		converted_dict = dict(sorted_by_count)
		self.load_quartiles(converted_dict, total_count)
	