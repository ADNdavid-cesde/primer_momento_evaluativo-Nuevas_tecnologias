
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