# #filer = open("C:\\Users\\naina\\OneDrive\\Desktop\\python\\pie-thon\\myfile.txt" ,"r")
# files = open("myfile.txt","r")
# print(files.read())
# #print(files.readline(20))
# #files.write("this is the good practise.")


# files.cl
# files=open("newfile.txt","w")
# files.write("This is file i created using the x \n attribute for file creation.")
# files.close()
# newfile=open("newfile.txt","r")
# print(newfile.readline())
# newfile.close()
# import os
# os.remove("myfile.txt")
import os 
if os.path.exists("newfile.txt"):
    os.remove("newfile.txt")
else:
    print("does not exist")
