#Slicing in strings
# Slicing refers to dividing a string into smaller parts or extracting a substring from a string.
# We make use of [] operator to slice the string.
# Using the slicing operator we can extract a substring from the string.
# In python the memory will always start from 0th index.
# the index i  python can be either +ve or -ve.
# +ve index means forward direction i,e left to right direction.
# -ve index means backward direction i,e right to left direction.


str1 = 'Ramayana'
print(str1[1])
print(str1[2])
print(str1[3])
print(str1[4])
print(str1[5])
print(str1[6])
print(str1[7])

print('-------------')

print(str1[2:90]) # print the string from 2nd index to 90th index
#postion to max avsilable position if it is less specified end position.
print(str1[2:]) 
print(str1[:])
print('-------------')

# Multiply the string to print it for specified number of times.
print(str1*4)
print('-------------')

#To find the number of character in the string
print(len(str1))