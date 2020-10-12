#sets {}
# A set is a collection which is unordered and unindexed. In Python, sets are written with curly brackets.
#create a set
# S1 = {'python', "DS",'ML', 'DL'}
# print("Printing the set elements:", S1)

#Acess Items in sets
# We cannot access items in a set by referring to an index or a key.
# But we can loop through the set items using a for loop,
# or ask if a specified value is present in a set, by using the in keyword.

# S1 = {'python', "DS",'ML', 'DL'}
# print("Django" in S1)
# print("DL" in S1)
#
# for x in S1:
#     print("set elememnts:", x)

#Change items
# Once a set is created, you cannot change its items, but you can add new items.

# To add one item to a set use the add() method.

# To add more than one item to a set use the update() method.

S1 = {'python', "DS",'ML', 'DL'}
S1.add("Django")
print("New item added to the set:", S1)
S1.update(["Testing", "Devops", "AWS"])
print("Updated set with new items", S1)

#length
print("Length of the set:", len(S1))
S2 = {}
print(S2)
#join two sets
set1 = {"a", "b", "c","d"}
set2 = {10, 20, 30,40}
set3 = set1.union(set2)
print("The join of two sets", set3)
# The union() method returns a new set with all items from both sets:
set4 ={'a','b','c'}
set5 = {1,2,3}
set4.update(set5)
print("after updation:",set4)

#remove items
set6 = {1,2,3,4,5,6,7,8,9,10}
print(set6)
set6.remove(5)
print("Set after removing the item", set6)
set6.discard(5)
print("Update after discarded:", set6)
set6.pop()
print("Update after pop:", set6)
set6.clear()
print("update after clear:", set6)
# set6.remove(5)
# print("Set after removing the item", set6)
