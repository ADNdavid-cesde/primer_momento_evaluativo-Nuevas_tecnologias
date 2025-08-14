
def estadisticas(data):
    total_ingresos = 0
    top_producto_por_ingresos = None
    compras_por_cliente = {}

    for item in data:
        cliente = item['cliente']
        producto = item['producto']
        cantidad = item['cantidad']
        precio_unitario = item['precio_unitario']

        # Calcular total ingresos
        total_ingresos += cantidad * precio_unitario

        # Calcular top producto por ingresos
        if top_producto_por_ingresos is None or producto['ingreso_total'] > top_producto_por_ingresos['ingreso_total']:
            top_producto_por_ingresos = {
                'producto': producto,
                'ingreso_total': cantidad * precio_unitario
            }

        # Calcular compras por cliente
        if cliente not in compras_por_cliente:
            compras_por_cliente[cliente] = 0
        compras_por_cliente[cliente] += cantidad

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