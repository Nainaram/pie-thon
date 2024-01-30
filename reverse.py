# str = input("enter the palindrome:") this is string slicing method to reverse a string
# if str == str[::-1]:
#     print("it is a palindrome")
# else:print("not a palindrome")
# this  above program is used to check whether entered string is a palidrome or 


# METHOD 2:below is the second method to reverse a string
# def reverse(s):
# 	str = ""
# 	for i in s:
# 		#print(i)
# 		str = i + str
# 		print(str)
# 	return str

# s = "MAREERSIAJ"

# # print("The original string is : ", end="")
# # print(s)

# print("The reversed string(using loops) is : ", end="")
# print(reverse(s))
# def reverse(s):
# 	if len(s) == 0:
# 		return s
# 	else:
#          return reverse(s[1:]) + s[0]

     
# """ take a example of s  = "hello"
# 	  this enters the recursion 
# 	  as s["ello"] + h
# 	     s[["llo"]+ e]"+h
# 		 s[[["lo"]+"l"]"e"]+h
# 		 s[[[["o]+l]+l]+e]+h
# 		 s[[[[[""]+o]+l]+l]+e]+h"""


# s = input("enter the string to  reverse a string")
# print("The original string is : ", end="")
# print(s)

# print("The reversed string(using recursion) is : ", end="")
# print(reverse(s))
 # this is the third way to reverse a string
# using a stack in python
# create a empty stack
# str = input("enter the string:")
# n = len(str)
# stack = []
# def isEmpty(stack):
#     if len(stack) == 0:
#         return len(stack)
# def push(stack, item):
#     stack.append(item)
# def pop(stack):
#     if isEmpty(stack):
#         return
#     return stack.pop()
# for i in range(0, n, 1):
#         push(stack, str[i])
# str = " "
# for i in range(0, n, 1):
#         str += pop(stack)

# print("The reversed string(using stack) is : ", end="")
# print(str)
#ANOTHER WAY TO REVERSE A STRING
# Python code to reverse a string
# using reversed()
# Function to reverse a string
# def reverse(string):
# 	string = "".join(reversed(string))
# 	return string

# s = input("enter the string:")

# print("The original string is : ", end="")
# print(s)

# print("The reversed string(using reversed) is : ", end="")
# print(reverse(s))

# Function to reverse a string
def reverse(string):
	string = [string[i] for i in range(len(string)-1, -1, -1)]
	return "".join(string)

s = "traehdliw"

print("The original string is : ", s)

print("The reversed string(using reversed) is : ", reverse(s))


 