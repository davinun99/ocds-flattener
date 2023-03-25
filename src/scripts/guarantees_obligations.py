import sys
sys.path.append('./src')
import helpers
BATCH_SIZE = 1000
QUERY_FILE_PATH = './Query.sql'

guarantee_type_map = {
	"fulfillment": 0,
	"Endoso - Fiel Cumplimiento": 1,
	"Endoso - Anticipo": 2,
	"Accidentes Personales": 3,
	"Todo Riesgos en Zona de Obras": 4,
	"Anticipo": 5,
	"Responsabilidad Civil General": 6,
	'Endoso - Accidentes Personales': 7,
	"Daños a Terceros": 8,
	"Responsabilidad Profesional": 9,
	"Endoso - Todo Riesgos en Zona de Obras": 10,
	"Endoso - Responsabilidad Civil General": 11,
	"Fondo de Reparo": 12,
	"Deshonestidad": 13,
	"Endoso - Daños a Terceros": 14,
	"Endoso - Responsabilidad Profesional": 15,
	"Endoso - Deshonestidad": 16,
	"Endoso - Fondo de Reparo": 17,
}

def process_row (row: tuple) -> tuple:
	countArr = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	if row[1]:
		for contract in row[1]:
			if('guarantees' in contract):
				for guarantee in contract['guarantees']:
					ind = guarantee_type_map[guarantee['obligations']]
					countArr[ind] += 1
	return (row[0], countArr)

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