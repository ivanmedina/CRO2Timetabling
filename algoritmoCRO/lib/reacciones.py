from funciones import neighborhood
from operadores import *

def colision_inef_pared( M, buffer, neighbor, fobjetivo, pobjetivo, KELossRate ):
    wd=neighbor(M.w) # neighbor(m)
    PEwd=fobjetivo( pobjetivo, )
    if M.PE  + M.KE >= PEwd:
        q=random.uniform( KELossRate, 1 )
        M.PE=fobjetivo()
        KEwd= ( M.PE + M.KE - PEwd ) * q
        buffer = buffer + ( M.PE + M.KE - PEwd ) * ( 1- q )
        M.w=wd
        M.pe=PEwd
        M.KE = KEwd
    return [ M, buffer ]


def colision_inef_intermol( M1, M2, neighbor, fobjetivo ):
    wd1=neighbor(M1.w)
    wd2=neighbor(M2.w)
    PEwd1 = fobjetivo
    PEwd2 = fobjetivo
    temp2 =  ( M1.PE + M2.PE + M1.KE + M2.KE ) - ( PEwd1 + PEwd2 )
    if temp2 >= 0:
        p=random.uniform( 0, 1 )
        KEwd1 = temp2 * p
        KEwd2 = temp2 * ( 1 - p )
        M1.w = wd1
        M1.PE = PEwd1
        M1.KE = KEwd1
        M2.w = wd2
        M2.PE = PEwd2
        M2.KE = KEwd2
    return [ M1, M2 ]

def sintesis( M1, M2 ):
    pass

def descomposicion( M, buffer ):
    pass

def fobjetivo_prueba( w ):
    pass