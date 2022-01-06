import unittest
import os
import sys
PROJECT_PATH = os.getcwd()
SOURCE_PATH = os.path.join(
    PROJECT_PATH,"../"
)
sys.path.append(SOURCE_PATH)

from lib.cro import CRO
from lib.reacciones import *
from lib.molecula import *

class TestCRO( unittest.TestCase ):
    
    initialKE = 1000
    buffer = 0
    KELossRate = 500
    pobjetivo = {  }
    pneighbor = { 'nsig':2 }
    pobSize = 2
    colision =0.5
    pinicio = {}
    alfa = 300
    beta = 50


    def fobjetivo( self, pobjetivo ):
        return random.uniform(0,1)

    def finicio( self, pinicio ):
        w1=[ 1, 0, 0, 0, 0, 0, 1, 0 ]
        w2=[ 1, 0, 0, 0, 0, 0, 1, 0 ]
        wds = [ [ random.randint(0,1) for i in range(10) ] for x in range(100) ]
        return [ Molecula( x, wds[x], 0.5, 0.5, 0, wds[x], 1, 0 ) for x in range(len(wds)) ]
        

    def ffitness( self ):
        pass

    def test_CRO( self ):
        CRO( self.initialKE, self.KELossRate, self.colision, self.finicio, self.pinicio, self.fobjetivo, self.pobjetivo, self.pneighbor, self.alfa, self.beta )


if __name__ == '__main__':
    unittest.main()