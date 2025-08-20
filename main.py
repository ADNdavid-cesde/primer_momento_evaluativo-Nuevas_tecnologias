from utils.utils import cargar_compras

"""
Módulo principal para la gestión de compras en ZORANY & ANDERSON S.A.S.
"""

def main():
    print("Bienvenido al sistema de compras ZORANY & ANDERSON S.A.S.")
    #ruta_archivo = input("Ingrese la ruta del archivo CSV de compras: ")
    ruta_archivo = 'data/compras.csv'  # Ruta del archivo CSV de compras quemado
    compras = cargar_compras(ruta_archivo)
    print(f"Compras cargadas desde: {ruta_archivo}")
    print(f"Total de compras cargadas: {len(compras)}")
    
if __name__ == "__main__":
    main()