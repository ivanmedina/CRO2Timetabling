from decimal import Decimal, getcontext
from timetabling.lib.restricciones import R1, R12,R2,R3,R4,R5,R6,R7,R8,R9,R10,R11
getcontext().prec = 16
RSn=4
K=1000
RDn=8*K

def verificarR1(input,X):
    verificado=True
    for c in range(0,len(input['cursos'])):
        if not R1(input,X, c):
            verificado=False
            break
    return 1 if verificado else 0

def verificarR2(input,X):
    verificado=True
    for d in range(0,len(X)):
        for e in range(0,len(X[d])):
            for p in range(0,len(input['profesores'])):
                if not R2(X,d,e,p):
                    verificado=False
                    break
            if not verificado: break
        if not verificado: break
    return 1 if verificado else 0

def verificarR3(X):
    verificado=True
    for d in range(0,len(X)):
        for e in range(0,len(X[d])):
            for s in range(0,len(X[d][e])):
                if not R3(X,d,e,s):
                    verificado=False
                    break
            if not verificado: break
        if not verificado: break
    return 1 if verificado else 0

def verificarR4(input,Y):
    verificado=True
    for c in range(0,len(Y)):
        for p in range(0,len(Y[c])):
            if not R4(input,Y,c,p):
                verificado=False
        if not verificado: break
    return 1 if verificado else 0

def verificarR5(input,Y):
    verificado=True
    for p in range(0,len(input['profesores'])):
        if not R5(input,Y,p):
            verificado=False
            break
    return 1 if verificado else 0

def verificarR6(input,X):
    verificado=True
    for d in range(0,len(X)):
        for e in range(0,len(X[d])):
            for p in range(0,len(input['profesores'])):
                if not R6(input,X,d,e,p):
                    verificado=False
            if not verificado: break
        if not verificado: break
    return 1 if verificado else 0

def verificarR7(input,X):
    verificado=True
    for d in range(0,len(X)):
        for c in range(0,len(input['cursos'])):
            for p in range(0,len(input['profesores'])):
                if not R7(input,X,d,c,p):
                    verificado=False
                    break
            if not verificado: break
        if not verificado: break
    return 1 if verificado else 0

def verificarR8( input, X, Y, W, V, gamma, omega ):
    verificado=True
    for d in range(0,len(input['dias'])):
        for c in range(0,len(input['cursos'])):
            if not R8(input, X, Y, W, V, gamma, omega, c, d):
                verificado=False
                break
        if not verificado: break
    return 1 if verificado else 0


def verificarR9(V):
    verificado=0
    for c in range(0,len(V)):
        if not R9(V,c):
            verificado=verificado+(1/len(V))
    return verificado

def verificarR10(input,X,U,W):
    verificado=0
    for c in range(0,len(input['cursos'])):
        if not R10(X,U,W,c):
           verificado=verificado+(1/len(input['cursos']))
    return verificado 

def verificarR11(input,W):
    verificado=0
    # suma=0
    for d in range(0, len(W)-1):
        for c in range(0,len(W[d])):
            if not R11(W,d,c):
                verificado=verificado+(1/((len(input['dias'])-1)*(len(input['cursos']))))
                # break
        # if not verificado: break
    return verificado

def RDCheck(rd):
    if rd*K >=RDn:
        return 1
    return 0

def RD(input,variables):
    suma=0
    suma+=verificarR1(input,variables['X'])
    suma+=verificarR2(input,variables['X'])
    suma+=verificarR3(variables['X'])
    suma+=verificarR4(input,variables['Y'])
    suma+=verificarR5(input,variables['Y'])
    suma+=verificarR6(input,variables['X'])
    suma+=verificarR7(input,variables['X'])
    suma+=verificarR8(input,variables['X'], variables['Y'], variables['W'],variables['V'], variables['gamma'], variables['omega'])
    check=RDCheck(suma)
    return [suma, check]

def RS(input,variables,Zanterior,Znueva):
    suma=0
    suma+=verificarR9(variables['V'])
    suma+=verificarR10(input,variables['X'],variables['U'],variables['W'])
    suma+=verificarR11(input,variables['V'])
    suma+= 100 if R12(Zanterior,Znueva) else 0
    return suma

def fobjetivo(parametros):
    rd,check =  RD( parametros['input'],    parametros['variables'])
    rd=rd*K
    return [    rd   +   RS(     parametros['input'],    parametros['variables'],    parametros['Zanterior'],    parametros['Znueva']    ), check   ]

def fitness(Z):
    return Decimal(1/(Z))