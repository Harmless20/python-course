from sys import argv

script, filename = argv

txt = open(filename) #This opens the file.

#Bellow code will print to screen the file and will
#read the file. 
print(f"Here is your file {filename}:")
print(txt.read())

#Open and print the file again
print("Type the filename again:")
file_again = input("> ")

txt_again = open(txt_again.read())
