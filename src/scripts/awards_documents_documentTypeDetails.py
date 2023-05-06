import sys
sys.path.append('./src')
import helpers
BATCH_SIZE = 1000

map = {
	"Informe de Evaluación": 0,
	"Notificación al Oferente": 1,
	"Resolución de Adjudicación": 2,
	"Cuadro Comparativo de Ofertas": 3,
	"Acta de Apertura": 4,
	"Nota de Observacion": 5, 
	"Otros - Exp. por Decreto 5174": 6,
	"Nota de Cancelación Adjudicación": 7,
	"Resolución de Cancelación Adjudicación": 8,
	"Resolución de Ratificación": 9,
	"Nota de Retención Adjudicación": 10,
	"Nota de Contestación": 11,
	"Nota de Observacion Adjudicacion": 12,
	"Orden de Compra o Contrato": 13,
	"Nota al Director": 14,
	"Nota de Suspensión": 15,
	"Nota Rechazo Solicitud de Cancelacion": 16,
}

def process_row (row: tuple, colNumber: int) -> list[int]:
	countArr = [0] * len(list(map))
	if row[colNumber]:
		for award in row[colNumber]:
			if('documents' in award):
				for document in award['documents']:
					if 'documentTypeDetails' in document:
						ind = map[document['documentTypeDetails']]
						countArr[ind] += 1
	return countArr

def main(arguments):
	query = """
		SELECT
			data['compiledRelease']['ocid'] as "id",
			data['compiledRelease']['awards'] as "awards"
		FROM RECORD r join data d on d.id = r.data_id
	"""
	# for row in helpers.get_rows(query):
	# 	idArr = process_row(row)
	# 	print(idArr)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))