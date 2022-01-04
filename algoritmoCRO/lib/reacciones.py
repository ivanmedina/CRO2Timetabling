from funciones import neighborhood
from operadores import *

def colision_inef_pared( M, buffer, neighbor, fobjetivo, pobjetivo, KELossRate ):
    wd=neighbor(M.w) # neighbor(m)
    PEwd=fobjetivo()
    if M.PE  + M.KE >= PEwd:
        q=random.uniform( KELossRate, 1 )
        M.PE=fobjetivo()
        KEwd= ( M.PE + M.KE - PEwd ) * q
        buffer = buffer + ( M.PE + M.KE - PEwd ) * ( 1- q )
        M.KE = KEwd
        M.w=wd
    return [ M, buffer ]


def colision_inef_intermol( M1, M2, neighbor ):
    wd1=neighbor(M1.w)
    wd2=neighbor(M2.w)

def sintesis( M1, M2 ):
    pass

def descomposicion( M, buffer ):
    pass

def fobjetivo_prueba( w ):
    pass