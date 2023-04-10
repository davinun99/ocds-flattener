import psycopg2
import settings
import helpers
import sys

con = None
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
try:
	con = psycopg2.connect(
		host = settings.dbHost, 
		port = settings.dbPort,
		database = settings.dbDatabase, 
		user = settings.dbUser, 
		password = settings.dbPassword
	)
except Exception as ex:
	print('\nException while connecting to db')
	print(ex)
	print('\n')
	exit()

def process_row (row: tuple) -> tuple:
	countArr = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	if row[1]:
		for contract in row[1]:
			if('guarantees' in contract):
				for guarantee in contract['guarantees']:
					ind = guarantee_type_map[guarantee['obligations']]
					countArr[ind] += 1
	return (row[0], countArr)


def generate_csv_batch(record_count: int) -> None:
	query = helpers.read_query_from_file(QUERY_FILE_PATH) + " ORDER BY r.ocid ASC LIMIT {0} OFFSET {1}"
	records_processed = 0
	offset = 0
	query = query.format(BATCH_SIZE, offset)
	cursor = con.cursor()
	while records_processed < record_count:
		print('init', query, offset)
		cursor.execute(query.format(BATCH_SIZE, offset))
		rows = cursor.fetchall()
		print(rows[0])
		records_processed += len(rows)
		# print(records_processed)
		offset += BATCH_SIZE
		# print('end', query, offset)
	print(records_processed)

def get_rows() -> list[tuple]:
	query = helpers.read_query_from_file(QUERY_FILE_PATH)
	cursor = con.cursor()
	cursor.execute(query)
	rows = cursor.fetchall()
	return rows

def main(arguments):
	cursor = con.cursor()
	cursor.execute('''SELECT count(*) FROM data;''')
	record_count_row = cursor.fetchone()
	
	record_count = 0
	if record_count_row:
		record_count = record_count_row[0]
	
	print(f'\n{record_count} records found\n')
	for row in get_rows():
		idArr = process_row(row)
		print(idArr)
	# print(rows[0])

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))