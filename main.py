venta_productos = [
[2, 122],
[1, 89],
[1, 22],
[3, 48],
[1, 75],
[3, 322],
[2, 95],
[1, 148],
[1, 83],
[3, 100]
]
productos = [['Maiz Grano', 285.55],['Pepino', 334.72],['Tomate Verde', 129.00]]

y=0
ventaDiaria=0

for x in venta_productos:
  cantidadCajas = venta_productos[y][1]
  ventaDiaria += cantidadCajas
  
for x in venta_productos:
  idProducto= venta_productos[y][0]
  cantidadCajas = venta_productos[y][1]
  y=y+1
  
  if idProducto == 1:
    idproducto = 1
  elif idProducto == 2:
    idProducto = 2
  elif idProducto == 3:
    idProducto = 3 
    
  producto = productos[idProducto-1][0]
  costoCaja = productos[idProducto-1][1]
  costoTotal = float(costoCaja) * cantidadCajas
    
  if cantidadCajas <= 100:
    costoTotal = costoTotal + 1500
    envio = '1500 pesos'
  else:
    costoTotal = costoTotal
    envio = 'Gratis'  
    
  if ventaDiaria <=1500:
    descuento20 = True
    costoConDescuento = costoTotal*0.20
    costoTotal = costoTotal - costoConDescuento
  else:
    descuento20 = False  
    costoConDescuento = 0
    
  print('El producto es:', producto)
  print('El precio por caja es:', costoCaja, 'pesos')
  print('Aplica descuento del 20%:',descuento20)
 # print('Descuento:', str(-costoConDescuento),'pesos')
  print('Costo de Envio:', envio)
  print('El total a pagar es:',       '{:.2f}'.format(costoTotal),'pesos')
  print('')
  
  

  
