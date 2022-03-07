import random
import sys
from time import sleep
from time import time
from lib.funciones import *
from lib.reacciones import *
from lib.operadores import *
from timetabling.lib.funciones import MatricesX, rearmarX, Z
from decimal import Decimal, getcontext

from timetabling.lib.operaciones import RDCheck
getcontext().prec = 16
def remplazarIndividuo(poblacion, n , nm):
    for i in range(0,len(poblacion)):
        if poblacion[i].n == n:
            poblacion[i] = nm
            break
    return poblacion

def mejorSolucion(poblacion,mejor):
    # print('mejor PE antes> ',mejor.PE)
    for i in range( 0, len(poblacion) ):
        if mejor.valid:
            if (Decimal(poblacion[i].PE) <= Decimal(mejor.PE) and poblacion[i].valid and Decimal(poblacion[i].Z) > mejor.Z ) :
            # print(float(poblacion[i].PE) +'<'+ float(mejor.PE))
                mejor = poblacion[i]
        elif (Decimal(poblacion[i].PE) <= Decimal(mejor.PE) ):
                mejor = poblacion[i]

    # print('mejor> ',mejor.n, mejor.PE)
    winner = Molecula(mejor.n, mejor.w, mejor.KE, Decimal(mejor.PE), mejor.hits, mejor.minimumw, mejor.minimumPE, mejor.minimumhits, mejor.Z, mejor.valid)
    fin = time.time()
    return [ winner,  fin ]
        

def CRO( KELossRate, colision, finicio, pinicio, fobjetivo, pobjetivo, pneighbor, alfa, beta, criterios ):
    poblacion, TE, initialKE = finicio( pinicio ) #inicializacion
    print('\n'+'#'*20+' Etapa 2 ' +'#'*20+'\n')
    pobSize = len(poblacion)
    buffer = 0
    mejor, fin = mejorSolucion(poblacion,poblacion[0])
    iteracion = 0
    try:
        # CRITERIOS DE ITERACION 
        pinicio['inicio']=time.time()
        while( pobSize < criterios['a'] and pobSize > criterios['b'] and iteracion < criterios['c'] ):
            t=random.uniform(0,1)
            if t > colision: # revisar si no es colision intermolecular
                m = random.choice(poblacion) # seleccionar molecula
                if m.hits - m.minimumhits > alfa:
                    mds=descomposicion( m, Decimal(buffer), operador_descomposicion, pneighbor, fobjetivo, pobjetivo, pobSize, initialKE )
                    if mds[3]:
                        md1=mds[0] # molecula 1
                        md2=mds[1] # molecula 2
                        poblacion.remove( m )
                        poblacion.append( md1 ) # agregar molecula 1 a la poblacion
                        poblacion.append( md2 ) # agregar molecula 2 a la poblacion 
                        buffer = Decimal(mds[2])
                        print(    ( "| Z:".ljust(10, ' ')  + ("{:.8F} ".format(md1.Z).rjust(8,' '))).rjust(49,' ') )
                        print(    ( "| Z:".ljust(10, ' ')  + ("{:.8F} ".format(md2.Z).rjust(8,' '))).rjust(49,' ') )
                        if (Decimal(TE) < Decimal(CalcularTE(poblacion,buffer)) <Decimal(TE) ):
                            ajuste = Decimal(TE) - Decimal(CalcularTE(poblacion,buffer))
                            buffer = Decimal(ajuste) + Decimal(buffer)
                else:
                    md=colision_inef_pared( m, buffer, operador_inef_pared, pneighbor, fobjetivo, pobjetivo, KELossRate )
                    if md[0].PE < md[0].minimumPE:
                        md[0].minimumPE = md[0].PE 
                        md[0].minimumhits = md[0].hits 
                        md[0].minimumw = md[0].w
                    print(    ( "| Z:".ljust(10, ' ')  + ("{:.8F} ".format(md[0].Z).rjust(8,' '))).rjust(49,' ') )
                    
                    poblacion = remplazarIndividuo( poblacion, m.n, md[0] )
                    buffer=Decimal(md[1])
                    # Ajuste para reducir ruido del punto flotante
                    if Decimal(TE) > Decimal(CalcularTE(poblacion,buffer) ):
                        ajuste = Decimal(TE) - Decimal(CalcularTE(poblacion,buffer))
                        buffer = Decimal(ajuste) + Decimal(buffer) 
                    CalcularTE(poblacion,buffer)
            elif len(poblacion) > 1:
                n1 = n2 = m1 = m2 = enough =0
                while(n1==n2 and len(poblacion)>1 and enough <1):
                    m1=random.choice(poblacion)  # seleccionar molecula 1
                    m2=random.choice(poblacion)  # seleccionar molecula 2
                    if m1.n == m2.n and len(poblacion)<3:
                        break
                    else: 
                        n1=m1.n
                        n2=m2.n 
                        enough=1
                if enough and m1.n != m2.n:
                    if m1.KE <= beta and m2.KE < beta:
                        md=sintesis( m1, m2, operador_sintesis, pneighbor, fobjetivo, pobjetivo, pobSize, initialKE )
                        if(md[1]): # si es una reaccion exitosa
                            poblacion.remove( m1 ) # remover molecula 1 de la poblacion
                            poblacion.remove( m2 ) # remover molecula 2 de la poblacion
                            poblacion.append( md[0] ) # agregar nueva molecula a la poblacion
                            print(    ( "| Z:".ljust(10, ' ')  + ("{:.8F} ".format(m1.Z).rjust(8,' '))).rjust(49,' ') )
                            print(    ( "| Z:".ljust(10, ' ')  + ("{:.8F} ".format(m2.Z).rjust(8,' '))).rjust(49,' ') )
                    else:
                        mds=colision_inef_intermol( m1, m2, operador_inef_intermol, pneighbor, fobjetivo, pobjetivo )
                        md1=mds[0] # molecula 1
                        md2=mds[1] # molecula 2
                        if md1.PE < md1.minimumPE:
                            md1.minimumPE = md1.PE 
                            md1.minimumhits = md1.hits 
                            md1.minimumw = md1.w
                        if md2.PE < md2.minimumPE:
                            md2.minimumPE = md2.PE 
                            md2.minimumhits = md2.hits
                            md2.minimumw = md2.w 
                        poblacion = remplazarIndividuo( poblacion, m1.n, md1)
                        print(    ( "| Z:".ljust(10, ' ')  + ("{:.8F} ".format(m1.Z).rjust(8,' '))).rjust(49,' ') )
                        print(    ( "| Z:".ljust(10, ' ')  + ("{:.8F} ".format(m2.Z).rjust(8,' '))).rjust(49,' ') )
                        poblacion = remplazarIndividuo( poblacion, m2.n, md2)
            mejor , fin =mejorSolucion(poblacion,mejor)
            pobSize= len(poblacion)
            iteracion = iteracion +1
            TEstr(CalcularTE(poblacion,buffer))
            print('|'.rjust(29,' ')+(("Mejor PE: {:.16F} ".format(mejor.PE))).rjust(60,' '))
        print('Mejor Solucion: ')
        print('Antes:   ',pobjetivo['original'].toString())
        print('Despues: ',mejor.toString())
        print('Tiempo: ', fin - pinicio['inicio'] ,' s.')
        return mejor
    except KeyboardInterrupt:
        print('\n'+ '*'*40+' Aborted '+'*'*40)
        print('Mejor Solucion: ')
        print('Antes:   ',pobjetivo['original'].toString())
        print('Despues: ',mejor.toString())
        print('Tiempo: ', fin - pinicio['inicio'] ,' s.')
        return mejor