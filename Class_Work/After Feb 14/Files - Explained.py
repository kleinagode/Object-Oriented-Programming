

import os

#To create a new file just write open("filename.txt" "w")

myfile = open("myfile.txt","r") # Opens the file in read mode, you can also open it in w/a mode
                                 # Opening the file in W will rewrite the content of the file

content = myfile.read() #Reads the contenof the file in the variable



print(content) #Prints the content

myfile.close()

os.remove("myfile.txt")

# myfile.readlines() Returns a list of strings, the first item is the first line and so on
# myfile.readline() Reads one line at a time


