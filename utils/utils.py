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

def estadisticas(data):
    total_ingresos = 0
    ingresos_por_producto = {}
    top_producto_por_ingresos = None
    compras_por_cliente = {}

    for item in data:
        cliente = item['cliente']
        producto = item['producto']
        cantidad = item['cantidad']
        precio_unitario = item['precio_unitario']

        # Calcular total ingresos
        total_ingresos += cantidad * precio_unitario

        # Calcular ingresos por producto
        if producto not in ingresos_por_producto:
            ingresos_por_producto[producto] = 0
        ingresos_por_producto[producto] += cantidad * precio_unitario

        # Calcular compras por cliente
        if cliente not in compras_por_cliente:
            compras_por_cliente[cliente] = 0
        compras_por_cliente[cliente] += cantidad

    # Calcular top producto por ingresos
    if ingresos_por_producto:
        producto_top = max(ingresos_por_producto, key=ingresos_por_producto.get)
        top_producto_por_ingresos = {
            'producto': producto_top,
            'ingreso_total': ingresos_por_producto[producto_top]
        }

    # Agregar condición de negocio
    if total_ingresos > 6_000_000:
        bono = True
    else:
        bono = False

    # Retornar resultados
    return {
        'total_ingresos': total_ingresos,
        'top_producto_por_ingresos': top_producto_por_ingresos,
        'compras_por_cliente': compras_por_cliente,
        'bono': bono
    }