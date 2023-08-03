import sys
sys.path.append('./src')
import helpers
BATCH_SIZE = 1000

map_data = {
	"Adjudicado": 0,
    "Confirmado Orden de Compra": 1,
    "Orden de compra recibida": 2,
    "Orden de compra entregada": 3,
    "Cancelado": 4,
    "Cancelada de la Orden de Compra": 5,
    "Vencida Orden de Compra": 6,
    "Suspendido": 7,
    "Anulado": 8,
}

def process_row (row: tuple, colNumber: int):
	countArr = [0] * len(list(map_data))
	if row[colNumber]:
		for contract in row[colNumber]:
			if('statusDetails' in contract):
				try:
					ind = map_data[contract['statusDetails']]
					countArr[ind] += 1
				except Exception as e:
					print('Exception:: ')
					print(e)
					print(e.with_traceback(None))
	return ";;;".join(map(str, countArr))

def main(arguments):
	query = """
		SELECT
			data['compiledRelease']['ocid'] as "id",
			data['compiledRelease']['awards'] as "contracts"
		FROM RECORD r join data d on d.id = r.data_id
	"""
	# for row in helpers.get_rows(query):
	# 	idArr = process_row(row)
	# 	print(idArr)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))