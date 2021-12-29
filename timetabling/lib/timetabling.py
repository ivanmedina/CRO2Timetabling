from lib.funciones import *

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
    L = [ [ 0 for e in range(0,En)] for d in range (0,Dn) ] # eventos
    O = [ [ [ 0 for p in range(0,Pn) ] for e in range(0,En) ] for d in range(0,Dn) ]

    while(len(cursosDisponible(Y))>0):
        # print(cursosDisponible(Y))
        c=cursosDisponible(Y)[0]
        # Y[c]=1
        for d in range(0,len(G)):
            find=False
            for e in range(0,len(G[d])):
                #seleccionar salon
                if (len(salonesDisponibles(G,d,e))>0):
                    s=salonesDisponibles(G,d,e)[0]
                    #revisa los profesores
                    pd=profesoresDisponibles(O,d,e)
                    if(len(pd)>0):
                        profesor=True
                        p=0
                        while(profesor and p<len(pd) and int(cantCursosProfesor(Y,pd[p]))<input['maxCP']):
                            horas=0
                            d2=d
                            e2=e
                            while horas < C[c]['horas']:
                                pdp=pd[p]
                                try:
                                    if P[pdp]['disponible'][d2][e2] == 1:
                                    #   #marcar profesor salon dia y evento y curso ocupados
                                        Y[c][pdp]=1
                                        V[c][s]=1
                                        X[d2][e2][s][c][pdp]=1
                                        U[c]=e
                                        G[d2][e2][s]=1
                                        O[d2][e2][pdp]=1
                                        W[d2][c]=1
                                        e2=e2+1
                                        horas=horas+1
                                    if e2==input['maxEC']:
                                        e2=e
                                        d2=d2+1
                                except:
                                    find=True
                                    profesor=False  
                                    break  
                            if horas==C[c]['horas'] or (e2>=En or d2>=Dn):
                                Q[s]=1
                                find=True
                                profesor=False
                            p=p+1
                if find:
                    break
            if find:
                break
    return {"X":X,"W":W,"Y":Y,"V":V,"Q":Q,"U":U,"G":G,"L":L,"O":O}