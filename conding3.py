def decimal_to_binary(number):
    result = ""
    while number > 0:  # keep dividing until at 0
        remainder = number % 2
        number = number // 2
        result = str(remainder) + result  # place string in reverse order
    return result

def is_valid_decimal_input(user_input):
    return user_input.isdigit() and 0 <= int(user_input) <= 9

# Main function
def main():
    good_input = False
    while not good_input:
        user_input = input("Enter a valid decimal number [0-9]: ")

        if is_valid_decimal_input(user_input):
            good_input = True
        else:
            print("Invalid input. Please enter a valid decimal number.")

    num = int(user_input)
    print("Decimal {} to Binary: {}".format(num, decimal_to_binary(num)))

if __name__ == "__main__":
    main()
