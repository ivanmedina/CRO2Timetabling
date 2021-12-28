from lib.funciones import *
from lib.input import *
from lib.output import *
from lib.timetabling import timetabling

def main():
    
    input=leerInput('./input/new_input.json')
    salida=timetabling(input)

    # print('cursos sin asignar: ',cursosDisponible(salida['Y']))
    # print('Salones sin usar: ',salida['Q'])

    # generarInputPrueba(5,10,10,20,8,10,4,3,'pruebas1')
    # dibujarTabla(salida['X'],input,'horario_nuevo')
    
    xlineal=aplanarX(salida['X'])
    print(xlineal)

    xarmada=rearmarX(xlineal,input)

    print(len(xarmada) * len(xarmada[0]) *len(xarmada[0][0]) * len(xarmada[0][0][0]) )

if __name__ == "__main__":
    main()