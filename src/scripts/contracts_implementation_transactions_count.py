import sys
sys.path.append('./src')
import helpers
BATCH_SIZE = 1000
QUERY_FILE_PATH = './Query.sql'


def process_row (row: tuple, colNumber: int) -> int:
	count = 0
	if row[colNumber]:
		for contract in row[colNumber]:
			if('implementation' in contract):
				if('transactions' in contract['implementation']):
					count += len(contract['implementation']['transactions'])
	return count

def main(arguments):
	query = """
		SELECT
			data['compiledRelease']['ocid'] as "id",
			data['compiledRelease']['contracts'] as "contracts"
		FROM RECORD r join data d on d.id = r.data_id
	"""
	# for row in helpers.get_rows(query):
	# 	idArr = process_row(row)
	# 	print(idArr)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))