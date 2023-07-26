import sys
sys.path.append('./src')
import pandas as pd

class TenderDocumentsDocumentTypeDetail: 

    def inicializar_70_percent(self, rows: list[tuple]):
        ## PRIMERA PARTE: Obtener todos los valores distintos con su cantidad de apariciones y la cantidad total de elementos
        diccionario = {} # diccionario donde guardaremos la cantidad de apariciones

        cant_elementos = 0

        for row in rows:
            if row[self.colNumber]:
                lista = row[self.colNumber]
                if lista is not None and 'documents' in lista:
                    elemento = lista['documents']
                    for val in elemento:
                        if 'documentTypeDetails' in val:
                            # sumamos 1 a la cantidad de elementos:
                            cant_elementos += 1
                            valor = val['documentTypeDetails']
                            # si está en el diccionario agregamos 1 al contador
                            if valor in diccionario.keys():
                                diccionario[valor] += 1
                            # si no está entonces creamos una nueva entrada de valor 1
                            else:
                                diccionario[valor] = 1
            
        # convertimos el diccionario a dataframe para poder ordenarlo
        df = pd.DataFrame( [[diccionario[key],key] for key in diccionario.keys()], columns=['contador','valor'] )
        ordenado_por_contador = df.sort_values('contador', ascending=False)
        
        ## SEGUNDA PARTE: Calcular los valores dentro del 70%
        setenta_por_ciento = 0.70 * cant_elementos
        
        # guardaremos los valores en un array para ir insertandolos a cada elemento como una columna
        values_map = []
        # array que tendrá cantidad de 0 igual a cantidad de elementos
        count_array =  []
        suma_actual = 0
        for index, fila in ordenado_por_contador.iterrows():
            suma_actual += fila['contador']
            if suma_actual <= setenta_por_ciento:
                values_map.append(fila['valor'])
                count_array.append(0)
            else:
                values_map.append("otros")
                count_array.append(0)
                break

        return count_array,values_map
    
    def process_row(self, row: tuple, colNumber: int):
        ## TERCERA PARTE: generar las nuevas columnas (por el momento solamente imprimir)
        # array lleno de ceros para resetear la lista cuando necesitemos
        count_array_bk = self.count_array.copy()
        count_array = self.count_array.copy()

        if row[colNumber]:
            tender = row[colNumber]         
            if tender is not None and 'documents' in tender:
                elemento = tender['documents']
                for val in elemento:
                    if 'documentTypeDetails' in val:
                        valor = val['documentTypeDetails']
                        if valor in self.values_map:
                            count_array[self.values_map.index(valor)] += 1
                        else:
                            count_array[-1] += 1
            return ";;;".join(map(str, count_array))
        else:
            return ";;;".join(map(str, count_array_bk))

    def __init__(self, rows: list[tuple], colNumber: int):
        pd.set_option('display.max_columns', None)
        self.colNumber = colNumber
        self.count_array, self.values_map = self.inicializar_70_percent(rows)
