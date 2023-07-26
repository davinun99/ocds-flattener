import sys
sys.path.append('./src')

# vector para mapear los posibles valores que puede tomar la futura columna
values_map = ['Persona Física - Bienes y Servicios', 'Persona Física - Servicios Personales', 'S.A.', 'S.R.L.', 'S.A.C.I.', 'S.A.E.C.A.', 'Consorcio', 'Otros', 'S.A.I.C.', 'S.A.C.', 'Sociedad Simple', 'S.A.E.', 'C.I.S.A.', 'Sociedad Civil', 'E.I.R.L.', 'Cooperativas', 'Extranjeras', 'Sucursal', 'C.E.I.S.A.', 'Coaseguro', 'Empresa de Acciones Simplificada', 'Empresa sin fines de lucro', 'Asociación']

roles = ['candidate','enquirer','payer', 'payee', 'supplier', 'procuringEntity', 'buyer', 'tenderer', 'notifiedSupplier']

def process_row (row: tuple, colNumber: int) -> str:
    # vector inicializado con ceros
    count_array = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
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
                            if 'legalEntityTypeDetail' in detail:
                                count_array[values_map.index(detail['legalEntityTypeDetail'])] += 1    
            # cada llamado diferente será una fila y cada rol diferente en el llamado es una columna de esa fila
            return_string += ";;;".join(map(str, count_array)) + ";;;"
            count_array = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    else:
        for rol in roles:
            return_string += "{};;;".format(";;;0"*len(count_array))
            
    # quitamos los ;;; de más antes de retornar
    return return_string[:-3]