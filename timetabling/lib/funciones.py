from decimal import Decimal, getcontext
import copy
from decimal import Decimal
import random
getcontext().prec = 16

def iniciarX(d,e,s,c,p):
    x=[ [ [ [ [ 0 for p in range(0,p) ] for c in range(0,c) ] for s in range(0,s) ] for e in range(0,e) ] for d in range(0,d) ]
    return x

def iniciarEnteros(e,s):
    x= [ [ [ 0 , 0] for s in range(0,s)] for e in range(0,e) ]
    return x

def cursosDisponible(Y):
    return [ c for c in range(0,len(Y)) if not '1' in str(Y[c]) ]
                    
def salonesDisponibles(G, d, e):
    disponibles =  [ s for s in range(0,len(G[d][e])) if str(G[d][e][s]) != '1'  ]
    if len(disponibles) > 3: return disponibles[:-2]
    return disponibles

def profesoresDisponibles(O,d,e):
    return [ p for p in range(0,len(O[d][e])) if str(O[d][e][p]) != '1'  ]

def cantCursosProfesor(Y,p):
    return  sum([ int(Y[c][p]) for c in range(0,len(Y)) ])

def maxHoras(input):
    maxim=0
    for i in range(1, len(input['cursos'])):
        if input['cursos'][i]['horas']>input['cursos'][maxim]['horas']:
            maxim=i
    return maxim


def aplanarX(X):
    array=[]
    for d in range(len(X)):
        for e in range(len(X[d])):
            for s in range(len(X[d][e])):
                for c in range(len(X[d][e][s])):
                    for p in range(len(X[d][e][s][c])):
                        array.append(X[d][e][s][c][p])
    return array

def rearmarX(X,input):
    i=0
    dias=[]
    for d in range(0,len(input['dias'])):
        eventos=[]
        for e in range(0,len(input['espacios'])):
            salones=[]
            for s in range(0,len(input['salones'])):
                cursos=[]
                for c in range(0,len(input['cursos'])):
                    profesores=[]
                    for p in range(0,len(input['profesores'])):
                        profesores.append(X[i])
                        i=i+1
                    cursos.append(profesores)
                salones.append(cursos)
            eventos.append(salones)
        dias.append(eventos)
    return dias

def E(array):
    return sum(array)

def Z(X):
    q=QdeX(X)
    # print('q> ',q )
    suma=0
    for s in range(0,len(q)):
        suma=suma+q[s]
    return float(float(suma) / len(q))

def WdeX(X):

    W = [ [ 0 for c in range(0,len(X[0][0][0])) ] for d in range(0,len(X))  ]

    for d in range(0,len(X)):
        for e in range(0,len(X[d])):
            for s in range(0,len(X[d][e])):
                for c in range(0,len(X[d][e][s])):
                    for p in range(0,len(X[d][e][s][c])):
                        if X[d][e][s][c][p] > 0:
                            W[d][c] = 1
    return W
            
def YdeX(X):

    Y = [ [ 0 for p in range( 0, len( X[0][0][0][0] ) ) ] for c in range( 0,len( X[0][0][0] ) )  ]

    for d in range(0,len(X)):
        for e in range(0,len(X[d])):
            for s in range(0,len(X[d][e])):
                for c in range(0,len(X[d][e][s])):
                    for p in range(0,len(X[d][e][s][c])):
                        if X[d][e][s][c][p] > 0:
                            Y[c][p] = 1
    return Y

def UdeX(X):

    U = [ 0 for c in range( 0,len( X[0][0][0] ) )  ]
    find=False

    for c in range(0,len(U)):
        for d in range(0,len(X)):
            for e in range(0,len(X[d])):
                for s in range(0,len(X[d][e])):
                    for p in range(0,len(X[d][e][s][c])):
                        if X[d][e][s][c][p] > 0:
                            U[c] = e
                            find = True
                            break
                    if find: break
                if find: break
            if find: break
    return U

def VdeX(X):
    
    V = [ [ 0 for s in range(0,len(X[0][0]))] for c in range( 0,len( X[0][0][0] ) )  ]
    
    for d in range(0,len(X)):
        for e in range(0,len(X[d])):
            for s in range(0,len(X[d][e])):
                for c in range(0,len(X[d][e][s])):
                    for p in range(0,len(X[d][e][s][c])):
                        if X[d][e][s][c][p] > 0:
                            V[c][s] = 1
    return V

