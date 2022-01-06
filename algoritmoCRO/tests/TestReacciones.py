import unittest
import os
import sys
PROJECT_PATH = os.getcwd()
SOURCE_PATH = os.path.join(
    PROJECT_PATH,"../"
)
sys.path.append(SOURCE_PATH)

from lib.reacciones import *
from lib.molecula import *

class TestReacciones( unittest.TestCase ):
    
    initiallKE = 0.5
    buffer = 0.5
    KELossRate = 0.5
    pobjetivo = {}
    pneighbor = {}
    pobSize = 2

    #sintesis
    def neighbors( self, w1, w2, pneighbor ):
        return  w1[:int(len(w1)/2):-1] + w2[ int(len(w2)/2)::-1 ]

    #descomposicion
    def neighbord( self, w1, pneighbor ):
        return  [   
                w1[:int(len(w1)/2):-1] + w1[ int(len(w1)/2)::-1 ],
                w1[:int(len(w1)/2):-1] + w1[ int(len(w1)/2)::-1 ]
            ] 

    # ineficiente intermolecular y contra la pared
    def neighbor( self, w1, pneighbor ):
        return w1[::-1]

    def fobjetivo( self, pobjetivo ):
        return 1
    wd1 = [ 1, 0, 0, 0, 0, 0, 1, 0]
    wd2 = [ 1, 0, 0, 0, 0, 0, 1, 0]
    M1 = Molecula( 0, wd1 , 0.5, 1, 0, wd1, 1, 0 )
    M2 = Molecula( 1, wd1, 0.5,  1, 0, wd2, 1, 0  )

    def test_colision_inef_pared(self):
        molecula_nueva = colision_inef_pared( self.M1, self.buffer, self.neighbor, self.pneighbor, self.fobjetivo, self.pobjetivo, self.KELossRate )
        self.assertIsInstance( molecula_nueva, list )
        self.assertIsInstance( molecula_nueva[0], Molecula  )

    def test_colision_inef_intermol(self):
        moleculas_nuevas =colision_inef_intermol( self.M1, self.M2, self.neighbor, self.pneighbor, self.fobjetivo, self.pobjetivo )
        self.assertIsInstance(moleculas_nuevas[0], Molecula)
        self.assertIsInstance(moleculas_nuevas[1], Molecula)

    def test_sintesis(self):
        molecula_nueva = sintesis( self.M1, self.M2, self.neighbors, self.pneighbor, self.fobjetivo, self.pobjetivo, self.pobSize, self.initiallKE )
        self.assertIsInstance(molecula_nueva[0], Molecula)

    def test_descomposicion(self):
        moleculas_nuevas = descomposicion( self.M1, self.buffer, self.neighbord, self.neighbord, self.fobjetivo, self.pobjetivo, self.pobSize, self.initiallKE )
        self.assertIsInstance( moleculas_nuevas[0], Molecula )
        self.assertIsInstance( moleculas_nuevas[1], Molecula )

if __name__ == '__main__':
    unittest.main()