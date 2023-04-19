from operator import eq


# class Coordinate (object):
#     def __init__(self, x, y):  # self is autmaticly completed by python
#         self.x = x
#         self.y = y
#     def getX(self):
#         # Getter method for a Coordinate object's x coordinate.
#         # Getter methods are better practice than just accessing an attribute directly
#         return self.x
#     def getY(self):
#         # Getter method for a Coordinate object's y coordinate
#         return self.y
#     def distance (self, other):
#         x_diff_sq = (self.x - other.x) **2
#         y_diff_sq = (self.y - other.y) **2
#         return (x_diff_sq + y_diff_sq) **0.5
#     def __str__ (self): # print representation diffrent than defult
#         return "<" + str(self.x) + "," + str(self.y) + ">" 
#     def __sub__ (self, other):
#         return Coordinate (self.x - other.x, self.y - other.y)
#     def __eq__(self, other): #-> bool
#         assert type (other) == type (self)
#         return self.getX() == other.getX() and self.getY() == other.getY()
#     def __repr__(self):
#         return 'Coordinate(' + str(self.getX()) + ',' + str(self.getY()) + ')'

# c1 = Coordinate(-3, -4)
# c2 = Coordinate(-3, -4)
# print (c1==c2)

# print(repr(c1))

# c = Coordinate (3,4)
# origin = Coordinate (0,0)

# print (c.x)
# print (origin.x)
# print (c.distance(origin)) # self is completed by python
# print (Coordinate.distance(c, origin))
# print (c)
# print (type(c))
# print (isinstance(c, Coordinate))

# foo = c - origin
# print (foo)

# # ---------------------------------------- 

# class Clock(object):
#     def __init__(self, time):
#         self.time = time
#     def print_time(self):
#         time = '6:30'
#         print (self.time)

# clock = Clock('5:30')
# clock.print_time() #---> 5:30

# #--------------------------------------------- 
# class Clock(object):
#     def __init__(self, time):
#         self.time = time
#     def print_time(self, time):
#         print(time)

# clock = Clock('5:30')
# clock.print_time('10:30') #---> 10:30

# # -----------------------------------
# class Clock(object):
#     def __init__(self, time):
#         self.time = time
#     def print_time(self):
#         print(self.time)

# boston_clock = Clock('5:30')
# paris_clock = boston_clock
# paris_clock.time = '10:30'
# boston_clock.print_time()  #----> 10:30
# paris_clock and boston_clock are the same object!!

# --------------------------------------
# class Weird(object):
#     def __init__(self, x, y): 
#         self.y = y
#         self.x = x
#     def getX(self):
#         return x    # X IS NOT DEFINED
#     def getY(self):
#         return y

# class Wild(object):
#     def __init__(self, x, y): 
#         self.y = y
#         self.x = x
#     def getX(self):
#         return self.x 
#     def getY(self):
#         return self.y

# X = 7
# Y = 8

# # w1 = Weird(X, Y) 
# # print(w1.getX()) # ----> error

# w2 = Wild(X, Y)
# print(w2.getX()) # ----> 7

# w3 = Wild(17, 18)
# print(w3.getX()) # ----> 17

# --------------------------------------

# class fraction(object):
#     def __init__(self, numer, denom):
#         self.numer = numer
#         self.denom = denom
#     def __str__(self):
#         return str(self.numer) + ' / ' + str(self.denom)
#     def getNumer(self):
#         return self.numer
#     def getDenom(self):
#         return self.denom
#     def __add__(self, other):
#         numerNew = other.getDenom() * self.getNumer() \
#                    + other.getNumer() * self.getDenom()
#         denomNew = other.getDenom() * self.getDenom()
#         return fraction(numerNew, denomNew)
#     def __sub__(self, other):
#         numerNew = other.getDenom() * self.getNumer() \
#                    - other.getNumer() * self.getDenom()
#         denomNew = other.getDenom() * self.getDenom()
#         return fraction(numerNew, denomNew)
#     def convert(self):
#         return self.getNumer() / self.getDenom()
      
# oneHalf = fraction(1, 2)
# twoThirds = fraction(2, 3)

# oneHalf.getNumer() #--> 1
# fraction.getDenom(twoThirds)  #-->3

# new = oneHalf + twoThirds
# print (new) #--> 7/6

# threeQuarters = fraction(3,4)
# print (threeQuarters)

# secondNew = twoThirds - threeQuarters
# print (secondNew)

# print (secondNew.convert())  #--> -0.0833333...

# ----------------------------------

class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
        Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
        Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        result = ''
        for e in self.vals:
            result = result + str(e) + ','
        return '{' + result[:-1] + '}'

    def intersect(self, other):
        """Assumes other is an intSet
           Returns a new intSet containing elements that appear in both sets."""
        # Initialize a new intSet    
        commonValueSet = intSet()
        # Go through the values in this set
        for val in self.vals:
            # Check if each value is a member of the other set    
            if other.member(val):
                commonValueSet.insert(val)
        return commonValueSet

    def __len__(self):
        """Returns the length of the set.
           This method is called by the `len` built-in function."""
        return len(self.vals)
    

setA = intSet()
setA.insert(-15)
setA.insert(-12)
setA.insert(17)
setB = intSet()
setB.insert(14)
setB.insert(-2)
setB.insert(17)

print (setA, setB)

print (setA.intersect(setB))


# s = intSet()
# print(s) #--> {}

# s.insert(3)
# s.insert(4)
# s.insert(3)
# print(s) #--> {3, 4}

# s.member(3) #--> True 
# s.member(5) #--> False
# s.insert(6)
# print(s)

# s.remove(3)
# print(s)
# s.remove(3) #--> ValueError, except "3 not found"

# ----------------------------
# inside class Time:
# The built-in function isinstance takes a value and a class object, and returns True if the value is an instance of the class. 

    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)
    
    def add_time(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)

#Here are examples that use the + operator with different types:

>>> start = Time(9, 45)
>>> duration = Time(1, 35)
>>> print start + duration  # !!
11:20:00
>>> print start + 1337
10:07:17


#-------------------------------
## inside class Time: To use this method, you have to invoke it on one object and pass the other as an argument:

    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()
# To use this method, you have to invoke it on one object and pass the other as an argument:
    end.is_after(start)

# ---------------
# When I write a new class, I almost always start by writing __init__, which makes it easier to instantiate objects, and __str__, which is useful for debugging.

# ------------------
# the special method __radd__, which stands for “right-side add.” This method is invoked when a Time object appears on the right side of the + operator. Here’s the definition:

# inside class Time:

    def __radd__(self, other):
        return self.__add__(other)

# And here’s how it’s used:

>>> print 1337 + start
10:07:17

# ----------------------
#Another way to access the attributes of an object is through the special attribute __dict__, which is a dictionary that maps attribute names (as strings) and values:

>>> p = Point(3, 4)
>>> print p.__dict__
{'y': 4, 'x': 3}

#For purposes of debugging, you might find it useful to keep this function handy:

def print_attributes(obj):
    for attr in obj.__dict__:
        print attr, getattr(obj, attr)

print_attributes traverses the items in the object’s dictionary and prints each attribute name and its corresponding value.

#The built-in function getattr takes an object and an attribute name (as a string) and returns the attribute’s value. 
