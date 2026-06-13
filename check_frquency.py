def check_frequency():
    test_dictionary = {
        "Codingal": 3,
        "is": 2,
        "best": 2,
        "for": 2,
        "Coding": 1
    }

    print(test_dictionary)

    word = input("Enter a word to check its frequency: ")

    if word in test_dictionary:
        print("Frequency of", word, "is", test_dictionary[word])
    else:
        print(word, "is not in the dictionary")

check_frequency()
