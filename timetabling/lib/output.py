def dibujarTabla(X,input,nombre_archivo):
    print(input['dias'])
    horario=open('./output/'+str(nombre_archivo)+'.html','w')
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