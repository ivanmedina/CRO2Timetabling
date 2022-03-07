import json
import os

from timetabling.lib.funciones import Intensidades, IntensidadesCursos

def leerInput(filename):
    with open(filename) as file:
        # print(file.read())
        input = json.load(file)
        return input

def generarInputPrueba(nDias,nEspacios,nSalones,nCursos,horas_cursos,nProfesores,maxCP, maxEC,nombre_archivo):
    dias=[ 'Dia %s' % (str(d)) for d in range(0,nDias) ]
    espacios=[ 'Hora %s' % (str(h)) for h in range(0,nEspacios) ]
    salones=[ 'Salon %s' % (str(s)) for s in range(0,nSalones) ]
    cursos=[ { "nombre":'Curso %s' % (str(c)), "horas":horas_cursos } for c in range(0,nCursos) ]
    #creacion de profesor
    disponibilidad=[ [1 for j in range(0,nEspacios) ] for i in range(0,nDias)]
    cursos_profesor=[ 1 for i in range(0,nCursos)]
    profesores=[ { "nombre":'Profesor %s' % (str(p)), "disponible":disponibilidad, "cursos":cursos_profesor } for p in range(0,nProfesores) ]
    I,F=Intensidades(cursos)
    horario={"dias":dias, "espacios":espacios,"salones":salones,"cursos":cursos,"profesores":profesores,"maxCP":maxCP,"maxEC":maxEC , "I": I, "F": F, "J": IntensidadesCursos(I, cursos)}
    horario=json.dumps(horario)
    file=open("../timetabling/input/"+str(nombre_archivo)+".json",'w')
    filename=file.name
    file.write(horario)
    file.close()
    return filename

def generarInstancias(filename):
    instancias=[]
    files=[]
    with open(filename) as file:
        instancias=[l.split('\t') for l in file.read().split('\n')]
    for i in instancias:
        files.append(generarInputPrueba(int(i[1]),int(i[2]),int(i[3]),int(i[4]),int(i[5]),int(i[6]),int(i[7]),int(i[8]),"instancia-"+str(i[0])))
    return files