import sys
sys.path.append('./src')

def process_row (row: tuple, colNumber: int) -> str:
    respondidos = 0
    total = 0
    porcentaje = 0
    if row[colNumber]:  
        tender = row[colNumber]
        if tender is not None and 'enquiries' in tender:
            elemento = tender['enquiries']
            for val in elemento:
                if 'answer' in val:
                    respondidos += 1
                total += 1 
    if total != 0:
        return "{};;;{};;;{}".format(str(total),str(respondidos),str(int((respondidos/total) * 100)))
    else:
        return "{};;;{};;;0".format(str(total),str(respondidos))
 