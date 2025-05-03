# there are two important partitions in the complex data type.
# 1. Real part
# 2. Imaginary part
# example  : a + cj -----> 2 + 3j
# where 2 is real part and 3 is imaginary part.
# The variables a and c in the above syntax can contain either int or float point values.
# In The real part we use int values then we can specify them either by decimal, octal, binary or hexadecimal formats.
# But the imaginary part should contain decimal format only.
# From the latest version of python imaginary part can decimal/float formats.

a = 10 + 3j
print(type(a)) 
print('-------')

b = 20 + 4j
print(type(b))
print('-------')

c = a + b

# Built in functions for complex data type
print('==============================')
print('Real part of a = ', a.real)
print('Real part of b = ', b.real)
print('Real part of c = ', c.real)
print('----------------------------')
print('Imaginary part of a = ', a.imag)
print('Imaginary part of b = ', b.imag)
print('Imaginary part of c = ', c.imag)