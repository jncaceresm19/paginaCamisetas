def total_carrito(request):
    total = 0
    if 'carrito' in request.session:
        for key, value in request.session['carrito'].items():
            if 'acumulado' in value:
                total += int(value['acumulado'])
    return {'total_carrito': total}