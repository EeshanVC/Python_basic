# tuple datatype: Tuple datatype is same as the list datatype except that it is immutable.
#Incase tuple datatype we cannot change the value once added
#A tuple datatype is represented using normal function parenthesis

t1 = (10,20,30,40,50,60)
print(t1)
print(type(t1))
print("----------")
print(t1[0])
print(t1[1])
print(t1[2])
print(t1[3])
print(t1[4])
print("----------")
#t1[0] =222
# print(t1[0])
t1.append(100)
print(t1)