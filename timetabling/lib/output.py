from time import time

from timetabling.lib.funciones import XaEnteros
# Representacion binaria de la solución.
def dibujarTabla(X,input,nombre_archivo):
    horario=open('./../timetabling/output/HTML'+str(nombre_archivo)+'_bin.html','w')
    texto=""
    texto+="<html>"
    texto+="<head>"
    texto+="<style>"
    texto+="table, th, td {border: 1px solid black;}"
    texto+="</style>"
    texto+="</head>"
    texto+="<body>"
    texto+="<table style='width:90%;padding:10px'>"
    rgb=0xCD5C00
    for d in range(0,len(X)):
        rgb=rgb+0x5c
        texto+="<tr><th colspan=100%>Dia"+str(d)+"</th></tr>"
        texto+="<tr style='background-color:#"+hex(rgb)[2:]+";padding:10px'>"
        for e in range(0,len(X[d])):
            texto+="<td>Evento %d </td>" %(e)
            texto+="<td style=';padding:10px'>"
            for s in range(0,len(X[d][e])):
                texto+="<table style='width:100%;padding:10px'>"
                texto+="<tr><th colspan="+str(len(X[d][e][s])+1)+">Salon %d </th></tr>" % (s)
                for c in range(0,len(X[d][e][s])):
                    texto+="<tr><td colspan=100%>Curso "+str(c)+" </td></tr>"
                    texto+="<tr>"
                    for p in range(0,len(X[d][e][s][c])):
                        texto+="<td style=''>"
                        if(str(X[d][e][s][c][p])==str(1)):
                            texto+="<td style='background-color:green'>"+str(X[d][e][s][c][p])+"</td>"
                        else:
                            texto+="<td style='background-color:#3AFFFF'>"+str(X[d][e][s][c][p])+"</td>"
                        texto+="</td>"
                    texto+="</tr>"
                texto+="</table>"
            texto+="</td>"
        texto+="</tr>"
    texto+="</table>"
    texto+="</body>"
    texto+="</html>"
    horario.write(texto)

# Representación de la solcuion con numeros enteros
def timetable(X,nombre_archivo):
    horario=open('./../timetabling/output/TXT/'+str(nombre_archivo)+'.txt','w')
    timetable=XaEnteros(X)
    horario.write(str(timetable))
    return timetable
    
# Representación de la solución para usuario
def dibujarHorario(timetable,input,nombre_archivo):
    horario=open('./../timetabling/output/HTML/'+str(nombre_archivo)+'.html','w')
    texto=""
    texto+="<html>"
    texto+="<head>"
    texto+="<style>"
    texto+="table, th, td {border: 1px solid black;}"
    texto+="</style>"
    texto+="</head>"
    texto+="<body>"
    texto+="<table style='width:90%;padding:10px'>"
    iterator=0

    texto+="<tr>"
    texto+="<th></th>"
    for s in range(0,len(input['salones'])):
            texto+="<th>"
            texto+=input['salones'][s]
            texto+="</th>"
    texto+="</tr>"
    for d in range(0,len(input['dias'])):
        for e in range(0,len(input['espacios'])):
            texto+="<tr>"
            texto+="<td>"
            texto+=input['dias'][d]
            texto+="<small>["
            texto+=input['espacios'][e]
            texto+="]</small>"
            texto+="</td>"
            for s in range(0,len(input['salones'])):
                texto+="<td>"
                if len(timetable[iterator])>0:
                    if s < len(timetable[iterator]):
                        try:
                            texto+=input['cursos'][timetable[iterator][s][0]]['nombre']
                            texto+="<small>("
                            texto+=input['profesores'][timetable[iterator][s][1]]['nombre']
                            texto+=")</small>"
                        except: pass    
                texto+="</td>"
            texto+="</tr>"
            iterator=iterator +1
    horario.write(texto)

# Dibujar matriz de 1 y 0s ( descontinuado )
def dibujarMatriz(X):
    string="["
    for d in range(0,len(X)):
        string+="["
        for e in range(0,len(X[d])):
            string+="["
            for s in range(0,len(X[d][e])):
                string+="["
                for c in range(0,len(X[d][e][s])):
                    string+="["
                    for p in range(0,len(X[d][e][s][c])):
                        if p==len(X[d][e][s][c])-1:
                            string+=str(X[d][e][s][c][p])
                        else:
                            string+=str(X[d][e][s][c][p])+", "
                    if c == range(0,len(X[d][e][s])-1):
                        string+="]"
                    else:
                        string+="],"
                if s == range(0,len(X[d][e])-1):
                    string+="]"
                else:
                    string+="],"
            if e == range(0,len(X[d])-1):
                string+="]"
            else:
                string+="],"
        if d == range(0,len(X)-1):
            string+="]"
        else:
            string+="],"
    string+="]"
    file=open('matriz.txt','w')
    file.write(string)
    return string