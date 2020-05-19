def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtruct(a, b):
    print(f"SUBTRUCTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("Let's do some math with just functions!")

age = add(20, 6)
height = subtruct(60, 3)
weight = multiply(30, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

#A puzzle for the extra credit, type it anyway.
print("Here is a puzzle.")

#what = add(age, subtruct(height, multiply(weight, divide(iq, 2))))
what = age + height - weight * iq / 2

print("That becomes:", what, "Can you do it by hand?")
