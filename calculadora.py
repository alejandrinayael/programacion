n1 = float(input("Introduce tu primer número: ") )
n2 = float(input("Introduce tu segundo número: ") )

opcion = 0
while True:
    print("""
    Dime, ¿qué quieres hacer?
    
    1) Sumar
    2) Restar
    3) Multiplicar
    4) Dividir 
    5) Potencia
    6) Nueva operación
    7) Apagar calculadora
    """)
    opcion = int(input("Elige una opción: ") )     

    if opcion == 1:
        print(" ")
        print("RESULTADO: La suma de",n1,"+",n2,"es igual a",n1+n2)
    elif opcion == 2:
        print(" ")
        print("RESULTADO: La resta de",n1,"-",n2,"es igual a",n1-n2)
    elif opcion == 3:
        print(" ")
        print("RESULTADO: El producto de",n1,"*",n2,"es igual a",n1*n2)
    elif opcion ==4:
        print(" ")
        print("RESULTADO: La divición de",n1,"÷",n2,"es igual a",n1/n2)
    elif opcion ==5:
        print(" ")
        print("RESULTADO: La potencia de",n1,"**",n2,"es igual a",n1**n2)
    elif opcion == 6:
        n1 = float(input("Introduce tu primer número: ") )
        n2 = float(input("Introduce tu segundo número: ") ) 
    elif opcion == 7:
        break
    else:
        print("Opción incorrecta")
