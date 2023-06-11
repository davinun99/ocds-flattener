#Parametros de conexion a kingfisher PostgreSQL
import psycopg2

dbHost="localhost"
dbPort=5432
dbDatabase="kf2016"
dbUser="postgres"
dbPassword="postgres"
con = None

try:
	con = psycopg2.connect(
		host = dbHost, 
		port = dbPort,
		database = dbDatabase, 
		user = dbUser, 
		password = dbPassword
	)
except Exception as ex:
	print('\nException while connecting to db')
	print(ex)
	print('\n')
	exit()
