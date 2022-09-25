import math


def menu():
    print("Menu")
    print("1.-Triangulo")
    print("2.-Cuadrado")
    print("3.-Circulo")
    opcion=input("seleccione la opcion deseada: ")
    while (True):
        if opcion=="1":
            triangulo()
            break
            
        elif opcion=="2":
            cuadrado()
            break
        elif opcion=="3":
            circulo()
            break
        else:
            print("elija opcion correcta")
            menu()
            break


def triangulo():
    base=int(input("ingrese la base: "))
    altura=int(input("ingrese altura: "))
    area=base*altura/2
    print("El area es: ",area)

def cuadrado():
    lado=int(input("ingrese la base: "))
    area=lado*lado
    print("El area es: ",area)


def circulo():
    pi=3.1416
    radio=int(input("ingrese radio: "))
    area=pi*radio**2
    print("El area es: ",area)


menu()
