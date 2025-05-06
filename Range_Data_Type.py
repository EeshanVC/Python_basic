
# range datatype : range basically represents the sequence of numbers
#In case of range datatype element present in the particular range are not
#modifiable, i.e it is immutable

r1 = range(10)
for i in r1:
    print(i)
print(' ----- ')
r2 = range(2,8)
for i in r2:
    print(i)
print(' ----- ')
r3 = range(1,20,2)
for i in r3:
    print(i)
print(' ----- ')
l1 = list(range(10))
print(l1)   
for i in l1:
    print(i)
     