#this one is like your script with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

#this just takes one arguement
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no arguement
def prin_non():
    print("I have got nothing'.")


print_two("Isaac", "Kwame")
print_two_again("Isaac", "Kwame")
print_one("First")
prin_non()
