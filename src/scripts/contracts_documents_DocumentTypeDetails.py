import sys
sys.path.append('./src')
import helpers
BATCH_SIZE = 1000

map = {
	"Orden de Compra o Contrato": 0,
	"Nota de Aclaración": 1,
	"Nota de Observacion": 2,
	"Nota de Contestación": 3,
	"Resolución Rescisión": 4,
	"Nota de Retención Adjudicación": 5, 
	"CDP Proveedor": 6,
	"Anexo Adjudicación": 7,
}

def process_row (row: tuple, colNumber: int) -> list[int]:
	countArr = [0] * len(list(map))
	if row[colNumber]:
		for contract in row[colNumber]:
			if('documents' in contract):
				for document in contract['documents']:
					if 'documentTypeDetails' in document:
						ind = map[document['documentTypeDetails']]
						countArr[ind] += 1
	return countArr

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