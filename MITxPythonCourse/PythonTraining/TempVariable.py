# swap variables - wrong method 
from tempfile import tempdir


a = 1
b = 2
a = b
b = a

# swap variables - correct method 
c = 1
d = 2
temp = c
c = d
d = temp

print ('c = ', c)
print ('d = ', d)