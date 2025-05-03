#DATA TYPE CONVERSION (TYPE CASTING)

#In order to convert the data from any other format to binary format we can use the bin() function
a = 10
print(bin(a))  # Binary representation of the number
print("-------")

a = 0o11
print(bin(a))  # Binary representation of the number
print("-------")

a = 0xafd
print(bin(a))  # Binary representation of the number
print("-------")
print("===================================")

#In order to convert the data from any other format to octal format we can use the bin() function
a = 10
print(oct(a)) 
print("-------")

a = 0B11
print(oct(a)) 
print("-------")

a = 0xafd
print(oct(a))
print("-------")
print("===================================")

#In order to convert the data from any other format to hexadecimal format we can use the bin() function
a = 10
print(hex(a)) 
print("-------")

a = 0o11
print(hex(a))  
print("-------")

a = 0B11
print(hex(a)) 
print("-------")

a = 0xafd
print(hex(a))
print("-------")
