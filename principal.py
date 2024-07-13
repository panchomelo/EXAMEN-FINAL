from funciones import menu, asignar_sueldos, listar_empleados, ver_estadisticas
import json, os
import numpy as np

matriz = np.empty((10, 2), dtype=object)

if os.path.exists('empleados.json'):
    with open('empleados.json', 'r') as file:
        json_empleados = json.load(file)
    
    for i, empleado in enumerate(json_empleados):
        matriz[i, 0] = empleado['nombre_completo']
        matriz[i, 1] = empleado['sueldo']

while True:
    op = menu()

    match op:
        case 1:
            matriz=asignar_sueldos(matriz)
        case 2:
            listar_empleados(matriz)
        case 3:
            ver_estadisticas(matriz)
        case 4:
            print("reporte de sueldos")
        case 5:
            print("Has elegido salir, adiós")
            break
        case _:
            print("Opción no válida")