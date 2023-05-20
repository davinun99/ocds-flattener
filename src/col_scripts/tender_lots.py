import sys
sys.path.append('./src')

def process_row (row: tuple, colNumber: int) -> int:
    total = 0 
    if row[colNumber]:  
        tender = row[colNumber]
        if tender is not None and 'lots' in tender:
            total = len(tender['lots'])
    return total
