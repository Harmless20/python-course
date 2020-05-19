from sys import argv

script, input_file = argv
#The function that will print all the file.
def print_all(f):
    print(f.read())
#The function that will rewind the file.
def rewind(f):
    f.seek(0)
#The function that will print the file line by line.
def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's print rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1 #Current line is one here.
print_a_line(current_line, current_file)

current_line = current_line + 1  #Current line is two here.
print_a_line(current_line, current_file)

current_line = current_line + 1  #Current line is three here.
print_a_line(current_line, current_file)
