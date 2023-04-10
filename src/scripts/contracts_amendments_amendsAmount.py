import sys
sys.path.append('./src')
import helpers
BATCH_SIZE = 1000
QUERY_FILE_PATH = './Query.sql'


def process_row (row: tuple) -> tuple:
	amount_by_currency = {
		"USD": 0,
		"PYG": 0,
	}
	if row[1]:
		for contract in row[1]:
			if('amendments' in contract):
				for amendment in contract['amendments']:
					if('amendsAmount' in amendment):
						currency = amendment['amendsAmount']['currency']
						amount_by_currency[currency] += amendment['amendsAmount']['amount']
	return (row[0], amount_by_currency["PYG"], amount_by_currency["USD"])

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