from lib.funciones import *
from lib.input import *
from lib.output import *
from lib.timetabling import timetabling
from lib.restricciones import R1,R2,R3,R4,R5,R6,R7,R8,R9,R10,R11

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

    if(xarmada==salida['X']):
        print('xarmada == salida[\'X\']')

    
    print('Restriccion 1 para c=0 :', R1(input,salida['X'],0))
    print('Restriccion 2 para d=e=p=0 :', R2(salida['X'],0,0,0))
    print('Restriccion 3 para d=e=s=0 :', R3(salida['X'],0,0,0))
    print('Restriccion 4 para c=p=0 :', R4(input,salida['Y'],0,0))
    print('Restriccion 5 para p=0 :', R5(input,salida['Y'],0))
    print('Restriccion 6 para d=e=p=0 :', R6(input,salida['X'],0,0,0))
    print('Restriccion 7 para d=e=p=0 :', R7(input,salida['X'],0,0,0))
    print('Restriccion 8 para c=0 :', R8(salida['V'],0))
    print('Restriccion 9 para c=0 :', R9(salida['X'],salida['U'],salida['W'],0))
    print('Restriccion 10 para d=c=0 :', R10(salida['W'],0,0))
    # print('Restriccion 11 :', R11(xlineal))

    print(salida['Q'])
    Z1=Z(salida['X'],salida['G'])
    print('Z > ',Z1)

    print('Restriccion 11 :', R11(151,Z1))


if __name__ == "__main__":
    main()