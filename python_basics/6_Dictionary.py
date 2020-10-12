#Dictionaries
#A dictionary is a collection which is unordered, changeable and indexed.
#In Python dictionaries are written with curly brackets, and they have keys and values.
#Dictionaries are indexed by keys, which can be any immutable type; strings
#and numbers can always be keys.

#Creation of an dictionary
dict1 = {
  "brand": "Indigo",
  "model": "Galaxy",
  "year": 2010
}
print(dict1)

print("\n")

# dictionary of the days in the months of the year:

days = {'January': 31, 'February': 28, 'March': 31, 'April': 30,
        'May': 31, 'June': 30, 'July': 31, 'August': 31,
        'September': 30, 'October': 31, 'November': 30, 'December': 31, 'February':31}

print("Days in a month:-", days)
print("\n")
print(days["February"]) # If duplicate key exists, then console will take the latest value.

d = {'A':100, 'B':200}
print("Dictionary items:-", d)
d['A'] = 400
print("Dictionary items with updated value:", d)
d['C'] = 500
print("Dictionary items with new values:", d)

#Accessing Items
dict1 = {
  "brand": "Indigo",
  "model": "Galaxy",
  "year": 2010
}
x = dict1["model"]
print(x)

#get method
x = dict1.get("model")
print(x)

#changing values
# You can change the value of a specific item by referring to its key name:
dict1["year"] = 2020
print("Dictionary after changes:", dict1)

# Dictionary Methods
dict1 = {
  "brand": "Indigo",
  "model": "Galaxy",
  "year": 2010
}
print("The length of the dictionary is:", len(dict1))
# Adding Items - Adding an item to the dictionary is done by using a new index key and assigning a value to it.
dict1["color"] = "RED"
print("Adding an item to the dictionary is:", dict1)
#copy of the dictionary
dict2 = dict1.copy()
print("coying dictionary items in new dictionary:", dict2)

dict3 = dict(dict2)
print("copying dictionary item with dict()", dict3)

#Nested dictionaries
# Create a dictionary that contain three dictionaries:

myfamily = {"child1" : {"name" : "Emil","year" : 2004},
            "child2" : {"name" : "Tobias","year" : 2007},
            "child3" : {"name" : "Linus","year" : 2011}}
print("Nested Dictionaries:-", myfamily)

# Create three dictionaries, then create one dictionary that will contain the other three dictionaries:

child1 = {"name" : "Emil", "year" : 2004}
child2 = {"name" : "Tobias","year" : 2007}
child3 = {"name" : "Linus","year" : 2011}
myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print("Nested Dictionaries:-", myfamily)

#Removing items
# Removing Items:- There are several methods to remove items from a dictionary.

# The pop() method removes the item with the specified key name:

dict12 = {
  "brand": "Indigo",
  "model": "Galaxy",
  "year": 2010,
  "Color": "green"
}
print("Dictionary before Pop:-", dict12)
dict12.pop("model")
print("Dictionary after Pop:-",dict12)
print("\n")

# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):

dict13 = {
  "brand": "Indigo",
  "model": "Galaxy",
  "year": 2010,
  "Color": "green"
}

print("Dictionary before Popitem:-", dict13)
dict13.popitem()
print("Dictionary after Popitem:-",dict13)
print("\n")

# The del keyword removes the item with the specified key name:

dict14 = {
  "brand": "Indigo",
  "model": "Galaxy",
  "year": 2010,
  "Color": "green"
}

del dict14["model"]
print("Dictionary after del:-", dict14)

# The del keyword can also delete the dictionary completely:

dict2 = {
  "brand": "Indigo",
  "model": "Galaxy",
  "year": 2010,
  "Color": "green"
}

del dict2
# print(dict2) #this will cause an error because "thisdict" no longer exists.

# The clear() method empties the dictionary:

dict3= {
  "brand": "Indigo",
  "model": "Galaxy",
  "year": 2010,
  "Color": "green"
}

dict3.clear()
print("Dictionary after clear():-", dict3)