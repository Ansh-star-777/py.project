n = int(input("Enter a decimal number: "))

binary = ""

while n > 0:
    binary = str(n % 2) + binary
    n = n // 2

print("Binary:", binary)
