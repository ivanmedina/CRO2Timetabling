import random
from funciones import *
from reacciones import *
from operadores import *

def CRO( initialKE, KELossRate, colision, finicio, pinicio, fobjetivo, pobjetivo, ffitness, fcriterio, pcriterio ):

    poblacion = inicializacion( finicio, pinicio, initialKE, ffitness, fobjetivo, pobjetivo )
    pobSize = len(poblacion)
    buffer = 0
    mejor = None

    while( not criterio( fcriterio, pcriterio ) ):
        t=random.uniform(0,1)
        if t > colision: # revisar si es colision intermolecular
            m = selMolecula() # seleccionar molecula
            if esDescomposicion():
                mds=descomposicion(  )
                md1=mds[0] # molecula 1
                md2=mds[1] # molecula 2
                poblacion.pop( m.n )
                poblacion.append( md1 ) # agregar molecula 1 a la poblacion
                poblacion.append( md2 ) # agregar molecula 2 a la poblacion
            else:
                md=colision_inef_pared( m, buffer, randomRotate, fobjetivo, pobjetivo, KELossRate ) 
                poblacion[m.n]=md # remplazar molecula en la poblacion
        else:
            m1=selMolecula()  # seleccionar molecula 1
            m2=selMolecula()  # seleccionar molecula 2
            if esSintesis():
                md=sintesis( m1, m2, halfExchange, fobjetivo, pobjetivo, pobSize, initialKE )
                if(md[1]): # si es una reaccion exitosa
                    poblacion.pop( m1.n ) # remover molecula 1 de la poblacion
                    poblacion.pop( m2.n ) # remover molecula 2 de la poblacion
                    poblacion.append( md ) # agregar nueva molecula a la poblacion
            else:
                mds=colision_inef_intermol( m1, m2 )
                md1=mds[0] # molecula 1
                md2=mds[1] # molecula 2
                poblacion[m1.n]=md1 # remplazar molecula 1
                poblacion[m2.n]=md2 # remplazar molecula 2
        mejor=mejorSolucion(poblacion)
    return mejor