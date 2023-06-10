"""Se recibe un número a través de un input y se valida para saber si corresponde a un año biciesto"""



##anio = int(input("Escribe un año: "))
anio = int(1992)
if anio%4 == 0 and anio%100== 0 and anio%400==0:
    print ('Es biciesto.')
else:
    print('No es biciesto.')

    #pendiente agregar el año 1992 como año biciesto