def find_squares(start, end):
    square_list = []

    for num in range(start, end + 1):
        square_list.append(num ** 2)

    print("Squares:", square_list)

    print("Even Squares:")
    for square in square_list:
        if square % 2 == 0:
            print(square)

    print("Odd Squares:")
    for square in square_list:
        if square % 2 != 0:
            print(square)


begin = int(input("Enter starting number: "))
finish = int(input("Enter ending number: "))

find_squares(begin, finish)
