import sys
sys.path.append('./src')
import helpers
BATCH_SIZE = 1000

map_data = {
	"769": 0,
	"109": 1,
	"773": 2,
	"151": 3,
	"116": 4,
	"720": 5,
	"179": 6,
	"766": 7,
	"68": 8,
	"66": 9,
	"709": 10,
	"142": 11,
	"252": 12,
	"389": 13,
	"20": 14,
	"388": 15,
	"757": 16,
	"251": 17,
	"112": 18,
	"746": 19,
	"729": 20,
	"155": 21,
	"148": 22,
	"764": 23,
	"768": 24,
	"329": 25,
	"96": 26,
	"591": 27,
	"644": 28,
	"69": 29,
	"84": 30,
	"597": 31,
	"64": 32,
	"780": 33,
	"756": 34,
	"731": 35,
	"749": 36,
	"5": 37,
	"732": 38,
	"806": 39,
	"445": 40,
	"8": 41,
	"562": 42,
	"45": 43,
	"394": 44,
	"747": 45,
	"750": 46,
	"147": 47,
	"143": 48,
	"278": 49,
	"384": 50,
	"195": 51,
	"719": 52,
	"52": 53,
	"218": 54,
	"560": 55,
	"386": 56,
	"387": 57,
	"748": 58,
	"28": 59,
	"83": 60,
	"782": 61,
	"120": 62,
	"67": 63,
	"308": 64,
	"15": 65,
	"103": 66,
	"50": 67,
	"153": 68,
	"219": 69,
	"715": 70,
	"89": 71,
	"827": 72,
	"447": 73,
	"451": 74,
	"55": 75,
	"325": 76,
	"722": 77,
	"58": 78,
	"90": 79,
	"257": 80,
	"217": 81,
	"149": 82,
	"159": 83,
	"160": 84,
	"250": 85,
	"13": 86,
	"723": 87,
	"383": 88,
	"85": 89,
	"97": 90,
	"124": 91,
	"379": 92,
	"817": 93,
	"758": 94,
	"98": 95,
	"162": 96,
	"259": 97,
	"272": 98,
	"273": 99,
	"326": 100,
	"455": 101,
	"49": 102,
	"53": 103,
	"563": 104,
	"60": 105,
	"71": 106,
	"714": 107,
	"724": 108,
	"730": 109,
	"735": 110,
	"751": 111,
	"755": 112,
	"770": 113,
	"324": 114,
	"594": 115,
	"310": 116,
	"621": 117,
	"446": 118,
	"18": 119,
	"726": 120,
	"734": 121,
	"818": 122,
	"595": 123,
	"574": 124,
	"760": 125,
	"763": 126,
	"570": 127,
	"568": 128,
	"567": 129,
	"559": 130,
	"1002": 131,
	"454": 132,
	"448": 133,
	"793": 134,
	"39": 135,
	"80": 136,
	"382": 137,
	"38": 138,
	"32": 139,
	"309": 140,
	"275": 141,
	"727": 142,
	"742": 143,
	"260": 144,
	"725": 145,
	"718": 146,
	"716": 147,
	"646": 148,
	"75": 149,
	"753": 150,
	"754": 151,
	"154": 152,
	"36": 153,
	"561": 154,
	"24": 155,
	"566": 156,
	"56": 157,
	"233": 158,
	"23": 159,
	"127": 160,
	"70": 161,
	"444": 162,
	"576": 163,
	"10": 164,
	"581": 165,
	"123": 166,
	"596": 167,
	"47": 168,
	"728": 169,
	"76": 170,
	"767": 171,
	"311": 172,
	"100": 173,
	"557": 174,
}

def process_row (row: tuple, colNumber: int):
	countArr = [0] * len(list(map_data))
	if row[colNumber]:
		for contract in row[colNumber]:
			if('investmentProjects' in contract):
				for investmentProject in contract['investmentProjects']:
					ind = map_data[investmentProject['id']]
					countArr[ind] += 1
	return ";;;".join(map(str, countArr))

def main(arguments):
	query = """
		SELECT
			data['compiledRelease']['ocid'] as "id",
			data['compiledRelease']['contracts'] as "contracts"
		FROM RECORD r join data d on d.id = r.data_id
	"""
	# for row in helpers.get_rows(query):
	# 	idArr = process_row(row, 1)
	# 	print(idArr)

# if __name__ == '__main__':
#     sys.exit(main(sys.argv[1:]))