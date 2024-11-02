HEXADECIMAL_SYMBOLS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

#переводи в різні системи числення
def two_to_ten(binary_num):
    decimal_num = 0
    for n, grade in enumerate(binary_num[::-1]):
        decimal_num += int(grade) * 2**n
    return str(decimal_num)

def ten_to_two(decimal_num):
    binary_num = ""
    decimal_num = int(decimal_num)
    while True:
        binary_num = str(decimal_num % 2) + binary_num
        decimal_num //= 2
        if decimal_num == 0:
            return binary_num

def sixteen_to_ten(hexa_num):
    decimal_num = 0
    for n, grade in enumerate(hexa_num[::-1]):
        decimal_num += HEXADECIMAL_SYMBOLS.index(grade.upper()) * 16**n
    return str(decimal_num)

def ten_to_sixteen(decimal_num):
    hexa_num = ""
    decimal_num = int(decimal_num)
    while True:
        hexa_num = HEXADECIMAL_SYMBOLS[decimal_num%16] + hexa_num
        decimal_num //= 16
        if decimal_num == 0:
            return hexa_num


#валідації
def is_binary(arg):
    for symbol in arg:
        if symbol not in ["1","0"]:
            return False
    return True

def is_hexadecimal(arg):
    for symbol in arg:
        if symbol.upper() not in HEXADECIMAL_SYMBOLS:
            return False
    return True

#визначення типу конвертації, та конвертація
def conversion(from_type, argument):
    print(f"We've classified your number as {from_type}")
    while True:
        to_type = input("Which type you want to convert to\n"
                        "(2-binary / 10-decimal / 16-hexadecimal): ")
        if to_type.lower() in ["2", "binary"]:
            to_type = "binary"
            break
        elif to_type.lower() in ["10", "decimal"]:
            to_type = "decimal"
            break
        elif to_type.lower() in ["16", "hexadecimal"]:
            to_type = "hexadecimal"
            break
        else:
            print("Syntax error, try again")

    if from_type == to_type:
        print(f"{from_type.title()} to {to_type} conversion:\n"
              f"{argument} -> {argument}")
    elif from_type == "decimal":
        if to_type == "binary":
            print(f"Decimal to binary conversion: "
                  f"\n{argument} -> 0b{ten_to_two(argument)}")
        else:
            print(f"Decimal to hexadecimal conversion: "
                  f"\n{argument} -> 0x{ten_to_sixteen(argument)}")

    elif from_type == "binary":
        if to_type == "decimal":
            print(f"Binary to decimal conversion: "
                  f"\n{argument} -> {two_to_ten(argument)}")
        else:
            print(f"Binary to hexadecimal conversion: "
                  f"\n{argument} -> 0x{ten_to_sixteen(two_to_ten(argument))}")

    elif from_type == "hexadecimal":
        if to_type == "decimal":
            print(f"Hexadecimal to decimal conversion: "
                  f"\n{argument} -> {sixteen_to_ten(argument)}")
        else:
            print(f"Hexadecimal to binary conversion: "
                  f"\n{argument} -> 0b{ten_to_two(sixteen_to_ten(argument))}")

#очевидно
def continue_or_not():
    while True:
        command = input("Do you wan to enter another nuber (Y-yes / N-no): ")
        if command.upper() == "Y" or command.upper() == "YES":
            print("="*100)
            return True
        elif command.upper() == "N" or command.upper() == "NO":
            return False
        else:
            print("Syntax error, try again")


print("="*100)
print("This program wil help you to switch your number between binary, decimal and hexadecimal\n"
      "If you number is decimal just enter it, if it's binary start with \"0b\" and if it's hexadecimal start with \"0x\"")
while True:
    number = input("Please enter your number: ")
    if number.isnumeric():
        conversion("decimal", number)

    elif number[:2] == "0b" and is_binary(number[2:]):
        conversion("binary", number[2:])

    elif number[:2] == "0x" and is_hexadecimal(number[2:]):
        conversion("hexadecimal", number[2:])

    else:
        print("Syntax error, try again")
        continue

    if not continue_or_not():
        exit()