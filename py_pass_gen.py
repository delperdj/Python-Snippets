"""Password Generator."""
# JDD 11/2023

import random
import sys

# define use cases to generate random password
lowerLetters = [chr(i) for i in range(97, 123)]
upperLetters = [chr(i) for i in range(65, 91)]
numbers = [str(i) for i in range(10)]
symbols = ['!', '#', '$', '&', '(', ')', '*', '+']

def generate_password(number_lower_letters, number_upper_letters, number_numbers, number_symbols):
    """function for the 'RNG'."""
    password_list = []

    # pick the random lower case letters
    for _ in range(number_lower_letters):
        password_list.append(random.choice(lowerLetters))

    # pick the random upper case letters
    for _ in range(number_upper_letters):
        password_list.append(random.choice(upperLetters))

    # pick the random numbers
    for _ in range(number_numbers):
        password_list.append(random.choice(numbers))

    # pick the random symbols
    for _ in range(number_symbols):
        password_list.append(random.choice(symbols))

    # shuffle and return password
    random.shuffle(password_list)
    your_password = ""
    return your_password.join(password_list)

def main():
    """main is the Main."""
    print("\nWelcome to the PyPassword Generator!")

    if len(sys.argv) > 4:
        # if command line aruguments exist, it will execute this
        num_lower_letters = int(sys.argv[1])
        num_upper_letters = int(sys.argv[2])
        num_numbers = int(sys.argv[3])
        num_symbols = int(sys.argv[4])
    else:
        # ask for input for random generation
        num_lower_letters= int (input (
            "\nHow many lower case letters would you like in your password?\n"))
        num_upper_letters= int (input (
            "How many upper case letters would you like in your password?\n"))
        num_numbers = int (input ("How many numbers would you like?\n"))
        num_symbols = int (input ("How many symbols would you like?\n"))

    # pass input to function for password generation
    random_password = generate_password(
        num_lower_letters,
        num_upper_letters,
        num_numbers,
        num_symbols)
    # show returned random generated password from function
    print("\n\x1b[31mRandom generated password is:\x1b[0m")
    # can switch between formatted password or nonformatted password to display
    # print(random_password)
    print('\x1b[11;30;42m' + random_password + '\x1b[0m\n')

# main

if __name__ == "__main__":
    main()

# end
