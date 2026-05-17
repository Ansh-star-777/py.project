def circumference(radius):
    pi = 3.14
    return 2 * pi * radius

# taking input
r = float(input("Enter radius: "))

# calling function
answer = circumference(r)

print("Circumference of circle =", answer)
