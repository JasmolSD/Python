"""
Assignment 2: Temperature Conversions
Submitted by Jasmol Singh Dhesi
Submitted:  January 18, 2024

Assignment 2: This assignment prompts the user for a temperature in Celsius and
then converts that temperature to a specified different temperature unit.

Assignment 1: This program demonstrates printing lines of text to the screen
"""


def print_header():
    """
    Print a header for the STEM Center Temperature Project.

    This function prints the header information: the project name and author

    Output:
    STEM Center Temperature Project
    Jasmol Dhesi
    """
    print("STEM Center Temperature Project")
    print("Jasmol Singh Dhesi")


def convert_units(celsius_value, units):
    """
    Module: Temperature Conversion

    This module provides a function for converting temperature values between
    Celsius, Fahrenheit, and Kelvin units.

    Functions:
        - convert_units(celsius_value, units): Convert a temperature value
        from Celsius to Fahrenheit or Kelvin.
            Parameters:
                - celsius_value (float): The temperature value in Celsius.
                - units (int): The desired units for conversion
                (0 for Celsius, 1 for Fahrenheit, 2 for Kelvin).
    Returns:
        - tuple: A tuple containing the converted temperature value and units.
        - str: Special error codes:
            - "ERROR_INVALID_TEMP":
                Returns an error when converting the Celsius value to a float.
            - "ERROR_INVALID_UNITS":
                Returns an error when the units value is not a valid integer
                or is outside the range [0, 1, 2].
    """
    # Tuple for conversion units
    temp_units = ("Celsius", "Fahrenheit", "Kelvin")

    while True:
        try:
            celsius_value = float(celsius_value)
            break
        except ValueError:
            return "ERROR_INVALID_TEMP"

    # Perform unit conversion
    # If units = 0 then celsius
    # If units = 1 return fahrenheit conversion,
    # if units = 2 then return kelvin conversion
    try:
        units = int(units)
        if units in [0, 1, 2]:
            # Input is valid
            if units == 0:
                answer = (celsius_value, temp_units[units])
                return answer
            elif units == 1:
                f_val = celsius_value * (9/5) + 32
                answer = (f_val, temp_units[units])
                return answer
            else:
                k_val = celsius_value + 273.15
                answer = (k_val, temp_units[units])
                return answer
        else:
            # Return a special error code for invalid units
            return "ERROR_INVALID_UNITS"
    except ValueError:
        # Return a special error code for invalid units
        return "ERROR_INVALID_UNITS"


def main():
    """
    The main() function is where the unit-test code is placed
    """
    print_header()

    # Receive user input for celsius value
    celsius_val_question = str("\nPlease enter a numerical"
                               + " temperature value in Celsius: ")
    celsius_value = input(celsius_val_question)

    # Receive user input for units value
    # If units = 0 then celsius
    # If units = 1 return fahrenheit conversion,
    # if units = 2 then return kelvin conversion
    unit_question = str('\nPlease enter the units  for the conversion desired:'
                        '\n Input 0 for a result in Celsius.'
                        '\n Input 1 for a result in Fahrenheit.'
                        '\n Input 2 for a result in Kelvin.'
                        '\n Enter units here: ')
    units = input(unit_question)

    # Proceed with the rest of your code using the valid input.
    # Call the convert_units function
    answer = convert_units(celsius_value, units)

    if answer == "ERROR_INVALID_TEMP":
        print(f"\n*** Invalid celsius input \"{celsius_value}\"."
              + " Input a numerical value such as \"55.98\".")
        while True:
            celsius_value_str = input(celsius_val_question)
            try:
                celsius_value = float(celsius_value_str)
                break
            except ValueError:
                print(f"\n*** Invalid celsius input \"{celsius_value}\"."
                      + " Input a numerical value such as \"55.98\".")

        answer = convert_units(celsius_value, units)

    # Confirm reception of valid temperature
    print(f"\nTemperature value accepted: {celsius_value} Celsius")

    if answer == "ERROR_INVALID_UNITS":
        (f"\n*** Invalid celsius input \"{celsius_value}\"."
         + " Input a numerical value such as \"55.98\".")
        while True:
            unit_str = input(unit_question)
            try:
                units = int(unit_str)
                if units in [0, 1, 2]:
                    # Input is valid
                    break
                else:
                    print(f"\n*** Invalid celsius input \"{celsius_value}\"."
                          + " Input a numerical value such as \"55.98\".")
            except ValueError:
                print(f"\n*** Invalid celsius input \"{celsius_value}\"."
                      + " Input a numerical value such as \"55.98\".")
        answer = convert_units(celsius_value, units)

    # Proceed with the rest of your code using the valid input
    print(f"\nConversion units value accepted: {units} {answer[1]}")
    print("\n...\nSuccess! Your input has been converted to: "
          + f"{answer[0]} {answer[1]}.")


if __name__ == "__main__":
    main()

r"""
STEM Center Temperature Project
Jasmol Singh Dhesi

Please enter a numerical temperature value in Celsius: 9-

Please enter the units value for the conversion desired:
 Input 0 for a result in Celsius.
 Input 1 for a result in Fahrenheit.
 Input 2 for a result in Kelvin.
 Enter units here: 22

*** Invalid celsius input "9-". Input a numerical value such as "55.98".

Please enter a numerical temperature value in Celsius: 60

Temperature value accepted: 60.0 Celsius

*** Invalid conversion units input "22". Please enter 0, 1, or 2.

Please enter the units value for the conversion desired:
 Input 0 for a result in Celsius.
 Input 1 for a result in Fahrenheit.
 Input 2 for a result in Kelvin.
 Enter units here: 1

Conversion units value accepted: 1 Fahrenheit

...
Success! Your input has been converted to 140.0 Fahrenheit.

Process finished with exit code 0

***Sample output 2***
STEM Center Temperature Project
Jasmol Singh Dhesi

Please enter a numerical temperature value in Celsius: 45.9

Please enter the units value for the conversion desired:
 Input 0 for a result in Celsius.
 Input 1 for a result in Fahrenheit.
 Input 2 for a result in Kelvin.
 Enter units here: 0

Temperature value accepted: 45.9 Celsius

Conversion units value accepted: 0 Celsius

...
Success! Your input has been converted to 45.9 Celsius.

Process finished with exit code 0


***Sample output 3***
STEM Center Temperature Project
Jasmol Singh Dhesi

Please enter a numerical temperature value in Celsius: 78

Please enter the units value for the conversion desired:
 Input 0 for a result in Celsius.
 Input 1 for a result in Fahrenheit.
 Input 2 for a result in Kelvin.
 Enter units here: 2

Temperature value accepted: 78 Celsius

Conversion units value accepted: 2 Kelvin

...
Success! Your input has been converted to 351.15 Kelvin.

Process finished with exit code 0
STEM Center Temperature Project
Jasmol Singh Dhesi

Please enter a numerical temperature value in Celsius: 135.64

Please enter the units value for the conversion desired:
 Input 0 for a result in Celsius.
 Input 1 for a result in Fahrenheit.
 Input 2 for a result in Kelvin.
 Enter units here: 1

Temperature value accepted: 135.64 Celsius

Conversion units value accepted: 1 Fahrenheit

...
Success! Your input has been converted to 276.152 Fahrenheit.

Process finished with exit code 0


***Sample output 4***

"""
