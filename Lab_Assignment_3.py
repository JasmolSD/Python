"""
Assignment 3: Implementing a Menu
Submitted by Jasmol Singh Dhesi
Submitted:  January 22, 2024

Assignment 3: This program will build a menu and the code to support it.
The menu provides a user interface for menu interaction.

Assignment 2: This program prompts the user for a temperature in Celsius and
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


def print_menu():
    """
    Module: Print Menu

    This module simply prints a menu which the user will interact with

    Returns:
        String: Main menu representation

    """
    print("Main Menu"
          + "\n---------"
          + "\n1 - Process a new data file"
          + "\n2 - Choose units"
          + "\n3 - Edit room filter"
          + "\n4 - Show summary statistics"
          + "\n5 - Show temperature by date and time"
          + "\n6 - Show histogram of temperatures"
          + "\n7 - Quit")


def new_file(dataset):
    """
    Open a new file
    """
    print("New File Function Called\n")


def choose_units():
    """
    Select units of choice

    """
    print("Choose Units Function Called\n")


def change_filter(sensor_list, active_sensors):
    """
    Change the filter used
    """
    print("Change Filter Function Called\n")


def print_summary_statistics(dataset, active_sensors):
    """
    Print a summary of statistics for the given sensors

    Parameters
    ----------
    dataset : TYPE
        DESCRIPTION.
    active_sensors : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    print("Summary Statistics Function Called\n")


def print_temp_by_day_time(dataset, active_sensors):
    """
    Print the temperature data response from sensor

    Parameters
    ----------
    dataset : TYPE
        DESCRIPTION.
    active_sensors : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    print("Print Temp by Day/Time Function Called\n")


def print_histogram(dataset, active_sensors):
    """
    Print a histogram for the active sensor provided

    Parameters
    ----------
    dataset : TYPE
        DESCRIPTION.
    active_sensors : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    print("Print Histogram Function Called\n")


def main():
    """
   Main Function: User Interaction with STEM Center Temperature Project

   This function initiates the main menu for the STEM Center Temperature
   Project, allowing the user to interact with various options.
   The user can choose tasks such as processing a new data file,
   selecting units, editing room filters, displaying summary statistics,
   showing temperature by date and time,
   presenting a histogram of temperatures, or quitting the program.

   Usage:
       - Call header to display project information.
       - Enter a while loop for continuous user interaction.
       - Display the main menu using print_menu().
       - Obtain user input for menu selection.
       - Handle user input errors, ensuring the input is a valid integer.
       - Perform tasks based on the user's selection using
           appropriate function calls.
       - Display error messages for invalid choices or non-numeric inputs.
       - Repeat the loop until the user chooses to quit (option 7).

   Returns:
       None
   """
    # Call header
    print_header()

    # Provide main menu
    # While loop to select an input
    while True:
        # Provide user the menu
        print_menu()

        # Get user input
        selection = input("\nWhat is your choice? ")

        # Error handling
        try:
            selection_int = int(selection)
            if selection_int == 1:
                new_file(None)
            elif selection_int == 2:
                choose_units()
            elif selection_int == 3:
                change_filter(None, None)
            elif selection_int == 4:
                print_summary_statistics(None, None)
            elif selection_int == 5:
                print_temp_by_day_time(None, None)
            elif selection_int == 6:
                print_histogram(None, None)
            elif selection_int == 7:
                print("Thank you for using the "
                      + "STEM Center Temperature Project")
                break
            else:
                print("Invalid Choice, "
                      + "please enter an integer between 1 and 7.\n")
        except ValueError:
            print("*** Please enter a number only ***\n")


if __name__ == "__main__":
    main()

r"""
STEM Center Temperature Project
Jasmol Singh Dhesi
Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

What is your choice? 1
New File Function Called

Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

What is your choice? 2
Choose Units Function Called

Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

What is your choice? 3
Change Filter Function Called

Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

What is your choice? 4
Summary Statistics Function Called

Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

What is your choice? 5
Print Temp by Day/Time Function Called

Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

What is your choice? 6
Print Histogram Function Called

Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

What is your choice? 9
Invalid Choice, please enter an integer between 1 and 7.

Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

What is your choice? -1
Invalid Choice, please enter an integer between 1 and 7.

Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

What is your choice? a
*** Please enter a number only ***

Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

What is your choice? 7
Thank you for using the STEM Center Temperature Project

Process finished with exit code 0
"""
