# JDD 11/2023
# Temperature Conversion

import sys

# function for temperature conversion
def convert_temperature(temp):
    # extract the numerical part of the temperature and convert it to an integer
    degree = int(temp[:-1])
    # extract the convention part of the temperature input (either 'C/c' or 'F/f')
    i_convention = temp[-1].upper()

	# check if the input convention is 'C/c' (Celsius)
    if i_convention == "C":
        #convert the Celsius temperature to Fahrenheit
        result = int(round((9 * degree) / 5 + 32))
        o_convention = "Fahrenheit" # set the output convention as Fahrenheit
    # check if the input convention 'F/f' (Fahrenheit)
    elif i_convention == "F":
        # convert the Fahrenheit temperature to Celsius
        result = int(round((degree - 32) * 5 / 9))
        o_convention = "Celsius" # set the output convention as Celsius
    else:
        # if the input convention is neither 'C/c' nor 'F/f', print an error message and exit the program
        print("Input proper convention. Did you specify 'F' or 'C' at the end of the temperature during input?")
        return None

    return result, o_convention

def main():
    print("\nWelcome to the PyTemperature Conversion!")
    
    if len(sys.argv) > 1:
        # store command line argument that is provided
        temp = sys.argv[1]
    else:
        # prompt the user to input a temperature in the format (e.g., 45F, 102C, etc.)
        temp = input("\nInput the temperature you would like to convert? (e.g., 45F, 102C): ")

    result = convert_temperature(temp)
    if result:
        # display the converted temperature in the specified output convention
        # can switch between formatted password or nonformatted password to display
        # print("\nThe temperature is:", result[0], "degrees", result[1])
        print("\nThe temperature is:", '\x1b[11;30;42m' + str(result[0]) + " degrees " + result[1] + '\x1b[0m')

# main

if __name__ == "__main__":
    main()

# end
