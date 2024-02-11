def conversation () :
    print ("Do you like coding in python? Answer yes or no")
    answer = input()
    if answer == "yes":
        print ("That's goof - the United states neefs more coders !!")
    if answer == "no":
        print ("Perhaps you will change your mind ")
    else :
        print ("I don't understand ")
    print ("Goodbye")

def main() :
    print ("welcome to my conversation program")
    conversation()
    print ("thanks for chatting with me")

if __name__ == '__main__':
    main()
