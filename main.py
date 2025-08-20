from utils.utils import cargar_compras, estadisticas, generar_reporte

"""
Módulo principal para la gestión de compras en ZORANY & ANDERSON S.A.S.
"""

def main():
    print("Bienvenido al sistema de compras ZORANY & ANDERSON S.A.S.")
    ruta_archivo = 'data/compras.csv'  # Ruta del archivo CSV de compras quemado
    compras = cargar_compras(ruta_archivo)
    print(f"Compras cargadas desde: {ruta_archivo}")
    print(f"Total de compras cargadas: {len(compras)}")
    resultado = estadisticas(compras)
    print(f"Resultados de las estadísticas: {resultado}")
    ruta_salida = './reportes/reporte.json'
    generar_reporte(resultado, ruta_salida)
    
    if isinstance(resultado, dict): 
        # Imprimir el resumen en consola de forma legible
        print("\nResumen de estadísticas:")
        print(f"- Total de ingresos: {resultado['total_ingresos']}")
        print(f"- Producto con mayor ingreso: {resultado['top_producto_por_ingresos']}")
        print(f"- Compras por cliente:")
        for cliente, cantidad in resultado['compras_por_cliente'].items():
            print(f"    - {cliente}: {cantidad}")
        bono_mensaje = resultado.get('mensaje', "No aplica bono.")
        print(f"- Bono: ({bono_mensaje})")


if __name__ == "__main__":
    main()
