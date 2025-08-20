from utils.utils import estadisticas

def main():
    data = [
        {
            'cliente': 'Juan',
            'producto': 'Laptop',
            'cantidad': 2,
            'precio_unitario': 3500000
        },
        {
            'cliente': 'Ana',
            'producto': 'Mouse',
            'cantidad': 5,
            'precio_unitario': 50000
        },
        {
            'cliente': 'Luis',
            'producto': 'Teclado',
            'cantidad': 3,
            'precio_unitario': 120000
        }
    ]
    resultado = estadisticas(data)
    print(resultado)

if __name__ == "__main__":
    main()
