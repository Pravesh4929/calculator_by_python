def sc():
    print("Simple Calculator Options:")
    print("a) Add")
    print("b) Multiply")
    print("c) Divide")
    print("d) Subtraction")
    print("e) Modulo")
    print("f) Greater than")
    print("g) Smaller than")

    choice = input("Choose an option (a-g): ").lower()
    try:
        num1 = float(input("Enter first number according selected choice: "))
        num2 = float(input("Enter second number according selected choice : "))

        match choice:
            case 'a':
                print(f"Result: {num1 + num2}")
            case 'b':
                print(f"Result: {num1 * num2}")
            case 'c':
                if num2 != 0:
                    print(f"Result: {num1 / num2}")
                else:
                    print("Error: Division by zero")
            case 'd':
                print(f"Result: {num1 - num2}")
            case 'e':
                print(f"Result: {num1 % num2}")
            case 'f':
                print(f"{num1} is greater than {num2}: {num1 > num2}")
            case 'g':
                print(f"{num1} is smaller than {num2}: {num1 < num2}")
            case _:
                print("Invalid choice. The input value is wrong.")
    except ValueError:
        print("Error: Please enter valid numbers.")

def bc():
    print("Bitwise Converter Options:")
    print("a) Decimal to Binary")
    print("b) Decimal to Octal")
    print("c) Decimal to Hexadecimal")
    print("d) Binary to Decimal")
    print("e) Binary to Octal")
    print("f) Binary to Hexadecimal")
    print("g) Octal to Decimal")
    print("h) Octal to Binary")
    print("i) Octal to Hexadecimal")
    print("j) Hexadecimal to Decimal")
    print("k) Hexadecimal to Binary")
    print("l) Hexadecimal to Octal")

    choice = input("Choose an option (a-l): ").lower()
    value = input("Enter the value: ")

    try:
        match choice:
            case 'a':
                print(f"Binary: {bin(int(value))}")
            case 'b':
                print(f"Octal: {oct(int(value))}")
            case 'c':
                print(f"Hexadecimal: {hex(int(value))}")
            case 'd':
                print(f"Decimal: {int(value, 2)}")
            case 'e':
                print(f"Octal: {oct(int(value, 2))}")
            case 'f':
                print(f"Hexadecimal: {hex(int(value, 2))}")
            case 'g':
                print(f"Decimal: {int(value, 8)}")
            case 'h':
                print(f"Binary: {bin(int(value, 8))}")
            case 'i':
                print(f"Hexadecimal: {hex(int(value, 8))}")
            case 'j':
                print(f"Decimal: {int(value, 16)}")
            case 'k':
                print(f"Binary: {bin(int(value, 16))}")
            case 'l':
                print(f"Octal: {oct(int(value, 16))}")
            case _:
                print("Invalid choice. The input value is wrong.")
    except ValueError:
        print("Error: Please enter a valid value for the selected conversion.")

def main():
    while True:
        print("Multi-Calculator Options:")
        print("1) Simple Calculator")
        print("2) Bitwise Converter")
        print("3) Exit")

        choice = input("Choose an option (1-3): ")

        match choice:
            case '1':
                sc()
            case '2':
                bc()
            case '3':
                print("Exiting...")
                break
            case _:
                print("Invalid choice. The input value is wrong.")

if __name__ == "__main__":
    main()
