# str() = we can convert any type of data into string type using str()

v1 = 10
print('int---->str')
res = str(v1)
print(res)
print(type(res))
print('---------------')
v1 = 456.67
print('float---->str')
res = str(v1)
print(res)
print(type(res))
print('---------------')
v1 = 10
print('bool---->str')
res = str(v1)
print(res)
print(type(res))
print('---------------')
v1 = 10+4j
print('complex---->str')
res = str(v1)
print(res)
print(type(res))
print('---------------')