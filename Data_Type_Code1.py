# The type to which a particular Data belongs to.
# Data type is used on the variables to indicate the type of value that it contains
# In case of python there is no need to mention the datatype along with the variable
# In case of python based on the value provided the datatype is automatically selected
# In Python we have following datatypes :
# int, float, complex, str, bool, bytes, range, list, tuple, dict, set, none, etc

# Built-in function supported by python for identification of the data type is :
a = 10
print(type(a))

# Built-in function to find the unique id of the object
a = 10
print(id(a))
print("-------")

#--------------------------------------------------
#Integer Data Type : Is used to represent the integeral values
a1 = 100
print(a1)
print(type(a1))
print("-------")

a1 = 99
print(a1)
print(type(a1))
print("-------")

a1 = 98
print(a1)
print(type(a1))
print("-------")

# The value representational formats
# 1. Decimal Format
# 2. Binary Format
# 3. Octal Format
# 4. Hexadecimal Format
#-----------------------------

a1 = 101
print(a1)
print(type(a1))
print("-------")

a1 = 0B1010
print(a1)
print(type(a1))
print("-------")

a1 = 0O1010
print(a1)
print(type(a1))
print("-------")

a1 = 0x0afd
print(a1)
print(type(a1))
print("-------")