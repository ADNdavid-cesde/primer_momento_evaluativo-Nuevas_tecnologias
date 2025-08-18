from utils.utils import generar_reporte

def main():
    estadisticas2 = ''
    estadisticas = {
        'total_ingresos': 12225000,
        'top_producto_por_ingresos': 'laptop',
        'compras_por_cliente': {
            'A': 3,
            'B': 4,
            'C': 1,
            'D': 1
        },
        'bono': True
    }    
    ruta_salida = './reportes/reporte.json'
    generar_reporte(estadisticas, ruta_salida)
    
    if isinstance(estadisticas, dict): 
        # Imprimir el resumen en consola de forma legible
        print("\nResumen de estadísticas:")
        print(f"- Total de ingresos: {estadisticas['total_ingresos']}")
        print(f"- Producto con mayor ingreso: {estadisticas['top_producto_por_ingresos']}")
        print(f"- Compras por cliente:")
        for cliente, cantidad in estadisticas['compras_por_cliente'].items():
            print(f"    - {cliente}: {cantidad}")
        bono_mensaje = estadisticas.get('mensaje', "No aplica bono.")
        print(f"- Bono: ({bono_mensaje})")

if __name__ == "__main__":
    main()