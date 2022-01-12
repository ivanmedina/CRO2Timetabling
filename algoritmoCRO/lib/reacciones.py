from lib.funciones import *
from lib.operadores import *
from lib.molecula import Molecula

def colision_inef_pared( M, buffer, neighbor, pneighbor, fobjetivo, pobjetivo, KELossRate ):
    print('[*] colision_inef_pared')
    M.hits=M.hits+1
    wd=neighbor(M.w, pneighbor) # neighbor(m)
    pobjetivo['Zanterior'] = M.Z
    PEwd, Znueva=fobjetivo( pobjetivo )
    M.Z = Znueva
    if float(M.PE)  + float(M.KE) >= float(PEwd):
        q=random.uniform( KELossRate, 1 )
        KEwd= ( float(M.PE) + float(M.KE) - float(PEwd) ) * float(q)
        buffer = float(float(buffer) + float( M.PE) + float(M.KE) - float(PEwd)  * float(1 - q ))
        M.w=wd
        M.PE= float(PEwd)
        M.KE = float(KEwd)
    print('end')
    return [ M, float(buffer) ]


def colision_inef_intermol( M1, M2, neighbor, pneighbor, fobjetivo, pobjetivo ):
    print('[**] colision_inef_intermol')
    M1.hits = M1.hits + 1
    M2.hits = M2.hits + 1
    wd1=neighbor(M1.w, pneighbor)
    wd2=neighbor(M2.w, pneighbor)
    pobjetivo1 = pobjetivo
    pobjetivo2 = pobjetivo
    pobjetivo1['wd']=wd1
    pobjetivo2['wd']=wd2
    pobjetivo1['Zanterior']=M1.Z
    pobjetivo2['Zanterior']=M2.Z
    PEwd1, Z1nueva = fobjetivo( pobjetivo1 )
    PEwd2, Z2nueva = fobjetivo( pobjetivo2 )
    temp2 =  ( M1.PE + M2.PE + M1.KE + M2.KE ) - ( PEwd1 + PEwd2 )
    if temp2 >= 0:
        p=random.uniform( 0, 1 )
        KEwd1 = temp2 * p
        KEwd2 = temp2 * ( 1 - p )
        M1.w = wd1
        M1.PE = PEwd1
        M1.KE = KEwd1
        M1.Z = Z1nueva
        M2.w = wd2
        M2.PE = PEwd2
        M2.KE = KEwd2
        M2.Z = Z2nueva
    print('end')
    return [ M1, M2 ]

def sintesis( M1, M2, neighbor, pneighbor, fobjetivo, pobjetivo, pobSize, InitialKE ):
    print('[**] sintesis')
    M1.hits=M1.hits+1
    M2.hits=M2.hits+1
    wd = neighbor(M1.w, M2.w, pneighbor)
    pobjetivo['wd']=wd
    pobjetivo['Zanterior']= float(( M1.Z + M2.Z ) / 2)
    PEwd, Znueva = fobjetivo( pobjetivo )
    exito = False
    Md = Molecula( pobSize, wd, InitialKE, PEwd, 0, wd, PEwd, 0, Znueva )
    if M1.PE + M2.PE + M1.KE + M2.KE >= Md.PE:
        Md.KE = M1.PE + M2.PE + M1.KE + M2.KE - Md.PE
        exito = True
    return [ Md , exito ]


def descomposicion( M, buffer, neighbor, pneighbor, fobjetivo, pobjetivo, pobSize, InitialKE ):
    print('[ * ] descomposicion')
    M.hits = M.hits + 1 
    wds = neighbor( M.w, pneighbor )
    pobjetivo1 = pobjetivo
    pobjetivo2 = pobjetivo
    pobjetivo1['wd']=wds[0]
    pobjetivo2['wd']=wds[1]
    pobjetivo1['Zanterior']=M.Z
    pobjetivo2['Zanterior']=M.Z
    PEwd1, Znueva1 =  fobjetivo( pobjetivo1 )
    PEwd2, Znueva2 =  fobjetivo( pobjetivo2 )
    Md1 = Molecula( pobSize, wds[0], InitialKE, PEwd1, 0, wds[0], PEwd1, 0,Znueva1 )
    Md2 = Molecula( pobSize+1, wds[1], InitialKE, PEwd2, 0, wds[1], PEwd2, 0, Znueva2 )
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
        buffer = temp1 + buffer - Md1.KE - Md2.KE
    return [ Md1, Md2, buffer, exito]          