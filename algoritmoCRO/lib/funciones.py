import random
from dataclasses import dataclass
from typing import Callable


def neighbor(function, w):
    return function(w)


def inicializacion(funcion, parametros):
    return funcion(parametros)


def esIntermolecular(colision):
    return random.uniform(0, 1) <= colision


def selMolecula(poblacion):
    return random.choice(poblacion)


def selMoleculas(poblacion):
    n1 = n2 = enough = 0
    m1 = m2 = None
    while n1 == n2 and len(poblacion) > 1 and enough < 1:
        m1 = random.choice(poblacion)
        m2 = random.choice(poblacion)
        if m1.n == m2.n and len(poblacion) < 3:
            break
        n1 = m1.n
        n2 = m2.n
        enough = 1
    return m1, m2, enough


def esDescomposicion(m, alfa):
    return m.hits - m.minimumhits > alfa


def esSintesis(m1, m2, beta):
    return m1.KE <= beta and m2.KE < beta


def criterio(pobSize, iteracion, criterios):
    return (
        pobSize < criterios['a']
        and pobSize > criterios['b']
        and iteracion < criterios['c']
    )


@dataclass
class CROStrategy:
    esIntermolecular: Callable = esIntermolecular
    selMolecula: Callable = selMolecula
    selMoleculas: Callable = selMoleculas
    esDescomposicion: Callable = esDescomposicion
    esSintesis: Callable = esSintesis
    criterio: Callable = criterio
