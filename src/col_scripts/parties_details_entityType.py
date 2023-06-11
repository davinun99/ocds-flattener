import sys
sys.path.append('./src')

# vector para mapear los posibles valores que puede tomar la futura columna
values_map = ['Municipalidades', 'NO CLASIFICADO', 'Organismos de la Administración Central', 'Entidades Descentralizadas']

roles = ['candidate','enquirer','payer', 'payee', 'supplier', 'procuringEntity', 'buyer', 'tenderer', 'notifiedSupplier']

def process_row (row: tuple, colNumber: int) -> str:
    # vector inicializado con ceros
    count_array = [0,0,0,0]
    return_string = ""

    if row[colNumber]:
        parties = row[colNumber]
        for rol in roles:
            for party in parties:
                if 'roles' in party:
                    rol_llamado = party['roles']
                    # será una columna para cada rol
                    if rol in rol_llamado:
                        if 'details' in party:
                            detail = party['details']
                            if 'entityType' in detail:
                                count_array[values_map.index(detail['entityType'])] += 1    
            # cada llamado diferente será una fila y cada rol diferente en el llamado es una columna de esa fila
            return_string +=  ";;;".join(map(str, count_array)) + ";;;"
            count_array = [0,0,0,0]
    else:
        for rol in roles:
            return_string += "0;;;0;;;0;;;0;;;"
            
    # quitamos los ;;; de más antes de retornar
    return return_string[:-3]
