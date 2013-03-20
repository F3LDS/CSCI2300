alphabet = []
key = 4


def menu():
    print "What would you like to do?"
    print "[1] Encrypt a message"
    print "[2] Decrypt a message"
    print "[3] Exit program"
    choose = raw_input("Enter a number: ")
    return choose


def cryptIt(phrase):
    result = ""
    for i in range(97, 123):
        alphabet.append(chr(i))  # Add all of letters of the alphabet list
    for i in phrase:  # For each letter in the phrase...
        if i != ' ':  # and when that letter is NOT a space
            if (alphabet.index(i) + key) < len(alphabet):  # and that letter, when shifted, does not fall out of our list
                result = result + alphabet[alphabet.index(i) + key]  # Return the previous letters PLUS the new letter shifted by ?
            else:
                result = result + alphabet[alphabet.index(i) + key - len(alphabet)]
        else:
            result = result + ' '
    return result


def decryptIt(coded):
    return 0


def main():
    keepGoing = True
    while keepGoing:
        response = menu()
        if response == "1":
            plain = raw_input("text to be encoded: ")
            print cryptIt(plain)
        elif response == "2":
            coded = raw_input("code to be decyphered: ")
            print decryptIt(coded)
        elif response == "0":
            print "Thanks for doing secret spy stuff with me."
            keepGoing = False
        else:
            print "I don't know what you want to do..."

main()
