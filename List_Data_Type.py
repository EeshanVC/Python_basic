# List data type: When ever we have to represent group of items as a 
#                 single entity where insertion order has to be maintained and also to 
#                 allow the duplicate data entry, then we must choose list data type.
# A list is also defined as the  ordered heterogeneous collection of elements. 
# 
# Key features of list data type:
# 1. List maintains insertion order.
# 2. List allows duplicate data entry.
# 3. List allows heterogeneous data entry.
# 4. List is growable in nature.
# 5. To represent the values in case of list we must use square brackets [].


lst1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(lst1)
print(type(lst1))
print("----------")
lst2 = [100, 50, 'sachin', 'dhoni', 's', True]
print(lst2)
print(type(lst2))
print("----------")
print(lst1[1])
print(lst1[2])
print(lst1[3])
print(lst1[4])
print("----------")
print(lst2[0])
print(lst2[1])
print(lst2[2])
print(lst2[3])
print(lst2[4])
print("----------")
lst1.append("rohith")
print(lst1)
lst1.remove(10)
print(lst1)
