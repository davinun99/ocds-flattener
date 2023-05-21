import sys
sys.path.append('./src')
import pandas as pd

class PartiesRoles:

    # lista de roles
    roles = ['candidate', 'enquirer', 'payer', 'payee', 'supplier', 'procuringEntity', 'buyer', 'tenderer', 'notifiedSupplier']

    def inicializar_quartiles(self, rows: list[tuple]):
        roles_quartiles = {
            'candidate': {'firstq_map': [],'secondq_map': [],  'thirdq_map': []},
            'enquirer':  {'firstq_map': [],'secondq_map': [],  'thirdq_map': []},
            'payer':  {'firstq_map': [],'secondq_map': [],  'thirdq_map': []},
            'payee':  {'firstq_map': [],'secondq_map': [],  'thirdq_map': []},
            'supplier':  {'firstq_map': [],'secondq_map': [],  'thirdq_map': []},
            'procuringEntity':  {'firstq_map': [],'secondq_map': [],  'thirdq_map': []},
            'buyer':  {'firstq_map': [],'secondq_map': [],  'thirdq_map': []},
            'tenderer':  {'firstq_map': [],'secondq_map': [],  'thirdq_map': []},
            'notifiedSupplier':  {'firstq_map': [],'secondq_map': [],  'thirdq_map': []}
        }
        for rol in self.roles:
            ## PRIMERA PARTE: Obtener todos los valores distintos con su cantidad de apariciones y la cantidad total de elementos
            diccionario = {} # diccionario donde guardaremos la cantidad de apariciones

            cant_elementos = 0

            for row in rows:
                if row[self.colNumber]:
                    lista = row[self.colNumber]
                    for elem in lista:
                        if 'name' in elem:
                            valor = elem['name'] # CAMBIAR POR ID LUEGO
                            if 'roles' in elem and rol in elem['roles']:
                                cant_elementos += 1
                                # si está en el diccionario agregamos 1 al contador
                                if valor in diccionario.keys():
                                    diccionario[valor] += 1
                                # si no está entonces creamos una nueva entrada de valor 1
                                else:
                                    diccionario[valor] = 1
            
            # convertimos el diccionario a dataframe para poder ordenarlo
            df = pd.DataFrame( [[diccionario[key],key] for key in diccionario.keys()], columns=['contador','valor'] )
            ordenado_por_contador = df.sort_values('contador', ascending=False)

            ## SEGUNDA PARTE: Calcular los valores de cada cuartil
            primer_cuartil = 0.25 * cant_elementos
            segundo_cuartil = 0.5 * cant_elementos
            tercer_cuartil = 0.75 * cant_elementos
            
            # guardaremos los valores que pertenecen a cada cuartil en un array diferente
            firstq_map = []
            secondq_map = []
            thirdq_map = []
            # fourthq_map = [] # el cuarto cuartil no es necesario porque estarán todos los elementos que no están en los otros tres
            # ahora asignamos a cada elemento a su cuartil
            suma_actual = 0
            for index, fila in ordenado_por_contador.iterrows():
                suma_actual += fila['contador']
                if suma_actual <= primer_cuartil:
                    firstq_map.append(fila['valor'])
                elif suma_actual <= segundo_cuartil:
                    secondq_map.append(fila['valor'])
                elif suma_actual <= tercer_cuartil:
                    thirdq_map.append(fila['valor'])
                else:
                    break
            # guardamos los valores para cada rol
            roles_quartiles[rol]['firstq_map'] = firstq_map
            roles_quartiles[rol]['secondq_map'] = secondq_map
            roles_quartiles[rol]['thirdq_map'] =  thirdq_map

        return roles_quartiles
        
    def process_row(self, row: tuple, colNumber: int):
        ## TERCERA PARTE: generar las nuevas columnas (por el momento solamente imprimir)
        return_string = ""
        
        for rol in self.roles:
            quartiles = [0,0,0,0].copy()
            if row[colNumber]:
                parties = row[colNumber]
                for party in parties:
                    if 'name' in party:
                        valor = party['name'] # CAMBIAR POR ID LUEGO
                        if 'roles' in party and rol in party['roles']:
                            # 1er cuartil
                            if valor in self.roles_cuartiles[rol]['firstq_map']:
                                quartiles[0] += 1
                            # 2do cuartil
                            elif valor in self.roles_cuartiles[rol]['secondq_map']:
                                quartiles[1] += 1
                            # 3er cuartil
                            elif valor in self.roles_cuartiles[rol]['thirdq_map']:
                                quartiles[2] += 1
                            # 4to cuartil
                            else:
                                quartiles[3] += 1
            # cada llamado diferente será una fila y cada rol diferente en el llamado es una columna de esa fila
            if quartiles != [0,0,0,0]:
                return_string += "{};;;".format(quartiles)
                quartiles = [0,0,0,0].copy()
            else:
                return_string += "{};;;".format([0,0,0,0])
             
        # quitamos los ;;; de más antes de retornar
        return return_string[:-3]   

    def __init__(self, rows: list[tuple], colNumber: int):
        pd.set_option('display.max_columns', None)
        self.colNumber = colNumber
        self.roles_cuartiles = self.inicializar_quartiles(rows)
