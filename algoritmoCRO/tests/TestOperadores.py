import unittest
import os
import sys
PROJECT_PATH = os.getcwd()
SOURCE_PATH = os.path.join(
    PROJECT_PATH,"../"
)
sys.path.append(SOURCE_PATH)
from lib.operadores import *

class TestOperadores( unittest.TestCase ):
    
    def test_flipCoin(self):
        self.assertIn( flipCoin(), [ 0 , 1 ] )

    def test_rotate(self):
        array = [ 0, 0, 0, 1, 0, 0, 0, 1 ]
        n = 2
        self.assertEqual( rotateArray( array, n ), [ 0, 1, 0, 0, 0, 1, 0, 0 ] )
    
    def test_rorotateArrayByOne(self):
        array = [ 0, 0, 0, 1, 0, 0, 0, 1 ]
        self.assertEqual( rotateArrayByOne( array ), [ 1, 0, 0, 0, 1, 0, 0, 0 ] )

    def test_rotate(self):
        array = [ 0, 0, 0, 1, 0, 0, 0, 1 ]
        n = 2
        self.assertEqual( rotate( array, n ), [ 0, 1, 0, 0, 0, 1, 0, 0 ] )

    def test_randomRotate(self):
        array = [ 0, 0, 0, 1, 0, 0, 0, 1 ]
        n = 2
        new_array = randomRotate( array, { 'nrr' : n } )
        self.assertIsInstance( new_array, list )
     
    def test_splitInGroups(self):
        array = [ 1, 0, 0, 1 ]
        n = 2
        self.assertEqual( splitInGroups( array, { 'nsig' : n } ) , [ [ 1, 0], [ 0, 1 ] ] )

    def test_halfExchange(self):
        array1 = [ 1, 0, 0, 1 ]
        array2 = [ 0, 1, 1, 0 ]
        n = 2
        self.assertEqual( halfExchange( array1, array2, { 'nhe' : n}  ), [  0, 1, 0, 1 ] )

    def test_halfOddEven(self):
        array = [ 1, 0, 1, 0 ]
        n = 2
        new_array = halfOddEven( array, { 'nsig' : n } )
        # print( new_array )
        self.assertEqual( new_array[0][2], 1 )
        self.assertEqual( new_array[1][0], 1 )



if __name__ == '__main__':
    unittest.main()