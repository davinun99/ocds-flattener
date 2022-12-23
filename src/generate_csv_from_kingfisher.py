import psycopg2
import settings
import helpers
import sys

con = None
BATCH_SIZE = 100
QUERY_FILE_PATH = './Query.sql'

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
	# 65 data['compiledRelease']['parties'] as "parties", --IS AN ARRAY
	# 66 data['compiledRelease']['planning'] as "planning", --IS AN ARRAY
	# 67 data['compiledRelease']['tender']['items'] as "tender.items", --IS AN ARRAY
	# 68 data['compiledRelease']['tender']['additionalProcurementCategories'] as "tender.additionalProcurementCategories", --IS AN ARRAY
	# 69 data['compiledRelease']['tender']['submissionMethod'] as "tender.submissionMethod",
	# 70 data['compiledRelease']['tender']['tenderers'] as "tender.tenderers", --IS AN ARRAY
	# 71 data['compiledRelease']['tender']['documents'] as "tender.documents", --IS AN ARRAY FLATTENIZADO 2.1
	# 72 data['compiledRelease']['tender']['amendments'] as "tender.amendments", --IS AN ARRAY
	# 73 data['compiledRelease']['tender']['lots'] as "tender.lots", --IS AN ARRAY
	# 74 data['compiledRelease']['tender']['enquiries'] as "tender.enquiries", --IS AN ARRAY
	# 75 data['compiledRelease']['tender']['notifiedSuppliers'] as "tender.notifiedSuppliers", --IS AN ARRAY
	# 76 data['compiledRelease']['tender']['criteria'] as "tender.criteria", --IS AN ARRAY
	# 77 data['compiledRelease']['tender']['coveredBy'] as "tender.coveredBy", --IS AN ARRAY
	# 78 data['compiledRelease']['tender']['participationFees'] as "tender.participationFees", --IS AN ARRAY
	# 79 data['compiledRelease']['awards'] as "awards", --IS AN ARRAY
	# 80 data['compiledRelease']['contracts'] as "contracts", --IS AN ARRAY
	# 81 data['compiledRelease']['relatedProcesses'] as "relatedProcesses", --IS AN ARRAY
	# 82 data['compiledRelease']['sources'] as "sources", --IS AN ARRAY
	# 83 data['compiledRelease']['complaints'] as "complaints", --IS AN ARRAY
	# 84 data['compiledRelease']['bids'] as "bids", --IS AN ARRAY
	# 85 data['compiledRelease']['auctions'] as "auctions", --IS AN ARRAY
	# 86 data['compiledRelease']['secondStage']['candidates'] as "secondStage.candidates",
	# 87 data['compiledRelease']['secondStage']['invitations'] as "secondStage.invitations",
	# 88 data['compiledRelease']['secondStage']['documents'] as "secondStage.documents",
	return None


def generate_csv (record_count: int) -> None:
	query = helpers.read_query_from_file(QUERY_FILE_PATH) + " ORDER BY r.ocid ASC LIMIT {0} OFFSET {1}"
	records_processed = 0
	offset = 0
	query = query.format(BATCH_SIZE, offset)
	cursor = con.cursor()
	while records_processed < record_count:
		cursor.execute(query)
		rows = cursor.fetchall()
		records_processed += len(rows)
		print(records_processed)
		offset += BATCH_SIZE
		query = query.format(BATCH_SIZE, offset)
	print(records_processed)

def main(arguments):
	cursor = con.cursor()
	cursor.execute('''SELECT count(*) FROM data;''')
	record_count_row = cursor.fetchone()
	record_count = record_count_row[0]
	print(f'\n{record_count} records found\n')
	generate_csv(record_count)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))