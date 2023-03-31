import sys
sys.path.append('./src')
import helpers
BATCH_SIZE = 1000

map = {
	"fonacide": 0,
	"produccion_nacional": 1,
	"urgencia_impostergable": 2,
	"adreferendum": 3,
	"agricultura_familiar": 4,
	"covid_19": 5,
	"almuerzo_escolar": 6,
	"seguridad_nacional": 7,
}

def process_row (row: tuple) -> tuple:
	countArr = [0] * len(list(map))
	if row[1]:
		if('coveredBy' in row[1]):
			for cover in row[1]['coveredBy']:
				ind = map[cover]
				countArr[ind] += 1
	return (row[0], countArr)

def main(arguments):
	query = """
		SELECT
			data['compiledRelease']['ocid'] as "id",
			data['compiledRelease']['tender'] as "tender"
		FROM RECORD r join data d on d.id = r.data_id
	"""
	for row in helpers.get_rows(query):
		idArr = process_row(row)
		print(idArr)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))