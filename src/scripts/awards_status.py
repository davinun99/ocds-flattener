import sys
sys.path.append('./src')
import helpers
BATCH_SIZE = 1000

map = {
	"active": 0,
	"cancelled": 1,
	"pending": 2,
}

def process_row (row: tuple) -> tuple:
	countArr = [0] * len(list(map))
	if row[1]:
		for award in row[1]:
			if 'status' in award:
				ind = map[award['status']]
				countArr[ind] += 1
	return (row[0], countArr)

def main(arguments):
	query = """
		SELECT
			data['compiledRelease']['ocid'] as "id",
			data['compiledRelease']['awards'] as "awards"
		FROM RECORD r join data d on d.id = r.data_id
	"""
	for row in helpers.get_rows(query):
		idArr = process_row(row)
		print(idArr)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))