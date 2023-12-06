#lists are elements of either same data type or multiple data type
fruits = ["custard","pineapple","dragonfruit","kiwi"]
print(fruits)
print(len(fruits))
print(type(fruits))
#access the elements by giving the range
print(fruits[1:4])
#APPEND() CAN BE USED TO ADD THE ITEMS TO LIST
fruits.append("carrot")
print(fruits)
#remove () to remove items from the list
fruits.remove("pineapple")
print(fruits)
fruits.insert(2,"apple")#INSERT() TO  ADD THE ITEM AT PARTICULAR LOCATION
print(fruits)
#combining the lists by concatenation 
vegetables = ["chilli" ,"tomato","onion","cauliflower"]
eatables = fruits + vegetables
print(eatables)
# mixed types of the list
mixed = ["strings", 34,34.2,3434]
print (mixed)
for i in mixed:
    print(i)
    print(type(i))
    #nested list
eatable = [["chilli" ,"tomato","onion","cauliflower"],
           ["custard","pineapple","dragonfruit","kiwi"]
           ]
print (eatable)