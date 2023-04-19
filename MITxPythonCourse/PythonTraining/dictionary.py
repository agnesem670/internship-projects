# # keys must be unique!
# # valus can be unmutable or mutable, keys have to unmutable (int, float, string, tuple, bool)
# # no order for keys and values!
# my_dict = {}
# grades = {'Ana':'B', 'John':'A+', 'Denise':'A', 'Katy':'A'}
# print (grades['John'])
# grades['Sylvan'] = 'A'
# 'John' in grades # Test, boolean
# 'A' in grades.values() # test for values, boolean
# del(grades['Ana'])
# print (grades)
# grades.keys()
# grades.values()

# d.get(key,default) , hand.get('a',0) - when we are not sure, is a key in dictionary, and we want to avoid KeyError
# dict.copy()


# def how_many(aDict):
#     '''
#     aDict: A dictionary, where all the values are lists.

#     returns: int, how many individual values are in the dictionary.
#     '''
#     result = 0
#     for value in aDict.values():
#         # Since all the values of aDict are lists, aDict.values() will 
#         #  be a list of lists
#         result += len(value)
#     return result

def how_many(aDict):
    '''
    Another way to solve the problem.

    aDict: A dictionary, where all the values are lists.

    returns: int, how many individual values are in the dictionary.
    '''
    count = 0
    result = 0
    
    for key in aDict.keys():
        values = 0
        for value in aDict.values():
            values += len(aDict[values])
            if values >= count:
               count = values
               result = key
    return result

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
print (how_many(animals))


def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    result = None
    biggestValue = 0
    for key in aDict.keys():
        if len(aDict[key]) >= biggestValue:
            result = key
            biggestValue = len(aDict[key])
    return result

# a method to write results in dictionary and use them in next computations
def fib_efficient(n, d):
    global numFibCalls
    numFibCalls += 1
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = ans
        return ans
d = {1:1, 2:2}
print(fib_efficient(fibArg, d))
print('function calls', numFibCalls)