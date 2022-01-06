import random

def flipCoin():
    return random.randint(0,1)

# array is vector one-dimentional that by rotated
# to right if n is positive or left if is negative
def rotateArray(array,n):
    return array[-n:]+array[:-n] if n>0  else array[abs(n):]+array[:abs(n)]

# rotate just in one to left if n is positive
# or right if negative  
def rotateArrayByOne(array):
    return rotateArray(array,1)

def rotate(array, n):
    i=0
    while(i<n):
        array=rotateArrayByOne(array)
        i=i+1
    return array

# operador para colision inefectiva contra la pared
# y colision inefectiva intermolecular
def randomRotate(vector,parametros):
    n=random.randint(0,len(vector))
    return rotate(vector,n)

def splitInGroups( array, parametros ):
    return [ array[i:i+parametros['nsig']] for i in range(0, len(array), parametros['nsig'] ) ]

# operador para sintesis
def halfExchange( array1, array2, parametros ):
    return array2[:int(len(array1)/2)]+array1[int(len(array1)/2):]

# operador para descomposicion
def halfOddEven(array, parametros):
    array1=[]
    array2=[]
    grouped=splitInGroups(array,parametros )
    for i in range(0,len(grouped)):
        if (i +1) % 2 == 0 :
            array1= array1+grouped[i]
            randombit=[0 for x in range(0,parametros['nsig'])]
            randombit[random.randint(0,parametros['nsig']-1)]=1
            array2 = array2 + randombit
        else:
            array2 = array2 + grouped[i]
            randombit=[0 for x in range(0,parametros['nsig'])]
            randombit[random.randint(0,parametros['nsig']-1)]=1
            array1 = array1 +randombit
    return [array1, array2]


# print(rotate([1,2,3,4,5,6],5))
# print(randomRotate([1,2,3,4,5,6]))
# print(exchangePosition([1,2,3,4,5], [6,7,8,9,10],2))

# soluciones=halfOddEven([1,2,3,4,5,6,7,8,9,10],2)
# print(soluciones[0])
# print(soluciones[1])