from sys import stdin
import math


def suma(r,t):
    k = (r[0] + t[0], r[1] + t[1])
    return k

def resta(r,t):
    k = (r[0] - t[0], r[1] - t[1])
    return k

def multiplicacion(r,t):
    k = (r[0]*t[0] - r[1]*t[1],r[0]*t[1] + r[1]*t[0])
    return k

def division(r,t):
    k = ((r[0]*t[0] + r[1]*t[1])/(t[0]**2+t[1]**2),(r[1]*t[0] - r[0]*t[1])/(t[0]**2+t[1]**2))
    return k

def modulo(r):
    k = (r[0]**2 + r[1]**2)**(1/2)
    return k

def conjugado(r):
    k = (r[0], -1*r[1])
    return k

def conversion(r):
    l = (r[0]**2+r[1]**2)**(1/2)
    s = math.atan2(r[1],r[0])
    return (l,s)


def main():
    complejo1 = stdin.readline().strip().split(",")
    complejo2 = stdin.readline().strip().split(",")
    cm1 = (int(complejo1[0]),int(complejo1[1]))
    cm2 = (int(complejo2[0]),int(complejo2[1]))
    return (cm1,cm2)
    
def menu():
    while True:
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Módulo")
        print("6. Conjugado")
        print("7. Conversión")
        print("8. Fase")
        print("0. Salir")
        print("Elija una opción")
        op = stdin.readline().strip()
        if op == "1":
            p = main()
            print(suma(p[0],p[1]))
        elif op == "2":
            p = main()
            print(resta(p[0],p[1]))
        elif op == "3":
            p = main()
            print(multiplicacion(p[0],p[1]))
        elif op == "4":
            p = main()
            if p[1][0] == 0 and p[1][1] == 0:
                print("No se puede dividir por 0")
            else:
                print(division(p[0],p[1]))
        elif op == "5":
            p = stdin.readline().split(",")
            complejo = (int(p[0]),int(p[1]))
            print(modulo(complejo))
        elif op == "6":
            p = stdin.readline().split(",")
            complejo = (int(p[0]),int(p[1]))
            print(conjugado(complejo))
        elif op == "7":
            p = stdin.readline().split(",")
            complejo = (int(p[0]),int(p[1]))
            print(conversion(complejo))
        elif op == "8":
            p = main()
            print(fase(p[0],p[1]))
        elif op == "0":
            break
        else:
            print("Elija una de las opciones anteriormente mencionadas")
            
        
        
menu()
