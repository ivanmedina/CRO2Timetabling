import random
from lib.funciones import *
from timetabling.lib.funciones import ColumnaMatriz, FilaMatriz, UbicarC, iniciarX
import copy
################################################3

def operador_inef_pared(matriz,parametros):
    h= random.randint(0,len(parametros['input']['I'])-1)
    a,b = random.sample(parametros['input']['J'][h],2)
    A = UbicarC(matriz,a)
    B = UbicarC(matriz,b)
    for i in range(0,len(A)):
        try:
            temp=matriz[A[i][0]][A[i][1]]
            matriz[A[i][0]][A[i][1]]=matriz[B[i][0]][B[i][1]]
            matriz[B[i][0]][B[i][1]]=temp
        except:
            pass 
    return matriz

def operador_inef_intermol(matriz1, matriz2, parametros):
    a,b=random.sample(range(0,len(parametros['input']['cursos'])), 2)
    A=UbicarC(matriz1,a)
    B=UbicarC(matriz2,b)
    try:
        p1=matriz1[ A[0][0] ] [A[0][1] ][1]
        p2=matriz2[B[0][0]][B[0][1]][1]
        for i in A:
            matriz1[i[0]][i[1]][1]=p1
        for j in B:
            matriz2[j[0]][j[1]][1]=p2
    except: pass
    return [ matriz1, matriz2 ]


def operador_descomposicion(matriz,parametros):
    A = copy.deepcopy(matriz[:])
    B = copy.deepcopy(matriz[:])
    s = random.randint(0, len(matriz)-1)
    r = random.randint(0, len(matriz[0])-1)
    C= ColumnaMatriz(matriz,r)
    F= FilaMatriz(matriz,s)
    # *****************************************
    for i in range(0,len(C)):
        if i<1:
            A[i][r]=C[-1]
        else:
            A[i][r]=C[i-1]
    # # *****************************************
    for j in range(0,len(F)):
        if j < 1:
            B[s][j]=F[-1]
        elif j<len(F):
            B[s][j]=F[j-1]
    # *****************************************
    return [ A, B ]

def operador_sintesis( matriz1, matriz2, parametros ):
    a1=random.randint(0,len(matriz1)-1)
    a2=random.randint(0,len(matriz1[a1])-1)
    b1=random.randint(0,len(matriz2)-1)
    b2=random.randint(0,len(matriz2[b1])-1)
    matriz1[a1][a2]=matriz2[b1][b2]
    return matriz1