def cursosDisponible(Y):
    return [ c for c in range(0,len(Y)) if not '1' in str(Y[c]) ]
                    
def salonesDisponibles(G, d, e):
    return [ s for s in range(0,len(G[d][e])) if str(G[d][e][s]) != '1'  ]

def profesoresDisponibles(O,d,e):
    return [ p for p in range(0,len(O[d][e])) if str(O[d][e][p]) != '1'  ]

def cantCursosProfesor(Y,p):
    return  sum([ int(Y[c][p]) for c in range(0,len(Y)) ])