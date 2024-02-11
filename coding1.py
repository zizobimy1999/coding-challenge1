def intro_msg():
    print("I can reverse a string")
    print("If you give me 'apple' I will return 'elppa'")
    print("I can even do an entire sentence")
    return input("Type something and see (type 'quit' to exit): ")

def reverse_word(characters):
    reverse_string = ''
    for character in characters:
        reverse_string = character + reverse_string
    return reverse_string

# Main function
def main():
    while True:
        word = intro_msg()

        if word.lower() == 'quit':
            print("Exiting the program.")
            break

      # Check if the user wants to quit
        reversed_word = reverse_word(word)
        print('Below is your string in reverse:\n{}'.format(reversed_word))

# Check if the script is being run as the main module
if __name__ == "__main__":
    main()
