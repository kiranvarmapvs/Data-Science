# A tuple is an immutable list of values.
# Tuples are one of Python's simplest and most common collection types, and
# can be created with the comma operator (value = 1, 2, 3).

# The main difference between lists and tuples is- Lists are enclosed in brackets ( [ ] ) and
# their elements and size can be changed, while tuples are enclosed in parentheses ( ( ) )
# and cannot be updated. Tuples can be thought of as read-only Lists.

#Creating an empty tuple
# tup =("")
# print("Empty Tuple:", tup)
# print("type of an empty tuple:",type(tup))

# To create a tuple single element
# T = ('a',)
# print("Single item of a tuple:", type(T))
# To create a tuple with a single element, you have to include a final comma:

# For example, if we have a rectangle that should always be a certain size,
# we can ensure that its size doesn’t change by putting the dimensions into a tuple:

# dimensions = (200, 50)
# print(dimensions)
# print(type(dimensions))
#
# monthsOfYear = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
# print(monthsOfYear)
# print(type(monthsOfYear))

#Another way of creating Tuple, using built in function tuple()
# t = tuple("9,10")
# print(t)
print('----------------------------------------------------')
#Accessing the tuple elements

tup = ('Apple', 'Cherry', 'Grapes', 'Guava')
print(tup[-1])

# dimensions = (200, 50)
#
# print("First dimension:-", dimensions[0])
# print("Second dimension:-", dimensions[1])
#
# monthsOfYear = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
# print(monthsOfYear[5])
# print(monthsOfYear[8])
# print(monthsOfYear[-2])
#
# #Nested tuples
# T1 = (123456,54321,'hello', 'python')
# print(T1[1])
# T2 = T1,(1,2,3,4,5)
# print("Nested Tuples:",T2)
print('--------------------------------------------------------------------')

#Range of indexes
# You can specify a range of indexes by specifying where to start and where to end the range.

# When specifying a range, the return value will be a new tuple with the specified items.

# tp = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(tp[2:5])
# print(tp[-4:-1])
#
# X = (1,2,3)
# print(X[0])
# print(X[1])
# print(X[2])
# #print(X[3])
# print(X[-1])
# print(X[-2])
# print(X[-3])
# #print(X[-4])
# print(X[:-1])
# print(X[-1:])

#print(X[1:3])
# print(X[:])


#Tuples are Immutable
# One of the main differences between lists and tuples in Python is that tuples are immutable, that is, one cannot
# add or modify items once the tuple is initialized

# TP = (1,4,9)
# TP[1] = 6
# print(TP)

#Tuple built in functions
tuple1 = ('a', 'b', 'c', 'd', 'e')
print(len(tuple1))



tp = ("apple", "banana", "cherry")
print("The Length of the tuple:-",len(tp))
# Max of a tuple: he function max returns item from the tuple with the max value

print("Maximum value in the tuple:-",max(tuple1))


tuple2 = ('1','2','3')

print("Maximum value in the tuple:-",max(tuple2))

# Min of a tuple - The function min returns the item from the tuple with the min value
print("Minimum value in the tuple:-",min(tuple1))

print("Minimum value in the tuple:-",min(tuple2))
# Count
animals = (10, 20, 30, 'tiger', 'lion', 'wolf', 'lion')
print("The count of lion:-",animals.count('lion'))

# Convert a list into tuple
# The built-in function tuple converts a list into a tuple.

list = [1,2,3,4,5]
print("Converting List to tuple:-", tuple(list))
# Tuple concatenation: Use + to concatenate two tuples
print("Concatenation of tuples:-", tuple1 + tuple2)
colors = "red", "green", "blue","yellow"
print(tuple(reversed(colors)))

rev = tuple(reversed(colors))
print(rev)

print("----------------------------------------------------------------------------")
#Remove Items
# Note: You cannot remove items in a tuple.
# Tuples are unchangeable, so you cannot remove items from it, but you can delete the tuple completely:
# The del keyword can delete the tuple completely:

tp = ("apple", "banana", "cherry")
#del tp
#print(tp)

print('-----------------------------------------------------------------------------------')
#Exercise



tuple = ( 'abcd', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')
print (tuple) # Prints complete tuple
print (tuple[0]) # Prints first element of the tuple
print (tuple[1:3]) # Prints elements starting from 2nd till 3rd
print (tuple[2:]) # Prints elements starting from 3rd element
print (tinytuple * 2) # Prints tuple two times
print (tuple + tinytuple) # Prints concatenated tuple

print ("=======1. Creating Tuples ==========")
t1 =(1,2,3,4)
t2 =('x','y','z')
print ("Adding Tuples:")
print (t1+t2)
print ("Replicating Tuple: ")
print (t1*3)
print ("Replicating Tuple: ")
print (t2*4)
print ("Tuple slicing : ")
print (t1[0:2])
print(t1.count(1))
print(len(t1))