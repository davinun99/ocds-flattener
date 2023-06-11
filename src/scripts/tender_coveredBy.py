import sys
sys.path.append('./src')


BATCH_SIZE = 1000

map_data = {
	"fonacide": 0,
	"produccion_nacional": 1,
	"urgencia_impostergable": 2,
	"adreferendum": 3,
	"agricultura_familiar": 4,
	"covid_19": 5,
	"almuerzo_escolar": 6,
	"seguridad_nacional": 7,
}

def process_row (row: tuple, colNumber: int):
	countArr: list[int] = [0] * len(list(map_data))
	if row[colNumber]:
		for cover in row[colNumber]:
			ind = map_data[cover]
			countArr[ind] += 1
	return countArr
