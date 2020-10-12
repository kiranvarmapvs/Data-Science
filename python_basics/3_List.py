
#List
#Creating a list
# L = [1,2,3]
# print(L)
#
# user_age = [21,22,23,24,25]
# print(user_age)
#
# nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
# 32, 33, 34, 35, 36, 37, 38, 39, 40]
# print("printing long list:", nums)
#
# squares = [1,4,9,16,25]
# print(squares)

#list with different data types
# L1 = [10,20.5,10j,"Fruits", 'Flowers']
# print(L1)
#
# L2 = [1,2.718,'python',[5,6,7,8]]
# print('list with different data types', L2)

#indexing and slicing
# L3 = [1,2,3,4,5,'hello']
# print('List with Different Data Types:',L3)
# print('To print the 3rd element in the list:', L3[2])
# print('Last element in the list:',L3[-1])
#
# L4 = L3[1:5] #assigning the list items L3(from index 1 to 4) t0 new list L4
# print('New list elements', L4)

# L5 = ['python',70,2.25,'kiran', 80.4]
# tiny_list = [123, 'kiran']
# print(L5)
# print(L5[0])
# print(L5[1:3])
# print(L5[2:])
# print(tiny_list*2)
# print(L5+tiny_list)

# squares = [1,4,9,16,25,36,49]
# print(squares)
# print(squares[0])
# print(squares[-1])
# print(squares[-3 :])
# print(squares[:])

# fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(fruits[-4: -1])

#Modify or updating the list elements - Lists are mutable type, it is possible to change the content
L5 = [10,20,30,40,50,'python']
print('The original List is:', L5)
L5[2] = 80
print("Updated element in the list:", L5)
L5[1] = 'Data Science'
L5[5] = 100
print("Updated element in the list:", L5)

# Append a new item to the list
L5.append('How are you')
print('New appended value in the list:', L5) # Append the value at the last in the list
L5.insert(3,'Machine Learning') # Insert the value at the index specified
print("New inserted value in the list:", L5)
L6 = [200, 300, 400]
L5.extend(L6)
print("The extended list:",L5)
L5.reverse()
print("Reverse of the list:", L5)
L1 = len(L5)
print("The length of the list:", L1)
#Deleting elememts -POP(), remove(), del()
#pop modifies the list and returns the element that was removed. If you don’t provide an index, it deletes and returns the last element.
print("The List elements", L5)
P1 = L5.pop()
print("POP value is", P1)

P2 = L5.pop(1)
print("POP Index:", P2)
print("List after pop:", L5)

#Delete
del L5[2]
print("List after Deleted", L5)

#Remove
L5.remove('Data Science')
print('list after removal:', L5)

D1 = [10,20,30,40]
print(D1)
del D1

S1 = [20,10,6,50,43,99,2,42,51]
S1.sort()
print("Sorting order:", S1)
S2 = ['d','c','e','a']
S2.sort()
print("Alphabet Sorting:", S2)


#Nested List - Creating list containing other list
X1= ['a','b','c']
x2 = [1,2,3]
x3 = [X1, x2]
print("New list from other list:", x3)
print("Index in new list:",x3[0])
print("Index in new list:",x3[0][1])
print("Index in new list:",x3[1][1])

N = [3,41,12,9,74,15]
print("Len of N:", len(N))
print("Max of N:", max(N))
print("Min of N:", min(N))
print("Sum of N:", sum(N))
print("Avg of N:", sum(N)/len(N))
