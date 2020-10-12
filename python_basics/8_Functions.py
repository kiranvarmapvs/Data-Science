#Functions
#A function is basically a collection of code which performs a specific task.
#A function is a block of code which only runs when it is called.
#You can pass data, known as parameters, into a function.
#A function can return data as a result.

#creating a function
# def Hello_world():
#     print('hello world')
#     print('have a nice day')
# # calling the function. Note - use the function name followed by the parentheses
# Hello_world()
#
# #Paremeters in Function
# def Hello(Name, Age): # Defining a function with one parameter
#     print("Hi",Name)
#     print("Age", Age)
# Hello('Kiran', 36) #Calling the function with parameter value
#
# def Age(Name, Last_Name):
#     print("First Name", Name + " " + "Last Name:", Last_Name)
# Age('Kiran', 'Pinnamaraju')
#
# #Calculate sum of two values
# def sum(a, b):
#     return a+b
#
# a = int(input("Enter the value of a:"))
# b = int(input("Enter the value of b:"))
# print("sum of two numbers:", sum(a,b))
# Hello_world()
# Age('Kiran', 'Pinnamaraju')

#Average of 3 numbers

# def avg(n1,n2,n3):
#     return (n1+n2+n3)/3.0
#
# print("Welcome")
# res1 = avg(10,20,30)
# res2 = avg(1,2,3)
# res3 = avg(3.1,2,4.5)
# print(res1)
# print(res2)
# print(res3)

#Python function to calculate the average of three numbers by taking user inputs

# def average(n1,n2,n3):
#     return (n1+n2+n3)/3
# print("WECLOME TO LEENA IT")
# num1 = int(input("Enter the first number:"))
# num2 = int(input("Enter the second number:"))
# num3 = int(input("Enter the third number:"))
# result = average(num1, num2, num3)
# print("The average of three numbers:-",result)

# def Mul(x):
#     return 10*x
# print(Mul(5))
# print(Mul(10))

#Local Variables
# def F1():
#     N=5
#     print("The value of N is:", N)
#
# def F2():
#     N=10
#     print("The value of N is:", N)
#     F1()
# F2()
#
# F1()

#Global Variables
X =10
def F3():
    print("The value of X is:", X)

def F4():
    N=20
    print("The value of x is:", N)
    F3()
F4()

# Method	Description
# Python abs()
# returns absolute value of a number
# Python all()
# returns true when all elements in iterable is true
# Python any()
# Checks if any Element of an Iterable is True
# Python ascii()
# Returns String Containing Printable Representation
# Python bin()
# converts integer to binary string
# Python bool()
# Converts a Value to Boolean
# Python bytearray()
# returns array of given byte size
# Python bytes()
# returns immutable bytes object
# Python callable()
# Checks if the Object is Callable
# Python chr()
# Returns a Character (a string) from an Integer
# Python classmethod()
# returns class method for given function
# Python compile()
# Returns a Python code object
# Python complex()
# Creates a Complex Number
# Python delattr()
# Deletes Attribute From the Object
# Python dict()
# Creates a Dictionary
# Python dir()
# Tries to Return Attributes of Object
# Python divmod()
# Returns a Tuple of Quotient and Remainder
# Python enumerate()
# Returns an Enumerate Object
# Python eval()
# Runs Python Code Within Program
# Python exec()
# Executes Dynamically Created Program
# Python filter()
# constructs iterator from elements which are true
# Python float()
# returns floating point number from number, string
# Python format()
# returns formatted representation of a value
# Python frozenset()
# returns immutable frozenset object
# Python getattr()
# returns value of named attribute of an object
# Python globals()
# returns dictionary of current global symbol table
# Python hasattr()
# returns whether object has named attribute
# Python hash()
# returns hash value of an object
# Python help()
# Invokes the built-in Help System
# Python hex()
# Converts to Integer to Hexadecimal
# Python id()
# Returns Identify of an Object
# Python input()
# reads and returns a line of string
# Python int()
# returns integer from a number or string
# Python isinstance()
# Checks if a Object is an Instance of Class
# Python issubclass()
# Checks if a Object is Subclass of a Class
# Python iter()
# returns iterator for an object
# Python len()
# Returns Length of an Object
# Python list() Function
# creates list in Python
# Python locals()
# Returns dictionary of a current local symbol table
# Python map()
# Applies Function and Returns a List
# Python max()
# returns largest element
# Python memoryview()
# returns memory view of an argument
# Python min()
# returns smallest element
# Python next()
# Retrieves Next Element from Iterator
# Python object()
# Creates a Featureless Object
# Python oct()
# converts integer to octal
# Python open()
# Returns a File object
# Python ord()
# returns Unicode code point for Unicode character
# Python pow()
# returns x to the power of y
# Python print()
# Prints the Given Object
# Python property()
# returns a property attribute
# Python range()
# return sequence of integers between start and stop
# Python repr()
# returns printable representation of an object
# Python reversed()
# returns reversed iterator of a sequence
# Python round()
# rounds a floating point number to ndigits places.
# Python set()
# returns a Python set
# Python setattr()
# sets value of an attribute of object
# Python slice()
# creates a slice object specified by range()
# Python sorted()
# returns sorted list from a given iterable
# Python staticmethod()
# creates static method from a function
# Python str()
# returns informal representation of an object
# Python sum()
# Add items of an Iterable
# Python super()
# Allow you to Refer Parent Class by super
# Python tuple() Function
# Creates a Tuple
# Python type()
# Returns Type of an Object
# Python vars()
# Returns _dict_ attribute of a class
# Python zip()
# Returns an Iterator of Tuples
# Python _import_()
# Advanced Function Called by import





