#Calculadora de rectángulo
#solicita al usuario las medidas en cm de los lados del rectángulo

print("Calculadora de perímetros de rectángulos")

ladoA = float(input ("Ingresa el valor de la base del rectángulo: "))
ladoB = float(input ("Ingresa el valor de la altura del rectángulo: "))

perimetro = ladoA*ladoB

print ("La base mide {0} cm, la altura mide {1}, lo que nos da un perímetro total de {2} cm^2.".format(ladoA,ladoB,perimetro))