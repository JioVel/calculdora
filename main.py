import os
import variables as va
from funciones import inicio_calculadora, operacion_calculadora, reiniciar_calculadora, mostrar_acumulado

os.chdir(os.path.dirname(os.path.abspath(__file__)))

numero = None
reiniciar = False
while True:

    if numero == None:
        try:
            numero = float(input(va.mensaje1))
            inicio_calculadora(numero)
            print("\n")
        except:
            numero = None
            print("ERROR!!!!")


    try:
        print("Acumulado: ")
        mostrar_acumulado()
        print("\n")
        operacion = int(float(input(va.mensaje2)))
        # print(operacion)
        if operacion == 6:
            break
        elif operacion == 5:
            reiniciar = True
            if reiniciar == True:
                numero = None
                reiniciar_calculadora()
                reiniciar = False
                continue



        print("\n")
        numero2 = float(input(va.mensaje3))
        if operacion == 4:
            if numero2 == 0:
                print("Error!!!")
                continue

        operacion_calculadora(operacion, numero2)

    except:
        print("ERROR!!!!")
        continue