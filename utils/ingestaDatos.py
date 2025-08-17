import csv
from datetime import datetime

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
                        fecha_compra = datetime.strptime(linea['fecha'], "%Y-%m-%d")
                        if fecha_compra:
                            datos_validos.append(linea)
                    else:
                        print(f"Cliente: {linea['cliente']}, producto: {linea['producto']}, cantidad: {linea['cantidad']}, fecha: {linea['fecha']} -> Fecha no es valida. Se ignora la fila.")
                else:
                    info_compra = f"Cliente: {linea['cliente']}, producto: {linea['producto']}"
                    if int(linea['cantidad']) <= 0:
                        print(f"{info_compra}, cantidad: {linea['cantidad']} -> Valor de 'cantidad' no es valido. Se ignora la fila.")
                    elif float(linea['precio_unitario']) <= 0:
                        print(f"{info_compra}, precio: {linea['precio_unitario']} -> Valor de 'precio_unitario' no es valido. Se ignora la fila.")
        return datos_validos
    except FileNotFoundError:
        print(f"Error: El archivo {ruta_archivo} no fue encontrado.")
        return []
    except ValueError:
        print(f"Error: El archivo {ruta_archivo} contiene un formato de fecha invalido.")
        return []
    except Exception as e:
        print(f"Error al cargar el archivo: {ruta_archivo}, tipo de error: {type(e)}")
        return []