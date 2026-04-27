a = int(input("Enter first number (A): "))
b = int(input("Enter second number (B): "))
c = int(input("Enter third number (C): "))

print("Before swapping:")
print("A =", a, "B =", b, "C =", c)

a = b
b = c
c = a

print("After swapping:")
print("A =", a, "B =", b, "C =", c)
