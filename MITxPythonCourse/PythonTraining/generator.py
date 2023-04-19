from numpy import Infinity


def genPrimes():
# def prime (): # test 
    # prime = [] # test
    for x in range (1, 100, 1):
        count = 0
        for p in range (1, x+1, 1):
            if (x % p) == 0:
                count += 1
        if count <=2:
            # prime += [x] # test
            next = x
            yield next
    # return prime # test
prime = genPrimes()
print (prime)
print (prime.__next__())
# print (prime()) # test
