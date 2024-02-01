#file handling is the  way to  handle the files and data during the web development
#open("filename","Permission")
# s = " This is the sentence , i'm gonna  write in the new file"
# file = open("C:\\codes\\python\\pie-thon\\textfile.txt","w")
# file.write(s)
# print("file created")
# file.close()
# to read the content of the textfile.txt , we are gonna use the read() method
# file = open("textfile.txt","r")
# fileContent = file.read()
# print(fileContent)
# list1 = ["python","java","javascript","reactjs"]
# file = open("textfile.txt","w")
# file.writelines(list1)
# print("file Created")
# file.close()
# file = open("textfile.txt","r")
# fileContent = file.readlines()
# print(fileContent)
# s = " This is the sentence , i'm gonna  write in the new file"
# file = open("C:\\codes\\python\\pie-thon\\textfile.txt","w")
# file.write(s)
# print("fileupdated")
# file.close()
list1 = ["python","java","javascript","reactjs"]
file = open("textfile.txt","a")
file.writelines(list1)
print("file Created")
file.close()