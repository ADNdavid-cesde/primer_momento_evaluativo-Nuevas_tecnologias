import csv

def cargar_compras(ruta_archivo) -> list:
    """
    Carga los datos de compras desde un archivo CSV y los devuelve como una lista de diccionarios.
    Cada diccionario representa una compra con sus detalles.
    """
    try:
        datos_validos = []
        with open(ruta_archivo, 'r') as archivo:
            csv_reader = csv.DictReader(archivo)
            for linea in csv_reader:
                #cantidad y precio_unitario > 0 (si no, ignorar fila y registrar advertencia). 
                if int(linea['cantidad']) > 0 and float(linea['precio_unitario']) > 0:
                    #fecha con formato YYYY-MM-DD (si no, ignorar fila)
                    if len(linea['fecha']) == 10 and linea['fecha'][4] == '-' and linea['fecha'][7] == '-':
                        datos_validos.append(linea)
                    else:
                        print(f"producto: {linea['producto']}, cantidad: {linea['cantidad']}, precio_unitario: {linea['precio_unitario']} -> Fecha no es valida. Se ignora la fila.")
                else:
                    print(f"producto: {linea['producto']}, cantidad: {linea['cantidad']}, precio_unitario: {linea['precio_unitario']} -> Valores no son validos. Se ignora la fila.")
        return datos_validos
    except FileNotFoundError:
        print(f"Error: El archivo {ruta_archivo} no fue encontrado.")
        return []