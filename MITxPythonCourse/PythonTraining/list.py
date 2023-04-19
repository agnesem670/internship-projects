a_list = []
b_list = [2, 'a', 4, True]

L = [2, 1, 3]
len(L)
L[2]
L[2]+1

i=1
L[i+1] # index could be an expresion

# lists are mutable
L[1]=5  
print (L) 

L.append(8)
print (L)

copied_list = original_list[:]

# iterating over the list; sum of elements of the list
total = 0
for i in L:
    total += i
print (total)

# a list in a list
x = [1, 2, [3, 'John', 4], 'Hi'] 
x[2][2]
x[0:1] # cutting the list

# adding list to list
L1 = [1, 2, 3]
L2 = [4, 5, 6]
L3 = L1 + L2
print (L3)                    

L1.extend([5, 6])
print(L1)

del(L1[1])
print(L1)

L1.pop() # del the las element from the list, returns removed element
L1.remove(3) # retur specyfic element, but only the first one

# list of strings
s = 'abc' 
print (list(s)) # ['a', 'b', 'c']
S1 = ['a', 'b', 'c']
'_'.join(S1)
''.join(S1)

W1 = [8, 7, 0, 2]
sorted(W1) # sorting elements without changing the list
W1.sort() # mutates the list
W1.sorted() # does not mutate the list, must be assign to variable
W1.reverse() # mutates the list
W1.insert(0, 100) # 0 - index, 100 - value

# method to creat a new list as a COPY (not an alias) of previus one
cool = ['blue', 'grey', 'green']
chill = cool[:]

# iteration and mutations over lists
# every itaration can mutate the list and change values indexes. 
# In result some valus could be missed in iteration.
# Solution is to iterate a copy of list

def remove_dups (L1, L2):
    L1_copy = L1 [:]
    for e in L1_copy:
        if e in L2:
            L1.remove(e)

# functions can mutate list by using iteration and applaing f.e: type
def applyToEach (L, f):
    for i in range (len(L)):
        L[i] = f(L[i])   # adds for example int, abs itd
def plusOne(a):
    return a + 1
applyToEach(L1, plusOne)