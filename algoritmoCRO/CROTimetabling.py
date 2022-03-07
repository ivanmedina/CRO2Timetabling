from decimal import Decimal, getcontext
import os
from re import X
from time import time
from time import sleep
import sys
import json
PROJECT_PATH = os.getcwd()
SOURCE_PATH = os.path.join(
    PROJECT_PATH,"../"
)
sys.path.append(SOURCE_PATH)

from timetabling.lib.funciones import *
from timetabling.lib.inputT import *
from timetabling.lib.output import *
from timetabling.lib.timetabling import *
from timetabling.lib.operaciones import *
from algoritmoCRO.lib.molecula import Molecula
from algoritmoCRO.lib.cro import CRO
getcontext().prec = 16

initialKE = 0.5 # no se usa
buffer = 0
KELossRate = 0.05
# KELossRate = -0.000005
colision =0.9
alfa = 20
beta =  0.00000025
popSize = 20
porcentaje = 5
criterios = { 'a' : 50000, 'b' : 0, 'c' : 500 }

def finicio(    pinicio  ):
    print('#'*20+' Etapa 1 ' +'#'*20+'\n')
    print('[*] Generando poblacion ...')
    print('[i] '+'pobSize'.ljust(12,' ')+str(pinicio['size']).rjust(24,' '))
    poblacion=[]
    coors=encontrarUnosX( semilla )
    for i in range(pinicio['size']):
        xnueva=nuevaX(semilla, random.choice(coors[0]), random.choice(coors[1]))
        Zmin = Z(xnueva)
        pobjetivo = { "input" : pinicio['input'], "variables" : [], "K" : 1000, "Zanterior" : Zmin, "Znueva" : Zmin, "wd" : xnueva }
        PE, Znueva, F,check = fun_objetivo(pobjetivo)
        molecula=Molecula(i,xnueva, 0 , PE, 0, xnueva, PE, 0, Znueva, check )
        poblacion.append(molecula)
        # print(molecula.toString())
    print('[+] Poblacion generada\n')
    print('[*] Calculando Energia de la Poblacion ...')
    EPT = PETotal(poblacion)
    IK= calcularInitialKE(EPT, pinicio['porcentajeKE'])
    poblacion = setKE(poblacion, IK)
    TE= CalcularTE(poblacion) 
    print()
    EnergiasStr(pinicio['porcentajeKE'], IK, TE)
    print('[+] Energia Calculada\n')
    return [   poblacion, Decimal(TE), Decimal(initialKE)    ]

def fun_objetivo(pobjetivo):
    pobjetivo['variables'] = MatricesX( pobjetivo['wd'] )
    Znueva = Z(pobjetivo['variables']['X'])
    pobjetivo['Znueva'] = Znueva
    F,check=fobjetivo( pobjetivo )
    return [ Decimal(fitness(F)), Decimal(Znueva), Decimal(F),check ]

# Generar soluciones
# instancias = generarInstancias("./../timetabling/input/instancias.txt")
# for i in range(3,10):
#     input = leerInput(instancias[i])
#     start=time()
#     salida=timetabling(input)
#     secs= time()-start
#     # guardar solucion
#     horario=json.dumps(salida)
#     file=open("../timetabling/output/JSON/salida-"+str(i+1)+".json",'w')
#     filename=file.name
#     file.write(horario)
#     file.close()
#     print('[+] Timetabling '+str(i+1)+'(%0.10f s.)' % secs)
#     shedule=timetable(salida['X'],'horario-'+str(i+1))
#     dibujarHorario(shedule,input,'horario-oficial-'+str(i+1))

# Ejemplo instancia 10
# Cargar Semilla
# for i in range(4,11):
print('\n'+'#'*20+' Cargando ' +'#'*20+'\n')
print('[*] Cargando semilla ...')
instancia=10
print('instancia>',instancia)
input =  leerInput('./../timetabling/input/instancia-'+str(instancia)+'.json')
with open('../timetabling/output/JSON/salida-'+str(instancia)+'.json') as s:
    salida = json.load(s)
semilla = salida['X']
print('[+] Semilla cargada\n')
# Calcular Funcion Fitness, Funcion Objetivo y  Z
Zmin = Z(salida['X'])
print('[*] Calculando F(semilla) ...')
pobjetivo = { "input" : input, "variables" : salida, "K" : 1000, "Zanterior" : Zmin, "Znueva" : Zmin, "wd" : semilla }
PE, Znueva, F,check = fun_objetivo(pobjetivo)
original=Molecula(-1,semilla, 0 , PE, 0, semilla, PE, 0, Znueva,check )
pobjetivo['original']=original
print('[i] '+'PE'.ljust(12,' ')+str(PE).rjust(24,' '))
print('[i] '+'f(x)'.ljust(12,' ')+str(F).rjust(24,' '))
print('[i] '+'Z'.ljust(12,' ')+str(Znueva).rjust(24,' '))
print('[i] '+'valida'.ljust(12,' ')+str(check).rjust(24,' '))
print('[+] F(semilla) calulcada\n')
pinicio= {      'input': input, 'porcentajeKE': porcentaje, 'size' : popSize     }
pneighbor = {   'nsig': len(input['salones']), 'input':input    }
solucion=CRO( KELossRate, colision, finicio, pinicio, fun_objetivo, pobjetivo, pneighbor, alfa, beta, criterios)
# guardar solucion
horario=MatricesX(solucion.w)
# input()
file=open("../timetabling/output/JSON/salida-optimizada-"+str(instancia)+".json",'w')
filename=file.name
file.write(str(horario))
file.close()
shedule=timetable(horario['X'],'horario-'+str(instancia))
dibujarHorario(shedule,input,'horario-optimizado-'+str(instancia))