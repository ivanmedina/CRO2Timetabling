def cursosDisponible(Y):
    return [ c for c in range(0,len(Y)) if not '1' in str(Y[c]) ]
                    
def salonesDisponibles(G, d, e):
    return [ s for s in range(0,len(G[d][e])) if str(G[d][e][s]) != '1'  ]

def profesoresDisponibles(O,d,e):
    return [ p for p in range(0,len(O[d][e])) if str(O[d][e][p]) != '1'  ]

def cantCursosProfesor(Y,p):
    return  sum([ int(Y[c][p]) for c in range(0,len(Y)) ])

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

def Z(X,G):
    suma=0
    for d in range(0,len(X)):
        for e in range(0,len(X[d])):
            for s in range(0,len(X[d][e])):
                for c in range(0,len(X[d][e][s])):
                    for p in range(0,len(X[d][e][s][c])):
                        suma=(X[d][e][s][c][p] * G[d][e][s] )+suma
    return suma

def WdeX(X):

    W = [ [ 0 for c in range(0,len(X[0][0][0])) ] for d in range(0,len(X))  ]

    for d in range(0,len(X)):
        for e in range(0,len(X[d])):
            for s in range(0,len(X[d][e])):
                for c in range(0,len(X[d][e][s])):
                    for p in range(0,len(X[d][e][s][c])):
                        if X[d][e][s][c][p] > 1:
                            W[d][c] = 1
    return W
            
def YdeX(X):

    Y = [ [ 0 for p in range( 0, len( X[0][0][0][0] ) ) ] for c in range( 0,len( X[0][0][0] ) )  ]

    for d in range(0,len(X)):
        for e in range(0,len(X[d])):
            for s in range(0,len(X[d][e])):
                for c in range(0,len(X[d][e][s])):
                    for p in range(0,len(X[d][e][s][c])):
                        if X[d][e][s][c][p] > 1:
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
                        if X[d][e][s][c][p] > 1:
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
                        if X[d][e][s][c][p] > 1:
                            V[c][s] = 1
    return V

def GdeX(X):
    
    G = [ [ [ 0 for s in range(0,len( X[0][0] ) ) ] for e in range(0,len( X[0] ) ) ] for d in range( 0,len( X ) )  ]
    
    for d in range(0,len(X)):
        for e in range(0,len(X[d])):
            for s in range(0,len(X[d][e])):
                for c in range(0,len(X[d][e][s])):
                    for p in range(0,len(X[d][e][s][c])):
                        if X[d][e][s][c][p] > 1:
                            G[d][e][s] = 1
    return G


def OdeX(X):
    
    O = [ [ [ 0 for p in range(0,len( X[0][0][0][0] ) ) ] for e in range(0,len( X[0] ) ) ] for d in range( 0,len( X ) )  ]
    
    for d in range(0,len(X)):
        for e in range(0,len(X[d])):
            for s in range(0,len(X[d][e])):
                for c in range(0,len(X[d][e][s])):
                    for p in range(0,len(X[d][e][s][c])):
                        if X[d][e][s][c][p] > 1:
                            O[d][e][p] = 1
    return O

def QdeX(X):

    Q = [ 0 for s in range( 0,len( X[0][0] ) )  ]
    find=False

    for c in range(0,len(Q)):
        for d in range(0,len(X)):
            for e in range(0,len(X[d])):
                for s in range(0,len(X[d][e])):
                    for p in range(0,len(X[d][e][s][c])):
                        if X[d][e][s][c][p] > 1:
                            Q[s] = 1
                            find = True
                            break
                    if find: break
                if find: break
            if find: break
    return Q

def MatricesX(X):
    
    return {
        "X": X,
        "G" : GdeX(X),
        "O" : OdeX(X),
        "W" : WdeX(X),
        "Y" : YdeX(X),
        "V" : VdeX(X),
        "U" : UdeX(X),
        "Q" : QdeX(X)
    }
