"""Se recibirá la opción a ejecutar del usuario usando la función input,
la opción puede ser suma, resta, multiplicación, división o modal.
se validará el valor de entrada."""

def operacion (n1:int,n2:int, op:int) -> int:
    """n1 = número entero"""
    """n2 = número entero"""
    """op = número de operación"""

    match int(op):
        case 1:
            print(n1+n2)
        case 2:
            print (n1-n2)
        case 3:
            print (n1*n2)
        case 4:
            print (n1/n2)
        case 5:
            print (n1%n2)

print('Bienvenido a la calculadora de Moisés en Python.\n')
opcion = input('1: Adición. \n'
                +'2: Sustracción. \n'
                +'3: Multiplicación. \n'
                +'4: División. \n'
                +'5: Módulo.\n'
                +'Elige una opción:     ')

match int(opcion):
    case 1:
        print ('Eligió la opción {}.'.format('Adición'))
        n1 = int( input("Ingrese un número: "))
        n2 = int(input("Ingrese otro número:"))
        operacion (n1,n2,opcion)
    case 2:
        print ('Eligió la opción {}.'.format('Sustracción'))
        n1 = int(input("Ingrese un número: "))
        n2 = int(input("Ingrese otro número:" ))
        operacion (n1,n2,opcion)
    case 3:
        print ('Eligió la opción {}.'.format('Multiplicación'))
        n1 = int(input("Ingrese un número: "))
        n2 = int(input("Ingrese otro número:"))
        operacion (n1,n2,opcion)
    case 4:
        print ('Eligió la opción {}.'.format('División'))
        n1 = int(input("Ingrese un número: "))
        n2 = int(input("Ingrese otro número:"))
        operacion (n1,n2,opcion)
    case 5:
        print ('Eligió la opción {}.'.format('Módulo'))
        n1 = int(input("Ingrese un número: "))
        n2 = int(input("Ingrese otro número:" ))
        operacion (n1,n2,opcion)
    case _ :
        print('Eligió un valor no válido.')


