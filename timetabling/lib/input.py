import json

def leerInput(filename):
    with open(filename) as file:
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
    horario={"dias":dias, "espacios":espacios,"salones":salones,"cursos":cursos,"profesores":profesores,"maxCP":maxCP,"maxEC":maxEC}
    horario=json.dumps(horario)
    file=open("./input/"+str(nombre_archivo)+".json",'w')
    file.write(horario)