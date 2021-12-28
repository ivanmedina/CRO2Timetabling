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