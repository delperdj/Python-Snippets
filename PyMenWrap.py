"""Python Menu Wrapper."""
# JDD 12/2023

import os

def run_program(script_filename):
    """menu wrapper program to call other python programs."""
    args = input(
        f"Enter command line arguments for {script_filename} "
        "(or press enter to run without arguments): "
    )
    os.system(f'python {script_filename}.py {args}')

def main():
    """main is the Main."""
    print("\n Welcome to 'Ease of Access' Python programs!")

    programs = {
        "1": ("Password Generator", "PyPassGen"),
        "2": ("Temperature Conversion", "PyTempConv"),
        "3": ("Clipboard History", "PyClipHist"),
        "4": ("Currency Conversion", "PyCurrConv"),
        "5": ("Time Zone Conversion", "PyTimeZone")
    }

    while True:
        print("\nHere is a menu of programs to use:")
        for key, (display_name, _) in programs.items():
            print(f"{key}. {display_name}")
        print("0. Exit")
        print("\nCommand line arguments cheat sheet:")
        print("Password		- 4: lowercase amount; uppercase amount; number amount; symbol amout")
        print("Temperature 	- 1: temperature e.g., 45F, 102c, etc.")
        print("Clipboard	- 1: history amount")
        print("Currency		- 2: from currency e.g., UDS, EUR, etc.; to currency e.g., USD, EUR, etc.")
        print("Time\t\t\t- 3: orginal time YYYY-MM-DD HH:MM:SS; "
              "source time e.g., US/Eastern; "
              "target time e.g., Asia/Tokyo")

        choice = input("\nEnter the number of the program to run, or 0 to exit: ")

        if choice in programs:
            _, script_filename = programs[choice]
            run_program(script_filename)
        elif choice == '0':
            print("Exiting the program. Have a great day! :) ")
            break
        else:
            print("Invalid choice, please try again. :( ")

# main

if __name__ == "__main__":
    main()

#end