def GdeX(X):
    
    G = [ [ [ 0 for s in range(0,len( X[0][0] ) ) ] for e in range(0,len( X[0] ) ) ] for d in range( 0,len( X ) )  ]
    
    for d in range(0,len(X)):
        for e in range(0,len(X[d])):
            for s in range(0,len(X[d][e])):
                for c in range(0,len(X[d][e][s])):
                    for p in range(0,len(X[d][e][s][c])):
                        if X[d][e][s][c][p] > 0:
                            G[d][e][s] = 1
    return G


def OdeX(X):
    
    O = [ [ [ 0 for p in range(0,len( X[0][0][0][0] ) ) ] for e in range(0,len( X[0] ) ) ] for d in range( 0,len( X ) )  ]
    
    for d in range(0,len(X)):
        for e in range(0,len(X[d])):
            for s in range(0,len(X[d][e])):
                for c in range(0,len(X[d][e][s])):
                    for p in range(0,len(X[d][e][s][c])):
                        if X[d][e][s][c][p] > 0:
                            O[d][e][p] = 1
    return O

def QdeX(X):
    Q = [ 0 for s in range( 0,len( X[0][0] ) )  ]
    find=False
    for d in range(0,len(X)):
        for e in range(0,len(X[d])):
            for s in range(0,len(X[d][e])):
                for c in range(0,len(X[d][e][s])):
                    for p in range(0,len(X[d][e][s][c])):
                        if X[d][e][s][c][p] == 1:
                            Q[s] = 1
    return Q

def GammaX(X):
    gamma = [ [ -1 for c in range(0,len(X[0][0][0])) ] for d in range(0,len(X)) ]
    for c in range(0,len(X[0][0][0])):
        for d in range(0,len(X)):
            for e in range(0,len(X[d])):
                primero=False
                for s in range(0,len(X[d][e])):
                    for p in range(0,len(X[d][e][s][c])):
                        if X[d][e][s][c][p] == 1:
                            gamma[d][c] = e
                            primero = True
                            break
                    if primero: break
                if primero: break
            
    return gamma

def OmegaX(X):
    omega = [ [ -1 for c in range(0,len(X[0][0][0])) ] for d in range(0,len(X)) ]
    for c in range(0,len(X[0][0][0])):
        for d in range(0,len(X)):
            for e in range(len(X[d])-1,-1, -1):
                ultimo=False
                for s in range(0,len(X[d][e])):
                    for p in range(0,len(X[d][e][s][c])):
                        if X[d][e][s][c][p] == 1:
                            omega[d][c] = e
                            ultimo = True
                            break
                    if ultimo: break
                if ultimo: break
    return omega

def Intensidades(cursos):
    I=[]
    high=0
    index=0
    for i in range(0, len(cursos)):
        if not cursos[i]['horas']in list(I):
            I.append(cursos[i]['horas'])
        if cursos[i]['horas']>high:
            high=cursos[i]['horas']
            index=i
    return [ I, index ]
    
def IntensidadesCursos(I,cursos):
    IC=[]
    for i in range(0,len(I)):
        temp=[]
        for c in range(0,len(cursos)):
            if cursos[c]['horas'] == I[i]:
                temp.append(c)
        IC.append(temp)
    return IC

def MatricesX(X):
    return {
        "X": X,
        "G" : GdeX(X),
        "O" : OdeX(X),
        "W" : WdeX(X),
        "Y" : YdeX(X),
        "V" : VdeX(X),
        "U" : UdeX(X),
        "Q" : QdeX(X),
        "gamma": GammaX(X),
        "omega": OmegaX(X)
    }

def XaEnteros(X):
    iterator=0
    timetable= [ [ [] for s in range(0,len(X[0][0]))  ] for e in range(0,len(X)*len(X[0])) ]                    
    for d in range(0,len(X)):
        for e in range(0,len(X[d])):
            for s in range(0,len(X[d][e])):
                for c in range(0,len(X[d][e][s])):
                    for p in range(0,len(X[d][e][s][c])):
                        if X[d][e][s][c][p] == 1:
                            timetable[iterator][s]=[0,0]
                            timetable[iterator][s][0]=c
                            timetable[iterator][s][1]=p
            iterator=iterator+1
    return timetable

