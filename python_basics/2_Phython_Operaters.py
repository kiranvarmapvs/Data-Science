# 7 Operators
# Python has 7 types of Operators as stated below:
# 	Arithmetic Operator
# 	Comparison operators
# 	Logical operators
# 	Bitwise operators
# 	Assignment Operator
# 	Identity operators
# 	Membership operators

#Arthimetic operator
# x = 28
# y = 10
# z = x+y
# z1 = x-y
# z2 = x*y
# z3 = x**y
# z4 = x/y
# z5 = x%y
# z6 = x//y
# print("The sum of the numbers:", z)
# print("Subtraction:", z1)
# print("Multiplication:",z2)
# print("exponent:",z3 )
# print("Divison:", z4)
# print("mod:", z5)
#print("Floor Divison:",z6)

#Comparsion operators
# Operators	Definition
# Greater than (>)	True if left operand is greater than the right
# Less than (<)	True if left operand is less than the right
# Equal to (==)	True if both operands are equal
# Not equal to (!=)	True if operands are not equal
# Greater than or equal to (>=)	True if left operand is greater than or equal to the right
# Less than or equal to (<=)	True if left operand is less than or equal to the right

# a1 = 10
# b1 = 15
# print("Greater:", a1>b1)
# print("Less than:", a1<b1)
# print("Equal to:",a1==b1)
# print("Not Equal to :", a1!=b1)
# print("greater than or equal to:", a1>=b1)
# print("lesser than or equal to:", a1<=b1)

#Logical operators
# Operators	Definitions
# and	True if both the operands are true
# or	True if either of the operands is true
# not	True if operand is false
# x = 10
# print("logical and",x>10 and x>5)
# print("logical or",x>10 or x>5)
# print("logical not",not (x>10 and x>5))
# print("logical not",not (x>10 or x>5))

#Bitwise Operators
# Operators	Definitions	Example
# &	Bitwise AND	x& y = 0 (0000 0000)
# |	Bitwise OR	x | y = 14 (0000 1110)
# 	Bitwise NOT	x = -11 (1111 0101)
# ^	Bitwise XOR	x ^ y = 14 (0000 1110)
# >> 	Bitwise right shift	x>> 2 = 2 (0000 0010)
# << 	Bitwise left shift	x<< 2 = 40 (0010 1000)

# x = 10 # 10 in binary format is 1010
# y = 12 # 12 in binary format is 1100
# print("Bitwise Operator and:",x&y)
# print("Bitwise Operator or:",x|y)
# print("Bitwise Operator XOR:",x^y)
# print("Bitwise Operator NOT:",~x, ~y) #negate
#
# a=10
# b=2
# print("Bitwise operator right shift >>:", a>>b) # 1010 right shift 2 - 10 (2)
# print ("Bitwise operator left shift<<:", a<<b) # 1010 left shift 2 - 101000 (40)

# x = 9 # 9 in binary format is 1001
# y = 65 # 65 in binary format is 1000001
# print("Bitwise Operator and:",x&y) #1 0000001
# print("Bitwise Operator or:",x|y) #73 1001001
# print("Bitwise Operator XOR:",x^y) #72  1001000
# print("Bitwise Operator NOT:",~x, ~y) #negate 6 62 (x=-x-1 formula for negate)
#
# print(bin(9))
# print(int(0b1001))
#
# a=9
# b=3
# print("Bitwise operator right shift >>:", a>>b) # 1001 right shift 3 - 1 (1)
# print ("Bitwise operator left shift<<:", a<<b) # 1001 left shift 3 - 1001000 (72)

#Assignment Operators
# Operators	Definitions	Output
# =	x = 15	x = 15
# +=	x += 15	x = x + 15
# -=	x -= 15	x = x - 15
# =	x = 15	x = x * 15
# /=	x /= 15	x = x / 15
# %=	x %= 15	x = x % 15
# //=	x //= 15	x = x // 15
# *=	x *= 15	x = x ** 15
# &=	x &= 15	x = x & 15
# |=	x |= 15	x = x | 15
# ^=	x ^= 15	x = x ^ 15
# >>=	x >>= 15	x = x >> 15
# <<=	x <<= 15	x = x << 15

# a = 50
# a +=10
# print("Sum:",a)
# a-=20
# print("Subtract:",a)
# a*=5
# print("Multiply:",a)
# a/=10
# print("Division:",a)
# a **=2
# print("Exponent:",a)

#Identity Operator
# Operators	Definitions
# is	True if the operands are identical
# is not	True if the operands are not identical
# Python offers 2 types of identity operators i.e. is and is not.
# Both are used to compare if two values are located on the same part of the memory. Two variables that are equal does not imply that they are identical.

# list1 = [15,30,45,60]
# list2 = [15,30,45,60]
# print("Identify operator is:", list1 is list2)
# print("Identify operator is not:", list1 is not list2)
#
# a=3
# b=3
# print(a is b)
# print(a is not b)

#Membership Operators
# Operators	Definitions
# in	True if value is found in the sequence
# not in	True if value is not found in the sequenc

# list1 = [15,30,45,60]
# list2 = [15,30,45,60]
# print("Membership operator in:", list1 in list2)
# print("Membership operator not in:", list1 not in list2)
# print("Membership operator in:", 45 in list1)

# x =20
# y = 86
# assignment operators
x = 12 # (00001100)
y = 6  # (00000110)

# The bin() function is used to print in binary format.

print ('x =', x ,' and y =',y)
# and operator
print ('x & y is equal to', bin(x & y))
# or operator
print ('x | y is equal to', bin(x | y))
# xor operator
print ('x ^ y is equal to', bin(x ^ y))
# shift left operator
print ('x << y is equal to', bin(x << y))
# shift right operator
print ('x >> y is equal to', bin(x >> y))
# not operator
print (' x is equal to', bin( x ))
