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
def randomRotate(vector):
    n=random.randint(0,len(vector))
    return rotate(vector,n)
    

# operador para colision inefectiva intermolecular
def paireExchange():
    pass

# operador para sintesis
def exchangePosition():
    pass

# operador para descomposicion
def halfRandom():
    pass

# print(rotate([1,2,3,4,5,6],5))
print(randomRotate([1,2,3,4,5,6]))
