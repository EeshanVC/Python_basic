# bool() = we can convert any type of data into boolean type of data using bool()

# if in case the value is 0 then it will return false else true
v1 = 10
print('int---->boolean')
res = bool(v1)
print(res)
print(type(res))
print('---------------')
# if in case the value is 0 then it will return false else true
v1 = 456.67
print('float---->boolean')
res = bool(v1)
print(res)
print(type(res))
print('---------------')
# if in case the value is 0 for both real and imaginary part then it will return false else true
v1 = 0+0j
print('complex---->boolean')
res = bool(v1)
print(res)
print(type(res))
print('---------------')
v1 = 3+0j
print('complex---->boolean')
res = bool(v1)
print(res)
print(type(res))
print('---------------')
v1 = 0+3j
print('complex---->boolean')
res = bool(v1) 
print(res)
print(type(res))
print('---------------')

v1 = 2+5j
print('complex---->boolean')
res = bool(v1)  
print(res)
print(type(res))
print('---------------')
# if the string is empty then it will return false else returns true
v1 = 'India'
print('str---->boolean')
res = bool(v1)  
print(res)
print(type(res))
print('---------------')
v1 = ''
print('str---->boolean')
res = bool(v1)  
print(res)
print(type(res))
print('---------------')