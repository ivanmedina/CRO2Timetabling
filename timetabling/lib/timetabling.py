import os
import sys
PROJECT_PATH = os.getcwd()
SOURCE_PATH = os.path.join(
    PROJECT_PATH,"../../"
)
sys.path.append(SOURCE_PATH)


from timetabling.lib.funciones import *

def timetabling(input):
    D = input['dias']
    E = input['espacios']
    S = input['salones']
    C = input['cursos']    
    P = input['profesores']
    
    Dn = len(input['dias'])
    En = len(input['espacios'])
    Sn = len(input['salones'])
    Cn = len(input['cursos'])
    Pn = len(input['profesores'])

    X= [ [ [ [ [ 0 for p in range(0,Pn) ] for c in range(0,Cn) ] for s in range (0,Sn) ] for e in range (0,En)] for d in range(0,Dn) ]
    W = [ [ 0 for c in range(0,Cn) ] for d in range(0,Dn) ] # 1 si el dia D se imparte el curso C
    Y = [ [ 0 for p in range(0,Pn) ] for x in range(0,Cn) ] # 1 si el profesor P imparte el curso C
    V = [ [ 0 for s in range(0,Sn) ] for c in range(0,Cn) ] # { 1 si el curso c es impartido en el salon s; 0 si no }
    Q = [ 0 for s in range(0,Sn) ]
    U = [ 0 for c in range(0,Cn) ] #primera sesion del curso
    G = [ [ [ 0 for s in range(0,Sn) ] for e in range(0,En) ] for d in range(0,Dn) ] # dias eventos salones 1 si esta ocupado
    O = [ [ [ 0 for p in range(0,Pn) ] for e in range(0,En) ] for d in range(0,Dn) ]
    gamma =  [ [ -1 for c in range(0,len(X[0][0][0])) ] for d in range(0,len(X)) ]
    omega =  [ [ -1 for c in range(0,len(X[0][0][0])) ] for d in range(0,len(X)) ]
    
    while(len(cursosDisponible(Y))>0):
        c=cursosDisponible(Y)[0]
        for d in range(0,len(G),2):
            find=False
            for e in range(0,len(G[d])):
                #seleccionar salon
                salondisponible=salonesDisponibles(G,d,e)
                if (len(salondisponible)>0):
                    sd=salondisponible
                    # intencionalmente no se permite el uso de todos los salones
                    s=sd[0]
                    #revisa los profesores
                    pd=profesoresDisponibles(O,d,e)
                    if(len(pd)>0 and s<(Sn/2)):
                        profesor=True
                        p=pd[0]
                        while(profesor and len(pd)>0 and int(cantCursosProfesor(Y,p))<input['maxCP']):
                            horas=0
                            d2=d
                            e2=e
                            while horas < C[c]['horas']:
                                pdp=p
                                if P[pdp]['disponible'][d2][e2] == 1 and G[d2][e2][s]==0 and O[d2][e2][pdp]==0:
                                #   #marcar profesor salon dia y evento y curso ocupados
                                    Y[c][pdp]=1
                                    V[c][s]=1
                                    X[d2][e2][s][c][pdp]=1
                                    U[c]=e
                                    G[d2][e2][s]=1
                                    O[d2][e2][pdp]=1
                                    W[d2][c]=1
                                    Q[s]=1
                                    e2=e2+1
                                    horas=horas+1
                                elif G[d2][e2][s]==1:
                                    d2=d2+1
                                elif O[d2][e2][pdp]==1:
                                    pd=profesoresDisponibles(O,d2,e2)
                                    p=0
                                if e2>=input['maxEC']:
                                    e2=e
                                    if d2<=Dn-2:d2=d2+2
                                    else:
                                        d2=d2+1
                                if d2>=Dn:
                                    d2=0
                                    e2=0
                            if horas>=C[c]['horas']:
                                find=True
                                profesor=False
                            if (e2>=En):e2=0
                            if (d2>=Dn):d2=0
                            p=profesoresDisponibles(O,d,e)
                            if(len(p) > 0):p=p[0]
                if find:
                    break
            if find:
                break
    gamma=GammaX(X)
    omega=OmegaX(X)
    return { "X":X,"W":W,"Y":Y,"V":V,"Q":Q,"U":U,"G":G,"O":O,"Z":Z(X),"gamma":gamma, "omega":omega }