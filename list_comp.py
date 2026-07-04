# Question 1

number = int(input("Enter a number: "))

odd = [i for i in range(1, number + 1) if i % 2 != 0]
even = [i for i in range(1, number + 1) if i % 2 == 0]

print("Odd numbers:", odd)
print("Even numbers:", even)

# Question 2

fruits = ["apple", "banana", "mango", "orange"]

new_fruits = [fruit.capitalize() for fruit in fruits]

print("Original:", fruits)
print("New:", new_fruits)
