# x = 5

# def f(y):
#     x = 1
#     x += x
#     print (x)
# f(x)
# print (x)

# def g(y):
#     print (x)         #inside the function, can ACESS the variable defined outside
#     print (x+1)
# g(x)
# print (x)

# def h(y):
#     x += 1          #inside the function CANNOT modify the variable defined outside
# h(x)
# print (x)


# def k(x):
#     def l():
#         x = "abc" # here is no return, variable x does't change
#     x = x + 1
#     print ("in k(x): x = ", x)
#     l()
#     return x
# x = 3
# z = k(x)

# def fourthPower(x):
#     '''
#     x: int or float.
#     '''
#     x = x*x
#     return x
# x = 2
# print (fourthPower(fourthPower(fourthPower(x))))

# my version - the greatest common divisor of a & b
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b % a == 0:
        return a
    else:
        result = 1
        for i in range (2, a):
            if b % i == 0 and a % i == 0 and i > result:
                result = i
                i += 1
        return result
print (gcdIter(6,12))


# MIT version - the greatest common divisor of a & b
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    testValue = min(a, b)

    # Keep looping until testValue divides both a & b evenly
    while a % testValue != 0 or b % testValue != 0:
        testValue -= 1

    return testValue
print (gcdIter(6,12))