# Test dictionary
test_dict = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}

# Print dictionary
print("Dictionary:", test_dict)

# Take input from user
value = int(input("Enter the value to check frequency: "))

# Count frequency
count = 0
for v in test_dict.values():
    if v == value:
        count += 1

# Print result
print("Frequency of", value, "is:", count)
