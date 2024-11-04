HEXADECIMAL_SYMBOLS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

#переводи в різні системи числення
#def ten_to_n(decimal_num, n):
#    n_num = ""
#    decimal_num = int(decimal_num)
#    n = int(n)
#    while True:
#        n_num = HEXADECIMAL_SYMBOLS[decimal_num % n] + n_num
#        decimal_num //= n
#        if decimal_num == 0:
#           return n_num

#def n_to_ten(n_num, n):
#    decimal_num = 0
#    n = int(n)
#    for index, grade in enumerate(n_num[::-1]):
#        decimal_num += HEXADECIMAL_SYMBOLS.index(grade.upper()) * n**index
#    return str(decimal_num)

def n_to_n(n_num_in, n_in, n_out): # n <- numeric system
    decimal_num = 0
    n_in = int(n_in)
    n_out = int(n_out)
    n_num_out = ""
    for index, grade in enumerate(n_num_in[::-1]):
        decimal_num += HEXADECIMAL_SYMBOLS.index(grade.upper()) * n_in**index
    while True:
        n_num_out = HEXADECIMAL_SYMBOLS[decimal_num % n_out] + n_num_out
        decimal_num //= n_out
        if decimal_num == 0:
            return n_num_out

def n_defining_and_convertion(argument, n_in):
    print(f"We've identified your number as base-{n_in} numeric system number.")
    while True:
        n_out = input("To which numeric system (from 2 to 16), you want to convert your number: ")
        if n_out.isnumeric() and 2 <= int(n_out) <= 16:
            break
        print("Syntax error, try again")
    print(f"\n{n_in} -> {n_out} -base numeric system convertion:")
    print(f"{argument} -> {n_to_n(argument, n_in, n_out)}\n")

#валідація
def is_ncimal(argument, n):
    n = int(n)
    for symbol in argument:
        if symbol.upper() not in HEXADECIMAL_SYMBOLS[:n]:
            return False
    return True

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

#main
print("="*100)
print("This program wil help you to switch your number between different number systems\n"
      "If you number is decimal just enter it, if it's binary start with \"0b\" and if it's hexadecimal start with \"0x\"\n"
      "If it's in any other number system, just add \"xN\" at the end, where N is the number of your system.")
while True:
    number = input("Please enter your number: ")
    if number.isnumeric():
        n_defining_and_convertion(number, 10)

    elif number[:2] == "0b" and is_ncimal(number[2:], 2):
        n_defining_and_convertion(number[2:],2)

    elif number[:2] == "0x" and is_ncimal(number[2:], 16):
        n_defining_and_convertion(number[2:], 16)

    elif "x" in number:
        number = number.split("x")
        if number[1].isnumeric() and 2 <= int(number[1]) <= 16 and is_ncimal(number[0],number[1]):
            n_defining_and_convertion(number[0], number[1])
        else:
            print("Syntax error, try again")
            continue

    else:
        print("Syntax error, try again")
        continue

    if not continue_or_not():
        exit()