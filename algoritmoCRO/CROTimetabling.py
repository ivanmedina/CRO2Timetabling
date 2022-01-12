import os
import sys
PROJECT_PATH = os.getcwd()
SOURCE_PATH = os.path.join(
    PROJECT_PATH,"../"
)
sys.path.append(SOURCE_PATH)

from timetabling.lib.funciones import *
from timetabling.lib.input import *
from timetabling.lib.timetabling import *
from timetabling.lib.operaciones import *
from algoritmoCRO.lib.molecula import Molecula
from algoritmoCRO.lib.cro import CRO

initialKE = 1
buffer = 0
KELossRate = 0.000001

colision =0.5

alfa = 1
beta = 0.005

criterios = { 'a' : 10, 'b' : 0, 'c' : 10 }

def finicio(poblacion):
    return poblacion

def fun_objetivo(pobjetivo):
    X = rearmarX(pobjetivo['wd'], pobjetivo['input'] )
    pobjetivo['variables'] = MatricesX( X )
    Znueva = Z(pobjetivo['variables']['X'],pobjetivo['variables']['G'])
    pobjetivo['Znueva'] = Znueva
    return [ float(fitness(fobjetivo( pobjetivo ))), float(Znueva) ]
input =  leerInput('./../timetabling/input/new_input.json')
salida=timetabling(input)
semilla = aplanarX(salida['X']) 
Zmin = Z(salida['X'],salida['G'])
pobjetivo = { "input" : input, "variables" : salida, "K" : 1000, "Zanterior" : 100000, "Znueva" : Zmin, "wd" : semilla }
PE, Znueva = fun_objetivo(pobjetivo)
poblacion = [  Molecula( 0, semilla, initialKE, PE, 0, semilla, PE, 0, Zmin  ) ] 
pneighbor = { 'nsig': len(input['salones']) }
solucion=CRO(initialKE, KELossRate, colision, finicio, poblacion, fun_objetivo, pobjetivo, pneighbor, alfa, beta, criterios)
print('mejor solucion> ',solucion.PE)