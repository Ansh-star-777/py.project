while True:
    try:
        age = int(input("Enter your age: "))

        if age % 2 == 0:
            print("The age is even.")
        else:
            print("The age is odd.")

        break

    except ValueError:
        print("Error: Please enter a whole number only.")
