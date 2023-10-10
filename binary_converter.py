import sys

def binary_to_decimal(binary_input):
    output_decimal = 0

    # Check if input is binary or not
    if not is_binary(binary_input):
        print("Invalid input")
        sys.exit()
    else:
        # Reverse the order of the input to index from zero starting from the last character
        reverse_input = binary_input[::-1]

        # Use enumerate function to store the reversed input: key = index, value = character
        for index, value in enumerate(reverse_input):
            # Float the value since it's a string in order to perform a mathematical operation
            output_decimal += (int(value) * pow(2, index))

        return output_decimal

def is_binary(user_input):
    # Iterate through each character of user input
    for character in user_input:
        if character not in ['1', '0']:
            return False
    return True

def decimal_to_binary(base_10_number):
    binary_number = ""

    if base_10_number <= 0:
        return "0"

    while base_10_number > 0:
        module_division = (base_10_number % 2)
        binary_number = (str(module_division) + binary_number)
        base_10_number = (base_10_number // 2)

    return binary_number

def main():
    choice = input("Choose conversion (1: Binary to Decimal, 2: Decimal to Binary): ")

    if choice == "1":
        binary_input = input("Binary: ")
        decimal_output = binary_to_decimal(binary_input)
        print(f"Decimal-Value: {decimal_output}")
    elif choice == "2":
        base_10_number = int(input("Natural number: "))
        binary_output = decimal_to_binary(base_10_number)
        print(f"Binary: {binary_output}")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
