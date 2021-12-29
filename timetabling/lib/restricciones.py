from lib.funciones import E

def R1(input,X,c):
    # R1 = Las materias se programan de acuerdo
    # a la cantidad de horas por semana requeridas.
    suma=0
    for d in range(0,len(X)):
        for e in range(0,len(X[d])):
            for s in range(0,len(X[d][e])):
                    for p in range(0,len(X[d][e][s][c])):
                        suma=X[d][e][s][c][p]+suma
    return suma>=input['cursos'][c]['horas']

def R2(X,d,e,p):
    # R2 = Los cursos asignados al mismo profesor
    # no deben ocurrir en el mismo periodo.
    suma=0
    for s in range(0,len(X[d][e])):
            for c in range(0,len(X[d][e][s])):
                suma=X[d][e][s][c][p]+suma
    return suma <= 1

def R3(X,d,e,s):
    # R3 = Un salón solo puede atender un curso por periodo.
    suma=0
    for c in range(0,len(X[d][e][s])):
            for p in range(0,len(X[d][e][s][c])):
                suma=X[d][e][s][c][p]+suma
    return suma <= 1

def R4(input,Y,c,p):
    # R4 = A los profesores solo se les pueden asignar
    # las materias que son capaces de enseñar.
    return Y[c][p]<=input['profesores'][p]['cursos'][c]

def R5(input,Y,p):
    # R5 = Los profesores pueden tener asignadas máximo 4 materias.
    suma=0
    for c in range(0,len(Y)):
        suma=Y[c][p]+suma
    return suma <= input['maxCP']

def R6(input,X,d,e,p):
    # R6 = Se debe respetar la disponibilidad del profesor.
    suma=0
    for s in range(0,len(X[d][e])):
            for c in range(0,len(X[d][e][s])):
                suma=X[d][e][s][c][p]+suma
    return suma <= input['profesores'][p]['disponible'][d][e]

    pass

def R7(input,X,d,c,p):
    # R7 = Las clases deben ser programadas en sesiones
    # diarias de máximo 3 horas consecutivas.
    suma=0
    for e in range(0,len(X[d])):
        for s in range(0,len(X[d][e])):
            suma=X[d][e][s][c][p]+suma
    return suma <= input['maxEC']

def R8(V,c):
    # R8 = A cada curso le corresponde solo un salón.
    suma=0
    for s in range(0,len(V[c])):
        suma=V[c][s]+suma
    return suma<=1

def R9(X,U,W,c):
    # R9 = Cursos asignados mas de un día deben empezar a la misma hora.
    sumaX=0
    for d in range(0,len(X)):
        for s in range(0,len(X[d][U[c]])):
            for p in range(0,len(X[d][U[c]][s][c])):
                sumaX=X[d][U[c]][s][c][p]+sumaX
    sumaW=0
    for d in range(0,len(W)):
        sumaW=W[d][c]+sumaW
    return sumaX==sumaW

def R10(W,d,c):
    # R10 = Debe haber al menos un día de descanso entre
    # sesiones del mismo curso
    return W[d][c]+W[d+1][c] <= 1


def R11():
    # R12 = Minimizar la cantidad de salones utilizados.
    pass

# E([1,2,3,4,5])