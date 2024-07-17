def total_carrito(request):
    total = 0
    if 'carrito' in request.session:
        for key, value in request.session['carrito'].items():
            total += value['precio'] * value['cantidad']
    return {'total_carrito': total}


def total_producto(request):
    total = 0
    if 'carrito' in request.session:
        for key, value in request.session['carrito'].items():
            total += value['cantidad']
    return {'total_producto': total}