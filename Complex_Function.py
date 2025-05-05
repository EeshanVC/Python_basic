# Complex() = In order to convert data from any format to complex format

v1 = 10
print('int---->complex')
res = complex(v1)
print(res)
print(type(res))
print('---------------')
v1 = 456.67
print('float---->complex')
res = complex(v1)
print(res)
print(type(res))
print('---------------')
v1 = 10
print('bo9olean---->complex')
res = complex(v1)
print(res)
print(type(res))
print('---------------')
v1 = '10.678'
print('str---->complex')
res = complex(v1)
print(res)
print(type(res))
print('---------------')
v1 = 10
v2 = 30
print('int---->complex')
res = complex(v1, v2)  # 2 parameters indicate real part and imaginary part
print(res)
print(type(res))
print('---------------')
v1 = True
v2 = False
print('bool---->complex')
res = complex(v1, v2)  # 2 parameters indicate real part and imaginary part
print(res)
print(type(res))
print('---------------')
v1 = 10.546
v2 = 30.234
print('float---->complex')
res = complex(v1, v2)  # 2 parameters indicate real part and imaginary part
print(res)
print(type(res))
print('---------------')