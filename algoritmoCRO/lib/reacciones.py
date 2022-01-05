from lib.funciones import *
from lib.operadores import *
from lib.molecula import Molecula

def colision_inef_pared( M, buffer, neighbor, pneighbor, fobjetivo, pobjetivo, KELossRate ):
    wd=neighbor(M.w, pneighbor) # neighbor(m)
    PEwd=fobjetivo( pobjetivo )
    if M.PE  + M.KE >= PEwd:
        q=random.uniform( KELossRate, 1 )
        M.PE=fobjetivo( pobjetivo )
        KEwd= ( M.PE + M.KE - PEwd ) * q
        buffer = buffer + ( M.PE + M.KE - PEwd ) * ( 1- q )
        M.w=wd
        M.pe=PEwd
        M.KE = KEwd
    return [ M, buffer ]


def colision_inef_intermol( M1, M2, neighbor, pneighbor, fobjetivo, pobjetivo ):
    wd1=neighbor(M1.w, pneighbor)
    wd2=neighbor(M2.w, pneighbor)
    PEwd1 = fobjetivo( pobjetivo )
    PEwd2 = fobjetivo( pobjetivo )
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

def sintesis( M1, M2, neighbor, pneighbor, fobjetivo, pobjetivo, pobSize, InitialKE ):
    wd = neighbor(M1.w, M2.w, pneighbor)
    PEwd = fobjetivo( pobjetivo )
    exito = False
    Md = Molecula( pobSize, wd, InitialKE, PEwd )
    if M1.PE + M2.PE + M1.KE + M2.KE >= Md.PE:
        Md.KE = M1.PE + M2.PE + M1.KE + M2.KE - Md.PE
        exito = True
    return [ Md , exito ]


def descomposicion( M, buffer, neighbor, pneighbor, fobjetivo, pobjetivo, pobSize, InitialKE ):
    wds = neighbor( M.w, pneighbor )
    Md1 = Molecula( pobSize, wds[0], InitialKE, fobjetivo( pobjetivo ) )
    Md2 = Molecula( pobSize+1, wds[1], InitialKE, fobjetivo( pobjetivo ) )
    temp1 = M.PE + M.KE - Md1.PE - Md2.PE 
    exito = False
    if temp1 >= 0:
        exito = True
        k = random.uniform(0,1)
        Md1.KE = temp1 * k
        Md2.KE = temp1 * ( 1 - k)
    elif temp1 + buffer >= 0:
        exito = True
        m1 = random.uniform(0,1)
        m2 = random.uniform(0,1)
        m3 = random.uniform(0,1)
        m4 = random.uniform(0,1)
        Md1.KE = ( temp1 + buffer ) * m1 * m2
        Md2.KE = ( temp1 + buffer ) * m3 * m4
        buffer = temp1 + buffer - Md1.KE - Md2.ke
    return [ Md1, Md2, buffer, exito]          