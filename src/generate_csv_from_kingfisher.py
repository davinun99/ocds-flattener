import psycopg2
import settings
import helpers
import sys

def get_connection(): 
	con = None
	try:
		con = psycopg2.connect(
			host = settings.dbHost, 
			port = settings.dbPort,
			database = settings.dbDatabase, 
			user = settings.dbUser, 
			password = settings.dbPassword
		)
		return con
	except Exception as ex:
		print('\nException while connecting to db')
		print(ex)
		print('\n')
		exit()

def main(arguments):
	con = get_connection()
	cursor = con.cursor()
	cursor.execute('''SELECT count(*) FROM data;''')
	record_count_row = cursor.fetchone()
	record_count = record_count_row[0]
	print(f'\n{record_count} records found\n')
	query = helpers.read_query_from_file()
	print(query)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))