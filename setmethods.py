set1 = {"keys","locks","labourers","bikes"}
set3 = {"ravan","sita","ram"}
#print(set1)
#set1.add("faircream")#	Adds an element to the set"
#set1.clear()#	Removes all the elements from the set
set2=set1.copy()#	Returns a copy of the set
print(set1.difference(set3))#	Returns a set containing the difference between two or more sets
# print(set1.difference_update())#	Removes the items in this set that are also included in another, specified set
# print(set1.discard())#	Remove the specified item
print(set1.intersection(set3))#	Returns a set, that is the intersection of two or more sets
print(set1.intersection_update(set3))#	Removes the items in this set that are not present in other, specified set(s)
print(set2)
# print(set1.isdisjoint())#Returns whether two sets have a intersection or not
# print(set1.issubset())#	Returns whether another set contains this set or not
# print(set1.issuperset())#	Returns whether this set contains another set or not
print(set2.pop())#	Removes an element from the set
print(set2)
print(set2.remove("locks"))#Removes the specified element
print(set2)
# print(set1.symmetric_difference())#	Returns a set with the symmetric differences of two sets
# print(set1.symmetric_difference_update())#	inserts the symmetric differences from this set and another
# print(set1.union())#	Return a set containing the union of sets
print(set1.update(set3))#	Update the set with another set, or any other iterable