def eventoDE(h, D, E):
    k=0
    for i in range(0,D):
        for j in range(0,E):
            if h==k:
                return [i ,j]
            k=k+1
    return [-1, -1]

def EnterosaX(enteros, input):
    X=iniciarX( len(input['dias']), len(input['espacios']), len(input['salones']), len(input['cursos']), len(input['profesores']) )
    d=0
    e=0
    for h in range(0,len(enteros)):
        for s in range(0,len(input['salones'])):
            if len(enteros[h][s])==2:
                X[d][e][s][enteros[h][s][0]][enteros[h][s][1]]=1
        if e<len(input['espacios'])-1:
            e=e+1
        else:
            d=d+1
            e=0
    return X

def UbicarC(enteros,c):
    coors=[]
    for e in range(0,len(enteros)):
        for s in range(0,len(enteros[e])):
            if len(enteros[e][s])>0:
                if enteros[e][s][0]==c:
                    coors.append([e,s])
    return coors

def ColumnaMatriz(Matriz, c):
    columnas=[]
    for i in range(0,len(Matriz)):
        if len(Matriz[i][c])>0:
            columnas.append(Matriz[i][c])
        else:
            columnas.append([])
    return columnas

def FilaMatriz(Matriz, f):
    filas=[]
    for i in range(0,len(Matriz[f])):
        if len(Matriz[f][i])>0:
            filas.append(Matriz[f][i])
        else:
            filas.append([])
    return filas

def randomX(input):
    rd= random.randint(0, len(input['dias']) -1 )
    re= random.randint(0, len(input['espacios']) -1 )
    rs= random.randint(0, len(input['salones']) -1 )
    rc= random.randint(0, len(input['cursos']) -1 )
    rp= random.randint(0, len(input['profesores']) -1 )
    return [rd, re, rs, rc, rp]

def nuevaX(X, p1, p2):
    T=copy.deepcopy(X)
    temp= T[p1[0]][p1[1]][p1[2]][p1[3]][p1[4]]
    T[p1[0]][p1[1]][p1[2]][p1[3]][p1[4]] =T[p2[0]][p2[1]][p2[2]][p2[3]][p2[4]]
    T[p2[0]][p2[1]][p2[2]][p2[3]][p2[4]]= temp
    return T

def encontrarUnosX(X):
    coors0=[]
    coors1=[]
    for d in range(0,len(X)):
        for e in range(0,len(X[d])):
            for s in range(0,len(X[d][e])):
                for c in range(0,len(X[d][e][s])):
                    for p in range(0,len(X[d][e][s][c])):
                        if X[d][e][s][c][p]==1:
                            coors1.append([d,e,s,c,p])
                        else:
                            coors0.append([d,e,s,c,p])

    return [ coors0, coors1 ]

def PETotal( poblacion ):
    TEpe=0
    for i in poblacion:
        TEpe = TEpe + i.PE
    # initialKE = TEpe / 100 * percent
    # TE= TEpe + ( initialKE *len(poblacion) )
    return TEpe

def calcularInitialKE( EPT , porcentaje ):
    return Decimal(float(EPT / 100) * porcentaje)

def CalcularTE( poblacion, buffer = 0 ):
    TE=0
    for i in poblacion:
        TE = TE + ( i.PE + i.KE )
    return TE +buffer

def setKE(poblacion, initialKE):
    for i in range(0,len(poblacion)):
        poblacion[i].KE = initialKE
    return poblacion 

def TEstr(TE):
    print('|'.rjust(29,' ')+('TE'.ljust(6,' ')+str(TE).rjust(16,' ')).rjust(90,' '))

def EnergiasStr(porcentaje, initialKE, TE):
    TEstr(TE)
    print('[i] '+'%'.ljust(12,' ')+str( porcentaje).rjust(24,' '))
    print('[i] '+'initialKE'.ljust(12,' ')+str(initialKE).rjust(24,' '))