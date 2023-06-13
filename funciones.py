from clases import Calculadora
import variables as va

def inicio_calculadora(numero):
    global calculadora
    calculadora = Calculadora(numero)

def mostrar_acumulado():
    print(calculadora.acumulado)

def reiniciar_calculadora():
    calculadora.reiniciar()

def operacion_calculadora(operacion, numero):
    if operacion == 1:
        print(calculadora.suma(numero))

    elif operacion == 2:
        print(calculadora.resta(numero))

    elif operacion == 3:
        print(calculadora.multiplicacion(numero))

    elif operacion == 4:
        print(calculadora.division(numero))