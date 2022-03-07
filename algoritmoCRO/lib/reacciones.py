from unicodedata import decimal
from lib.funciones import *
from lib.operadores import *
from lib.molecula import Molecula
from timetabling.lib.funciones import *
import time
from decimal import Decimal, getcontext
getcontext().prec = 16

def colision_inef_pared( M, buffer, neighbor, pneighbor, fobjetivo, pobjetivo, KELossRate ):
    print('[*] IP'.ljust(28,' ')+'|')
    M.hits=M.hits+1
    enteros=XaEnteros(M.w) # M.w es X
    wd=neighbor(enteros, pneighbor) # neighbor(m)
    pobjetivo['input']['X']=wd
    wd= EnterosaX(wd,pobjetivo['input'])
    pobjetivo['Zanterior'] = Decimal(M.Z)
    pobjetivo['wd'] = wd
    PEwd, Znueva,F,check =fobjetivo( pobjetivo )
    energia = Decimal(M.PE) + Decimal(M.KE)
    if energia >= Decimal(PEwd):
        # si es mayor, tomo el valor sobrante y lo meto al buffer
        q=Decimal(random.uniform( 0, KELossRate ))
        dif = Decimal(energia) - Decimal(PEwd)
        KEwd= Decimal(dif)  * Decimal(q)
        buffer = Decimal(buffer) + (Decimal(dif) - Decimal(KEwd))
        M.w=wd
        M.PE= Decimal(PEwd)
        M.KE = Decimal(KEwd)
        M.Z = Decimal(Znueva)
        M.valid = check
    return [ M, Decimal(buffer) ]


def colision_inef_intermol( M1, M2, neighbor, pneighbor, fobjetivo, pobjetivo ):
    print('[*]   II'.ljust(28,' ')+'|')
    M1.hits = M1.hits + 1
    M2.hits = M2.hits + 1
    enteros1=XaEnteros(M1.w)
    enteros2=XaEnteros(M2.w)
    wd1,wd2=neighbor(enteros1, enteros2, pneighbor)
    wd1=EnterosaX(enteros1,pobjetivo['input'])
    wd2=EnterosaX(enteros2,pobjetivo['input'])
    pobjetivo1 = pobjetivo
    pobjetivo2 = pobjetivo
    pobjetivo1['wd']=wd1
    pobjetivo2['wd']=wd2
    pobjetivo1['Zanterior']=Decimal(M1.Z)
    pobjetivo2['Zanterior']=Decimal(M2.Z)
    PEwd1, Z1nueva, F, check1 = fobjetivo( pobjetivo1 )
    PEwd2, Z2nueva, F, check2 = fobjetivo( pobjetivo2 )
    temp2 =  Decimal( M1.PE + M2.PE + M1.KE + M2.KE ) - Decimal( PEwd1 + PEwd2 )
    if temp2 >= 0:
        p=random.uniform( 0, 1 )
        KEwd1 = Decimal(temp2) * Decimal(p)
        KEwd2 = Decimal(temp2) - KEwd1
        M1.w = wd1
        M1.PE = Decimal(PEwd1)
        M1.KE = Decimal(KEwd1)
        M1.Z = Decimal(Z1nueva)
        M1.valid = check1
        M2.w = wd2
        M2.PE = Decimal(PEwd2)
        M2.KE = Decimal(KEwd2)
        M2.Z = Decimal(Z2nueva)
        M2.valid = check2
    return [ M1, M2 ]

def sintesis( M1, M2, neighbor, pneighbor, fobjetivo, pobjetivo, pobSize, InitialKE ):
    print('[*]     SI'.ljust(28,' ')+'|')
    M1.hits=M1.hits+1
    M2.hits=M2.hits+1
    # x1=rearmarX(M1.w,pobjetivo['input'])
    enteros1=XaEnteros(M1.w)
    # x2=rearmarX(M2.w,pobjetivo['input'])
    enteros2=XaEnteros(M2.w)
    pneighbor['iniciarEnteros']=iniciarEnteros
    wd = neighbor(enteros1, enteros2, pneighbor)
    wd=EnterosaX(wd,pobjetivo['input'])
    # wd=aplanarX(x)
    pobjetivo['wd']=wd
    pobjetivo['Zanterior']= Decimal(Decimal(( M1.Z + M2.Z ) / 2))
    PEwd, Znueva, F,check = fobjetivo( pobjetivo )
    exito = False
    Md = Molecula( pobSize, wd, InitialKE, PEwd, 0, wd, PEwd, 0, Znueva,check )
    temp3 =Decimal( M1.PE + M2.PE + M1.KE + M2.KE)
    if Decimal(temp3) >= Decimal(Md.PE):
        Md.KE = Decimal( temp3 - Md.PE)
        exito = True
    return [ Md , exito ]


def descomposicion( M, buffer, neighbor, pneighbor, fobjetivo, pobjetivo, pobSize, InitialKE ):
    print('[*]       DE'.ljust(28,' ')+'|')
    M.hits = M.hits + 1
    # Convertir X en matrices de enteros
    # x=rearmarX(M.w,pobjetivo['input'])
    enteros=XaEnteros(M.w)
    wds = neighbor( enteros, pneighbor )
    # Volver matriz de enteros a arreglo
    # sacar la x de matriz de enteros
    wds[0] = EnterosaX(wds[0], pobjetivo['input'])
    wds[1] = EnterosaX(wds[1], pobjetivo['input'])
    pobjetivo1 = pobjetivo
    pobjetivo2 = pobjetivo
    pobjetivo1['wd']=wds[0]
    pobjetivo2['wd']=wds[1]
    pobjetivo1['Zanterior']=Decimal(M.Z)
    pobjetivo2['Zanterior']=Decimal(M.Z)
    PEwd1, Znueva1, F, check1 =  fobjetivo( pobjetivo1 )
    PEwd2, Znueva2, F, check2 =  fobjetivo( pobjetivo2 )
    Md1 = Molecula( pobSize, wds[0], InitialKE, PEwd1, 0, wds[0], PEwd1, 0,Znueva1, check1 )
    Md2 = Molecula( pobSize+1, wds[1], InitialKE, PEwd2, 0, wds[1], PEwd2, 0, Znueva2, check2 )
    temp1 = Decimal(M.PE + M.KE - Md1.PE - Md2.PE)
    exito = False
    if temp1 >= 0:
        exito = True
        k = Decimal(random.uniform(0,1))
        Md1.KE = Decimal(temp1 * k)
        Md2.KE = Decimal(temp1 - Md1.KE)
    elif temp1 + buffer >= 0:
        exito = True
        m1 = random.uniform(0,1)
        m2 = random.uniform(0,1)
        m3 = random.uniform(0,1)
        m4 = random.uniform(0,1)
        temp2 = Decimal(temp1) + Decimal(buffer )
        Md1.KE = temp2 * Decimal(m1) * Decimal(m2)
        Md2.KE = (temp2 - Md1.KE) * Decimal(m3) * Decimal(m4)
        buffer = temp2 - Md1.KE -Md2.KE
    return [ Md1, Md2, buffer, exito]