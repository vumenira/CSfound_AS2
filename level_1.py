def two_to_ten(binary_num):
    decimal_num = 0
    for n, grade in enumerate(binary_num[::-1]):
        decimal_num += int(grade) * 2**n
    return decimal_num

def ten_to_two(decimal_num):
    binary_num = ""
    while True:
        binary_num = str(decimal_num % 2) + binary_num
        decimal_num //= 2
        if decimal_num in [1, 0]:
            return binary_num

def is_binary(arg):
    for symbol in arg:
        if symbol not in ["1","0"]:
            return False
    return True

def continue_or_not():
    while True:
        command = input("Do you wan to enter another nuber (Y-yes / N-no): ")
        if command.upper() == "Y" or command.upper() == "YES":
            return True
        elif command.upper() == "N" or command.upper() == "NO":
            return False
        else:
            print("Syntax error, try again")



print("This program wil help you to switch your number from binary to decimal and in reverse"
      "\nIf you number is decimal just enter it, if it's binary enter \"0b\", and then your number (without space)")
while True:
    number = input("Please enter your number: ")
    if number.isnumeric():
        print(f"Decimal to binary conversion: "
              f"\n{number} -> {(ten_to_two(int(number)))}")
    elif number[:2] == "0b" and is_binary(number[2:]):
        print(f"Binary to decimal conversion: "
              f"\n{number[2:]} -> {two_to_ten(number[2:])}")
    else:
        print("Syntax error, try again")
        continue

    if not continue_or_not():
        exit()