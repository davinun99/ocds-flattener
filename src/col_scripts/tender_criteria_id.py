import sys
sys.path.append('./src')

def process_row (row: tuple, colNumber: int) -> bool:
    booleano = False
    if row[colNumber]:
        tender = row[colNumber]
        if tender is not None and 'criteria' in tender:
                booleano = True
    return booleano
