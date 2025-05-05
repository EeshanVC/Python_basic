# float() : we can use float() to convert the data from any other datatype to float data 
# incase of float datatype we can convert anytype of data into float except for complex 
# if we are using string then the string must contain a numeric value



print('Complex---->Float')
v1 = 10+5j
res1 = float(v1)
print(res1)
print(type(res1))
print('-----------')
print('int---->Float')
v1 = 10
res1 = float(v1)
print(res1)
print(type(res1))
print('-----------')
print('boolean---->Float')
v1 = True
res1 = float(v1)
print(res1)
print(type(res1))
print('-----------')
print('float---->Float')
v1 = 10.23
res1 = float(v1)
print(res1)
print(type(res1))
print('-----------')
print('string---->Float')
v1 = 'Python'   # string run agbek andre number form alle irbeku yak andre letter idre run agalla ascii values or numerical idre run aguthe
# v1 = '23.02'
res1 = float(v1)
print(res1)
print(type(res1))
print('-----------')