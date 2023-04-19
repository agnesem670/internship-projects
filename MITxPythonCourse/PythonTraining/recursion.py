# # multiplication a*b

# def mult(a,b):
#     if b == 1:
#         return a
#     else:
#         return a + mult(a, b-1)

# print (mult (2,3))

# factorial a!

# def fac(a):
#     """ 
#     a: int or float
#     returns a!
#     """
#     if a == 1:
#         return a
#     else:
#         return a + fac(a-1)

# print (fac (5))

# # base ^ exp
# def recurPower(base, exp):
#     '''
#     base: int or float.
#     exp: int >= 0
 
#     returns: int or float, base^exp
#     '''
#     if exp <= 0:
#         return 1
#     else:
#         return base * recurPower(base, exp-1)


def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b == 0:
        return a
    else:
        return gcdRecur(b, a%b)