import json
import os

def generar_reporte(resumen, ruta_salida):
    """Genera un reporte en formato JSON a partir de un resumen.
    
    Args:
        resumen (dict): Resumen de los datos.
        ruta_salida (str): Ruta donde se guardará el reporte.
    """
    # Guardar el reporte en formato JSON
    try:
        if not isinstance(resumen, dict):
            raise ValueError("El resumen debe ser un diccionario.")
        else:
            print("Generando reporte...")
            # Verificar si la carpeta de salida existe, si no, crearla
            directorio = os.path.dirname(ruta_salida)
            if not os.path.exists(directorio):
                os.makedirs(directorio)
            with open(ruta_salida, 'w') as archivo_salida:
                # Si bono es True, agregar mensaje adicional
                if resumen.get('bono', False):
                    resumen['mensaje'] = f"Umbral superado, aplicar descuento corporativo 5% en proxima compra"
                json.dump(resumen, archivo_salida, indent=4)
            print(f"Reporte generado exitosamente en: {ruta_salida}")
    except Exception as e:
        print(f"Error al generar el reporte: {e} {type(e)}")