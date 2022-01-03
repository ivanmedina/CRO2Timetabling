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
def randomRotate(vector):
    n=random.randint(0,len(vector))
    return rotate(vector,n)

def splitInGroups(array,x):
    return [array[i:i+x] for i in range(0, len(array), x)]

# operador para sintesis
def halfExchange(array1, array2, n):
    return array2[:n]+array1[n:]

# operador para descomposicion
def halfOddEven(array, groups):
    array1=[]
    array2=[]
    grouped=splitInGroups(array,groups)
    for i in range(0,len(grouped)):
        if (i +1) % 2 == 0 :
            array1.append(grouped[i])
            randombit=[0 for x in range(0,groups)]
            randombit[random.randint(0,groups-1)]=1
            array2.append(randombit)
        else:
            array2.append(grouped[i])
            randombit=[0 for x in range(0,groups)]
            randombit[random.randint(0,groups-1)]=1
            array1.append(randombit)            

    return [array1, array2]

# print(rotate([1,2,3,4,5,6],5))
# print(randomRotate([1,2,3,4,5,6]))
# print(exchangePosition([1,2,3,4,5], [6,7,8,9,10],2))

# soluciones=halfOddEven([1,2,3,4,5,6,7,8,9,10],2)
# print(soluciones[0])
# print(soluciones[1])