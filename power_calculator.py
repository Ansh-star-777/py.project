num = int(input("Enter the number: "))
n = int(input("Enter the power: "))

result = 1

for i in range(n):
    result = result * num

print("Result:", result)
