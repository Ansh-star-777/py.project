class RomanConverter:
    def convert_to_roman(self, number):
        value_symbols = [
            (1000, "M"), (900, "CM"),
            (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"),
            (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"),
            (5, "V"), (4, "IV"),
            (1, "I")
        ]

        result = ""
        for value, symbol in value_symbols:
            while number >= value:
                result += symbol
                number -= value

        return result


if __name__ == "__main__":
    num = int(input("Enter an integer: "))

    converter = RomanConverter()
    roman_value = converter.convert_to_roman(num)

    print(f"The Roman numeral for {num} is: {roman_value}")
