import json
import numpy as np
import random
import statistics
global matriz

def menu():
    print("¿Qué opción desea realizar?")
    print("1.- Asignar sueldos aleatorios")
    print("2.- Clasificar sueldos")
    print("3.- Ver estadísticas")
    print("4.- Reporte de sueldos")
    print("5.- Para salir del programa")
    op = int(input("Ingrese una opción válida (1/5): "))
    return op

def asignar_sueldos(matriz):
    aleatorio1 = random.randint(300000, 2500000)
    aleatorio2 = random.randint(300000, 2500000)
    aleatorio3 = random.randint(300000, 2500000)
    aleatorio4 = random.randint(300000, 2500000)
    aleatorio5 = random.randint(300000, 2500000)
    aleatorio6 = random.randint(300000, 2500000)
    aleatorio7 = random.randint(300000, 2500000)
    aleatorio8 = random.randint(300000, 2500000)
    aleatorio9 = random.randint(300000, 2500000)
    aleatorio10 = random.randint(300000, 2500000)

    
    matriz[0,1] = aleatorio1
    matriz[1,1] = aleatorio2
    matriz[2,1] = aleatorio3
    matriz[3,1] = aleatorio4
    matriz[4,1] = aleatorio5
    matriz[5,1] = aleatorio6
    matriz[6,1] = aleatorio7
    matriz[7,1] = aleatorio8
    matriz[8,1] = aleatorio9
    matriz[9,1] = aleatorio10

    return matriz

def listar_empleados(matriz):
    print()
    print("Listado de empleados:")
    print()

    lista1=[]
    lista2=[]
    lista3=[]

    for empleado in matriz:
        if empleado[1] <= 800000:
            lista1.append(empleado)
        elif 800000 < empleado[1] <= 2000000:
            lista2.append(empleado)
        elif empleado[1] > 2000000:
            lista3.append(empleado)

    print("Sueldos menores a $800.000:")
    print()
    print(lista1)

    print("Sueldos entre $800.000 y $2.000.000:")
    print()
    print(lista2)

    print("Sueldos superiores a $2.000.000:")
    print()
    print(lista3)

def ver_estadisticas(matriz):
    bajo = int(min(matriz[1]))
    alto = int(max(matriz[1]))
    dato = int(statistics.geometric_mean(matriz[1]))
    suma = int(matriz[0,1] + matriz[1,1] + matriz[2,1] + matriz[3,1] + matriz[4,1] + matriz[5,1] + matriz[6,1] + matriz[7,1] + matriz[8,1] + matriz[9,1])
    promedio = suma/10

    print(f"sueldo mas alto: {alto}")
    print(f"sueldo mas bajo: {bajo}")
    print(f"promedio de sueldos: {promedio}")
    print(f"Media geométrica: {dato}")

        




            
            

    