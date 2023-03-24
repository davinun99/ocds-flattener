import sys
sys.path.append('./src')
import helpers
BATCH_SIZE = 1000
QUERY_FILE_PATH = './Query.sql'


def process_row (row: tuple) -> tuple:
	amendmentsCount = 0
	if row[1]:
		for contract in row[1]:
			if('amendments' in contract):
				amendmentsCount += len(contract['amendments'])
	return (row[0], amendmentsCount)

def main(arguments):
	query = """
		SELECT
			data['compiledRelease']['ocid'] as "id",
			data['compiledRelease']['contracts'] as "contracts"
		FROM RECORD r join data d on d.id = r.data_id
	"""
	for row in helpers.get_rows(query):
		idArr = process_row(row)
		print(idArr)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))