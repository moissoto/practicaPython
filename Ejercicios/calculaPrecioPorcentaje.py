#Solicita al usuario ingresar el precio y el porcentaje.
#Imprime precio, descuento y precio final.

print("Abarrotes \"Si hay y bien\"")
precio= int (input ("Ingrese el valor del producto: "))
porcentaje = int (input("Ingrese el porcentaje de descuento: "))
precioFinal = precio-((precio*porcentaje)/100)
print("Precio del producto: {0}".format(precio))
print("Descuento: {0}".format(precio-precioFinal))
print ("Total a pagar: {0} ".format(precioFinal))