"""
Submitted by Jasmol Singh Dhesi
Submission Date: March 13, 2024

Enhancements by Assignment:
Assignment 11:This assignment implements the print_temp_by_day_time() and get_avg_temperature_day_time() methods.
              The print_temp_by_day_time() function utilizes the get_avg_temperature_day_time() and pandas to
              calculate the average temperature for the dataset provided by day of week and time of day. Said function
              houses a dictionary of days of the week as well as times of the days.
              Pandas is used to construct a dataframe from the provided dictionaries and average temperatures.
              The data is thereafter displayed.

Assignment 10:This assignment implements functionalities including unit selection, temperature statistics calculation,
              and output formatting.
              Firstly, the choose_unit() function allows users to select between temperature units.
              Secondly, the get_avg_temperature_day_time() method computes the average temperature for a specified
              day and time.
              Lastly, the get_summary_statistics() function calculates and returns minimum, maximum, and average
              temperature values for active sensors.
              Additionally, the print_summary_statistics() function formats and displays these statistics appropriately.

Assignment 9: This assignment completes the function new_file() and methods process_file() and get_loaded_temps().
              new_file(dataset): Prompts the user to load a dataset into the provided dataset object and name it.
              process_file(file_name): Processes a file and returns a boolean indicating success
              get_loaded_temps(): Returns the number of loaded temperatures.
              Finally, the user is prompted to give the dataset a name.

Assignment 8: This assignment adds a Class to encapsulate temperature data.

Assignment 7: This assignment introduces two methods (in detail)
              print_filter() - prints a list of sensors that are active and inactive
              change_filter() - allows a user to activate a sensor or deactivate it
              The change_filter() is initiated through the menu prompt #3 choice.
              The change_filter() method will print the filter list showing active or
              inactive states, and it will allow the user to turn a sensor on or off.

Assignment 6: Bubble Sort a list of sensors using recursion

Assignment 5: A separate recursion assignment (as another project; see assignment 5)

Assignment 4: Creating a Sensor List and Filter List

Assignment 3: This program will build a menu and the code to support it.
              The menu provides a user interface for menu interaction.

Assignment 2: This program prompts the user for a temperature in Celsius and
              then converts that temperature to a specified different temperature unit.

Assignment 1: This program demonstrates printing lines of text to the screen
"""
import math
import pandas as pd

# global constant variable defining temperature units
UNITS = {
    0: ("Celsius", "C"),
    1: ("Fahrenheit", "F"),
    2: ("Kelvin", "K"),
}
# global integer variable that, by default, reads temperature data as celsius
current_unit = 0


def recursive_sort(list_to_sort, key=0):
    """
    Recursively sorts a list of tuples based on a specified key.

    This function sorts the input list of tuples 'list_to_sort' based on the specified 'key' parameter.
    The key determines which value within each tuple to use for sorting:
    - If 'key' is 0, the sorting is based on the first value of each tuple.
    - If 'key' is 1, the sorting is based on the second value of each tuple.

    Parameters:
        list_to_sort (list of tuples): The list of tuples to be sorted.
        key (int): An integer value that specifies which value within each tuple to use for sorting.
            Defaults to 0, sorting based on the first value of each tuple.

    Returns:
        list: The sorted list of tuples.

    Note:
        The function uses bubble sort algorithm with recursion to perform the sorting.
        It creates a copy of the input list to avoid altering the original list.
        Error handling ensures that 'list_to_sort' is a list of tuples and 'key' is a valid integer.

    Example:
        # Sorting a list of tuples based on the second value of each tuple
        sorted_list = recursive_sort([('b', 2), ('a', 1), ('c', 3)], key=1)
        print(sorted_list)
        # Output: [('a', 1), ('b', 2), ('c', 3)]
    """

    # Copy the list to prevent alteration of original list
    list_copy = list_to_sort.copy()

    # Error handling to check if list_to_sort is a list
    try:
        len(list_copy)
    except TypeError:
        print("List value is not a list value or tuple.")
        return None

    # Error handling to check if key value is an integer value
    try:
        key = int(key)
        if key < 0 or key >= len(list_to_sort):
            raise ValueError("Key value is not within the valid range of indices.")
    except ValueError as e:
        print("Illegal Key value inputted. See error: ", str(e))
        return None

    # Base case: if the list has only one element, return it
    if len(list_copy) == 1:
        return list_copy

    # Variable for the last index in list_to_sort (copied to list_copy)
    max_index = len(list_copy) - 1

    # Swap based off of the key
    swapped = False  # set swapped = false to check if any swaps were required in the pass
    for i in range(0, max_index):
        value_curr = list_copy[i][key]
        value_next = list_copy[i + 1][key]

        # If room number of current item is greater than next index, swap the two items
        if value_curr > value_next:
            (list_copy[i], list_copy[i + 1]) = (list_copy[i + 1], list_copy[i])
            swapped = True  # Change swapped to True to indicate there was a swap in this pass

    # Clause to end for loop early if no swaps, similar to base case
    if not swapped:
        return list_copy

    # Establish recursion: concatenate the recursive values to the greatest value in the list
    ret_value = recursive_sort(list_copy[:max_index], key) + [list_copy[max_index]]  # ascending
    # ret_value = [list_to_sort[max_index]] + recursive_sort(list_to_sort[:max_index], key)    # descending

    # Return reversed list
    return ret_value


def print_filter(sensor_list, filter_list):
    # Initialize length of list sensor_list
    MAX_INDEX = len(sensor_list)

    # Spacing for tidiness
    print()

    # Print sensor list with adjusted toggle
    for i in range(MAX_INDEX):
        # If the sensor num is in the filter list show [ACTIVE]
        if sensor_list[i][2] in filter_list:
            print(f"{sensor_list[i][0]}: {sensor_list[i][1]} [ACTIVE]")
        else:
            print(f"{sensor_list[i][0]}: {sensor_list[i][1]}")


def change_filter(sensors, sensor_list, filter_list):
    """
    Toggles sensors on and off based on filter_list.
    Invokes print_filter function to display the full list of sensors and their current active/inactive status.
    Prompts the user to select sensors to turn on/off until they enter "x" to exit the function.

    Parameters:
        sensors (dict): Dictionary containing sensor information.
        sensor_list (list): List of sensor data stored as tuples.
        filter_list (list): List of sensor numbers to keep active.

    Modifies:
        filter_list (list): Updated with user-specified sensor inclusions/exclusions.

    Returns:
        No returns
    """

    # Get user input to toggle sensors on or off
    prompt = str("\nType the sensor to toggle (e.g. 4201), "
                 "'all' to deactivate all sensors, to or x to end: ")

    # Loop to allow user to toggle multiple sensors on or off
    while True:
        # print the lists
        print_filter(sensor_list, filter_list)

        # Get user input on sensor they'd like to toggle
        toggle = input(prompt).strip()

        # Break out of loop if they input "x", else continue
        if toggle.lower() == "x":
            print()
            break

        # Shortcut to deactivate all filters
        if toggle.lower() == "all":
            filter_list.clear()
            print("All filters deactivated.\n")
            break

        # If user inputted sensor number is within list of sensors then toggle said sensor
        if toggle in sensors:
            # Get sensor num from dictionary using user input as key
            sensor_num = sensors[toggle][1]

            # If sensor number is missing from filter_list append sensor_num, else remove it
            if sensor_num not in filter_list:
                filter_list.append(sensor_num)
            else:
                # filter_list = [_ for _ in filter_list if _ != sensor_num]    # List comprehension to remove sensor
                filter_list.remove(sensor_num)  # More efficient removal of sensor_num being toggled off
        else:
            print("Invalid Sensor")


def print_header():
    """
    Print a header for the STEM Center Temperature Project.

    This function prints the header information: the project name and author

    Output:
    STEM Center Temperature Project
    Jasmol Singh Dhesi
    """
    print("STEM Center Temperature Project",
          "\nJasmol Singh Dhesi\n")


def convert_units(celsius_value, units):
    """
    Module: Temperature Conversion

    This module provides a function for converting temperature values between
    Celsius, Fahrenheit, and Kelvin units.

    Functions:
        - convert_units(celsius_value, units): Convert a temperature value
        between Celsius to Fahrenheit or Kelvin.
            Parameters:
                - celsius_value (float): The temperature value in Celsius.
                - units (int): The desired units for conversion
                (0 for Celsius, 1 for Fahrenheit, 2 for Kelvin).
    Returns:
        - tuple: A tuple containing the converted temperature value and units.
        - None: Returns None if the units value is not a valid integer
        or is outside the range [0, 1, 2].
    """
    # Validate and convert celsius_value to float
    try:
        celsius_value = float(celsius_value)
    except ValueError:
        return None

    # Validate units
    if units not in UNITS.keys():
        return None

    # variable for the temperature abbreviation
    temp_abbrev = UNITS[units][1]

    # Perform unit conversion from Celsius
    #    Dataset inputted into this function is always in Celsius
    if units == 0:
        return celsius_value, temp_abbrev
    elif temp_abbrev == 'K':
        return celsius_value + 273.15, temp_abbrev
    elif temp_abbrev == 'F':
        return celsius_value * 9 / 5 + 32, temp_abbrev


def print_menu():
    """
    Module: Print Menu

    This module simply prints a menu which the user will interact with.

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
    Prompt the user to enter the filename of a new dataset and load it into the provided dataset object.

    Args:
        dataset: An object representing the dataset to load the new file into.

    Returns:
        None
    """
    prompt = "\nPlease enter the filename of the new dataset: "
    file_name = str(input(prompt))

    if not dataset.process_file(file_name):
        print("File not found. Program aborted.\n")
        return None

    # upon success print number of samples in the dataset
    print(f"Loaded {dataset.get_loaded_temps()} samples.\n")

    dataset_name_prompt = "Please provide a 3 to 20 character name for the dataset: "

    while True:
        dataset_name = str(input(dataset_name_prompt))
        if 2 < len(dataset_name) <= 20:
            dataset.name = dataset_name
            break
        else:
            print("ERROR! INVALID DATASET NAME!")
    print()


def choose_units():
    """
    Allows the user to select units from a predefined list.

    Displays the current unit and presents a menu of available units.

    Prompts the user to choose a new unit, ensuring it is a valid integer corresponding to one of the available units.

    Updates the global variable 'current_units' to the user's selection.

    Note: The function utilizes the global UNITS dictionary to generate the menu options and validate user selection.
    """

    global current_unit

    prompt = "Choose new unit: "
    temp_keys = UNITS.keys()  # All temperature keys for units dict

    # Loop until the user chooses a valid unit
    while True:
        # Display the current unit
        print(f"\nCurrent Unit is: {UNITS[int(current_unit)][0]}")

        # Display the available units
        for key, temp in UNITS.items():
            print(f"{key} - {temp[0]}")

        # Attempt to get user input for the new unit
        try:
            # Validate the input is an integer
            new_unit = int(input(prompt))
            # Check if the input is a valid unit
            if new_unit not in temp_keys:
                print("Please choose a unit from the list.")
            else:
                # Update current_unit and exit the loop
                current_unit = new_unit
                break
        # Handle non-integer input
        except ValueError:
            print("*** Please enter a number only ***")

    print()


def print_summary_statistics(dataset, active_sensors):
    """
    Print summary statistics for the given sensors.

    Parameters
    ----------
    dataset : DataSet
        The dataset containing temperature data.
    active_sensors : list
        A list of active sensor numbers.

    Returns
    -------
    None.

    """
    # Get summary statistics for the active sensors from the dataset
    summary_data = dataset.get_summary_statistics(active_sensors)

    # If summary data is not available, print an error message and return
    if summary_data is None:
        print("Please load data file and make sure at least one sensor is active.\n")
        return None

    # Unpack summary data
    min_temp, max_temp, average_temp = summary_data

    # formatting data to contain two decimal places
    formatted_min = "{:.2f}".format(min_temp)
    formatted_max = "{:.2f}".format(max_temp)
    formatted_avg = "{:.2f}".format(average_temp)

    # Print summary statistics
    print(f"Summary statistics for {dataset.name}:")
    print(f"Minimum Temperature: {formatted_min} {UNITS[current_unit][1]}")
    print(f"Maximum Temperature: {formatted_max} {UNITS[current_unit][1]}")
    print(f"Average Temperature: {formatted_avg} {UNITS[current_unit][1]}")
    print()


def print_temp_by_day_time(dataset, active_sensors):
    """
    Print the average temperature data by day and time for the specified sensors.

    Parameters
    ----------
    dataset : Dataset
        The dataset containing temperature data.
    active_sensors : list of str
        List of active sensors for which to calculate average temperatures.

    Returns
    -------
    None
        This function does not return any value.

    """
    DAYS = {
        0: "SUN",
        1: "MON",
        2: "TUE",
        3: "WED",
        4: "THU",
        5: "FRI",
        6: "SAT"
    }

    HOURS = {
        0: "Mid-1AM  ",
        1: "1AM-2AM  ",
        2: "2AM-3AM  ",
        3: "3AM-4AM  ",
        4: "4AM-5AM  ",
        5: "5AM-6AM  ",
        6: "6AM-7AM  ",
        7: "7AM-8AM  ",
        8: "8AM-9AM  ",
        9: "9AM-10AM ",
        10: "10AM-11AM",
        11: "11AM-NOON",
        12: "NOON-1PM ",
        13: "1PM-2PM  ",
        14: "2PM-3PM  ",
        15: "3PM-4PM  ",
        16: "4PM-5PM  ",
        17: "5PM-6PM  ",
        18: "6PM-7PM  ",
        19: "7PM-8PM  ",
        20: "8PM-9PM  ",
        21: "9PM-10PM ",
        22: "10PM-11PM",
        23: "11PM-MID ",
    }

    # Check if data is loaded
    is_data = dataset.get_loaded_temps()

    # If summary data is not available, print an error message and return
    if is_data is None:
        print("Please load data file and make sure at least one sensor is active.\n")
        return None

    temp_dict = {"Day": [values for values in HOURS.values()]}
    for i in DAYS.keys():
        average_vals = []
        for j in HOURS.keys():
            average_temp = round(dataset.get_avg_temperature_day_time(active_sensors, i, j), 1)
            if average_temp is None:
                average_temp = "---"
            average_vals.append(average_temp)
        temp_dict[DAYS[i]] = average_vals

    # dataframe manipulation
    df_temp = pd.DataFrame(temp_dict)
    df_temp.set_index('Day', inplace=True)  # changes the index
    df_temp.index.name = None  # removes empty index row

    # printing the output
    print(f"\nAverage Temperatures for {dataset.name}"
          f"\nUnits are in {UNITS[current_unit][0]}\n")
    print(df_temp, '\n')


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


class TempDataset:
    """
    A class representing a dataset with various methods for data processing and analysis.

    Attributes:
        DEFAULT_NAME (str): The default name for the dataset.
        MIN_NAME_LENGTH (int): The minimum allowed length for a dataset name.
        MAX_NAME_LENGTH (int): The maximum allowed length for a dataset name.
        dataset_num (int): A class variable to keep track of the number of Dataset instances.

    Methods:
        __init__(): Initializes a Dataset instance.
        data_name(): Getter method for the dataset name.
        data_name(new_name): Setter method for the dataset name.
        process_file(file_name): Processes a file and returns a boolean indicating success.
        get_summary_statistics(filter_list): Returns summary statistics based on a filter list.
        get_avg_temperature_day_time(filter_list, day, time): Returns the average temperature for a given day and time.
        get_num_temps(filter_list, lower_bound, upper_bound): Returns the number of temperatures within a range.
        get_loaded_temps(): Returns the number of loaded temperatures.
        get_num_objects(): Class method to get the number of Dataset objects.
    """
    # class (static) attributes
    DEFAULT_NAME = "Unnamed"
    MIN_NAME_LENGTH = 3
    MAX_NAME_LENGTH = 20

    # class attribute to record number of objects with class Dataset; will change over time
    dataset_num = 0

    # initializer instance method
    def __init__(self):
        """
        Initializes a Dataset instance with default values.
        Increments the dataset_num counter.
        """
        self._data_set = None
        self._name = TempDataset.DEFAULT_NAME

        # each time an object with class Dataset is instantiated, increase counter
        TempDataset.dataset_num += 1

    # additional instance methods
    def process_file(self, file_name):
        """
        Processes a file containing sensor data and extracts temperature values.

        Args:
            file_name (str): The name of the file to process.

        Returns:
            bool: True if the file was processed successfully and temperature values were extracted,
                  False otherwise.
        """
        try:
            my_file = open(file_name, 'r')
        except FileNotFoundError:
            return False

        # reinitialize data set as empty list
        self._data_set = []

        # read in the file line-by-line
        for next_line in my_file:
            # each line is formatted as 'Day of Week, Time of Day, Sensor Number, Reading Type, Value'
            my_list = list(next_line.split(','))
            value = my_list[3]  # Reading type

            # we only want to read in temperature values 'TEMP'
            if value != 'TEMP':
                continue

            day_of_week = int(my_list[0])
            time_of_day = math.floor(float(my_list[1]) * 24)  # convert time of day to hour
            sensor_num = int(my_list[2])
            temp = float(my_list[4])

            my_tuple = day_of_week, time_of_day, sensor_num, temp
            self._data_set.append(my_tuple)

        return True

    def get_summary_statistics(self, filter_list):
        """
        Returns summary statistics based on a filter list.

        This method calculates and returns the minimum, maximum, and average temperature
        of active sensors in the dataset based on the provided filter list.

        Args:
            filter_list (list): A list of sensor numbers to filter the dataset.

        Returns:
            tuple or None: A tuple containing the minimum, maximum, and average temperature
                           of active sensors in the filter list. Returns None if the dataset is None
                           or if the filter list is empty.

        Note:
            If the dataset is empty or the filter list is empty, returns None.

            This method relies on the `convert_units` function to convert temperature values
            to the appropriate units before calculating summary statistics.
        """
        if self._data_set is None or not filter_list:
            return None

        # Filter data using list comprehension
        #     If sensor number is in the filter list, add its temperature to the new_data list
        #     Use function convert_units(celsius_value, units) to appropriately convert temperature values
        new_data = [convert_units(i[3], current_unit)[0] for i in self._data_set if i[2] in filter_list]

        # Check if new_data is empty
        if new_data is None:
            return None

        # Calculate summary statistics: minimum, maximum, and average temperature of temperature dataset
        # average_temp = self.get_avg_temperature_day_time(filter_list)
        average_temp = sum(new_data) / len(new_data)
        min_temp = min(new_data)
        max_temp = max(new_data)

        return min_temp, max_temp, average_temp

    def get_avg_temperature_day_time(self, filter_list, day, time):
        """
        Calculate the average temperature for a specific day and time.
    
        Args:
            filter_list (list): A list of filters to apply to the dataset.
            day (str): The day for which to calculate the average temperature.
            time (str): The time of day for which to calculate the average temperature.
    
        Returns:
            float or None: The average temperature if data is available and calculations are possible, otherwise None.
        """
        if self._data_set is None or not filter_list:
            return None

        # Filter data using list comprehension
        new_data = [convert_units(i[3], current_unit)[0] for i in self._data_set
                    if i[2] in filter_list and i[1] == time and i[0] == day]

        if not new_data:  # Check if new_data is empty
            return None

        average_temp = float(sum(new_data) / len(new_data))
        return average_temp

    def get_num_temps(self, filter_list, lower_bound, upper_bound):
        """
        Returns the number of temperatures within a range.

        Args:
            filter_list (list): A list of filters to apply to the dataset.
            lower_bound (float): The lower bound of the temperature range.
            upper_bound (float): The upper bound of the temperature range.

        Returns:
            int: The number of temperatures within the specified range.
        """
        if self._data_set is None:
            return None
        else:
            return 0

    def get_loaded_temps(self):
        """
        Returns the number of loaded temperatures.

        Returns:
            int: The number of loaded temperatures.
        """
        if self._data_set is None:
            return None
        else:
            return len(self._data_set)

    @classmethod
    def get_num_objects(cls):
        """
        Class method to get the number of Dataset objects.

        Returns:
            int: The number of Dataset objects.
        """
        return cls.dataset_num

    # getter and setter for _data_name variable
    @property
    def name(self):
        """
        Getter method for the dataset name.

        Returns:
            str: The dataset name.
        """
        return self._name

    @name.setter
    def name(self, new_name):
        """
        Setter method for the dataset name.

        Args:
            new_name (str): The new name for the dataset.

        Raises:
            ValueError: If the new name is not a string, if it contains non-printable characters such as \n
            or if it is not of correct length.
        """
        # error handling to check if new_name is of appropriate data type or non-printable characters
        if not isinstance(new_name, str) or '\n' in new_name:
            raise ValueError  # ("Invalid dataset name")

        # error handling to check if the length of the new_name is within parameters
        if TempDataset.MIN_NAME_LENGTH <= len(new_name) <= TempDataset.MAX_NAME_LENGTH:
            self._name = new_name
        else:
            raise ValueError


def main():
    """
    Initializes data structures for sensors and filters.
    Displays the program header and main menu, and handles user input errors.

    Initializes:
        sensors (dict): Contains sensor dictionary with room numbers as keys and tuples of (description, sensor number).
        sensor_list (list): Contains sensor data as tuples in the format (room number, description, sensor number).
        filter_list (list): Contains sensor numbers for filtering purposes.

    Prints:
        Program header.

    Displays Main Menu:
        Prompts user to make a selection from the menu options.

    Error Handling:
        Validates user input to ensure it's an integer within the valid range (1 to 7).
        Provides an error message for invalid inputs and prompts the user to try again.

    Returns:
        None
    """
    # instantiation of class TempDataset() for sensor temperature dataset
    current_set = TempDataset()  # Temperatures2022-03-07.csv

    # dict of all sensors in format {room_num: (desc, sensor_num)}
    sensors = {"4213": ("STEM Center", 0),
               "4201": ("Foundations Lab", 1),
               "4204": ("CS Lab", 2),
               "4218": ("Workshop Room", 3),
               "4205": ("Tiled Room", 4),
               "Out": ("Outside", 5)
               }
    # list of tuples formatted (Room Number, Room Description, Sensor_Number)
    sensor_list = [(room_num, desc, sensor_num) for room_num, (desc, sensor_num) in sensors.items()]

    # Sort the sensor_list based off room number
    sensor_list = recursive_sort(sensor_list, 0)

    # list of the sensor numbers
    filter_list = [sensors[_][1] for _ in sensors]

    # Call header
    print_header()

    # Provide main menu and receive user input via while loop
    while True:
        # Provide user the menu
        print_menu()

        # Get user input
        selection = input("\nWhat is your choice? ")

        # Error handling for menu choice selection
        try:
            selection_int = int(selection)
            if selection_int == 1:
                new_file(current_set)
            elif selection_int == 2:
                choose_units()
            elif selection_int == 3:
                change_filter(sensors, sensor_list, filter_list)
            elif selection_int == 4:
                print_summary_statistics(current_set, filter_list)
            elif selection_int == 5:
                print_temp_by_day_time(current_set, filter_list)
            elif selection_int == 6:
                print_histogram(current_set, filter_list)
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
SAMPLE RUN:
    
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

What is your choice? 5
Please load data file and make sure at least one sensor is active.

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
Please load data file and make sure at least one sensor is active.

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

Please enter the filename of the new dataset: Temperatures2022-03-07.csv
Loaded 11724 samples.

Please provide a 3 to 20 character name for the dataset: Testeroo

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

Average Temperatures for Testeroo
Units are in Celsius

            SUN   MON   TUE   WED   THU   FRI   SAT
Mid-1AM    21.1  20.6  21.7  21.5  21.0  21.1  19.8
1AM-2AM    21.1  20.5  21.6  21.5  20.9  21.1  19.9
2AM-3AM    21.1  20.4  21.5  21.4  20.9  21.1  19.8
3AM-4AM    21.1  20.4  21.4  21.3  20.8  21.0  19.8
4AM-5AM    21.1  20.4  21.4  21.2  20.8  21.0  19.9
5AM-6AM    21.0  20.2  21.4  21.2  20.7  20.8  19.8
6AM-7AM    20.9  19.9  21.3  21.0  20.6  20.6  19.8
7AM-8AM    20.7  20.0  21.1  20.9  20.6  20.5  19.9
8AM-9AM    20.6  20.2  21.2  20.8  20.7  20.3  19.9
9AM-10AM   20.9  21.1  22.0  20.9  21.2  20.2  20.2
10AM-11AM  21.2  21.9  22.8  21.5  22.1  20.4  20.6
11AM-NOON  21.5  22.6  23.4  22.2  22.7  20.7  20.8
NOON-1PM   21.6  23.0  23.9  22.6  23.0  21.0  21.0
1PM-2PM    21.7  23.3  24.0  23.1  23.2  21.0  21.0
2PM-3PM    21.9  23.6  24.2  23.5  23.3  21.1  21.0
3PM-4PM    21.9  24.0  24.4  23.6  23.5  21.1  20.8
4PM-5PM    21.7  24.2  24.5  23.8  23.6  21.0  20.9
5PM-6PM    21.6  24.1  24.4  23.7  23.7  20.8  20.9
6PM-7PM    21.5  23.4  23.9  23.4  23.2  20.7  20.7
7PM-8PM    21.4  23.0  23.2  22.8  22.3  20.3  20.5
8PM-9PM    21.2  22.6  22.3  22.1  21.6  19.8  20.2
9PM-10PM   21.0  22.3  21.8  21.7  21.2  19.7  19.9
10PM-11PM  20.8  22.0  21.7  21.5  21.2  19.8  19.8
11PM-MID   20.8  21.9  21.6  21.2  21.1  19.8  19.7 

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

Current Unit is: Celsius
0 - Celsius
1 - Fahrenheit
2 - Kelvin
Choose new unit: 1

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

Average Temperatures for Testeroo
Units are in Fahrenheit

            SUN   MON   TUE   WED   THU   FRI   SAT
Mid-1AM    70.0  69.2  71.0  70.7  69.9  70.0  67.7
1AM-2AM    70.0  68.9  70.9  70.6  69.7  70.0  67.7
2AM-3AM    70.0  68.8  70.6  70.5  69.6  69.9  67.6
3AM-4AM    70.0  68.8  70.6  70.4  69.5  69.8  67.6
4AM-5AM    69.9  68.7  70.5  70.2  69.4  69.7  67.7
5AM-6AM    69.9  68.4  70.4  70.1  69.3  69.5  67.7
6AM-7AM    69.6  67.8  70.3  69.9  69.1  69.2  67.7
7AM-8AM    69.3  68.1  70.0  69.7  69.1  68.8  67.8
8AM-9AM    69.1  68.4  70.2  69.4  69.2  68.6  67.8
9AM-10AM   69.5  70.0  71.6  69.6  70.2  68.3  68.3
10AM-11AM  70.2  71.5  73.0  70.7  71.7  68.7  69.2
11AM-NOON  70.7  72.8  74.2  71.9  72.8  69.3  69.4
NOON-1PM   70.9  73.3  75.1  72.8  73.5  69.7  69.8
1PM-2PM    71.0  73.9  75.2  73.6  73.7  69.9  69.8
2PM-3PM    71.4  74.4  75.5  74.3  73.9  69.9  69.8
3PM-4PM    71.4  75.3  75.9  74.5  74.2  70.0  69.4
4PM-5PM    71.0  75.5  76.0  74.8  74.5  69.9  69.6
5PM-6PM    70.8  75.3  75.9  74.7  74.7  69.5  69.6
6PM-7PM    70.8  74.2  75.1  74.2  73.7  69.2  69.2
7PM-8PM    70.5  73.3  73.7  73.0  72.2  68.5  69.0
8PM-9PM    70.2  72.6  72.1  71.8  70.8  67.7  68.4
9PM-10PM   69.9  72.1  71.3  71.1  70.2  67.4  67.9
10PM-11PM  69.4  71.6  71.0  70.7  70.1  67.7  67.7
11PM-MID   69.4  71.4  70.9  70.2  70.1  67.7  67.5 

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

4201: Foundations Lab [ACTIVE]
4204: CS Lab [ACTIVE]
4205: Tiled Room [ACTIVE]
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside [ACTIVE]

Type the sensor to toggle (e.g. 4201), 'all' to deactivate all sensors, to or x to end: 4201

4201: Foundations Lab
4204: CS Lab [ACTIVE]
4205: Tiled Room [ACTIVE]
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside [ACTIVE]

Type the sensor to toggle (e.g. 4201), 'all' to deactivate all sensors, to or x to end: 4204

4201: Foundations Lab
4204: CS Lab
4205: Tiled Room [ACTIVE]
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside [ACTIVE]

Type the sensor to toggle (e.g. 4201), 'all' to deactivate all sensors, to or x to end: 4205

4201: Foundations Lab
4204: CS Lab
4205: Tiled Room
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside [ACTIVE]

Type the sensor to toggle (e.g. 4201), 'all' to deactivate all sensors, to or x to end: Out

4201: Foundations Lab
4204: CS Lab
4205: Tiled Room
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside

Type the sensor to toggle (e.g. 4201), 'all' to deactivate all sensors, to or x to end: x

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

Average Temperatures for Testeroo
Units are in Fahrenheit

            SUN   MON   TUE   WED   THU   FRI   SAT
Mid-1AM    68.8  68.4  72.7  71.3  70.6  70.7  66.8
1AM-2AM    69.0  68.3  72.5  71.1  70.3  70.5  66.9
2AM-3AM    69.1  68.3  72.3  70.9  70.0  70.4  67.0
3AM-4AM    69.2  68.1  72.2  70.8  69.8  70.3  67.0
4AM-5AM    69.2  68.1  72.1  70.6  69.7  70.1  67.1
5AM-6AM    69.2  68.0  72.1  70.5  69.6  70.0  67.1
6AM-7AM    68.8  67.9  72.1  70.1  69.4  69.6  67.1
7AM-8AM    68.1  68.1  71.8  70.0  69.5  69.2  67.1
8AM-9AM    67.4  68.1  71.1  69.5  69.7  68.3  67.1
9AM-10AM   67.3  69.1  71.5  69.4  70.6  67.1  67.2
10AM-11AM  67.1  70.4  72.3  69.9  71.5  66.6  67.2
11AM-NOON  66.9  70.9  73.2  70.4  72.2  66.6  66.6
NOON-1PM   66.8  71.2  73.1  71.3  72.1  66.3  65.9
1PM-2PM    66.7  71.9  73.6  72.3  71.9  66.1  65.5
2PM-3PM    66.9  72.8  74.3  73.1  72.3  66.1  65.2
3PM-4PM    66.7  73.3  74.7  74.0  72.7  66.1  65.0
4PM-5PM    66.7  73.8  75.1  74.4  73.4  66.0  64.9
5PM-6PM    66.7  74.2  75.7  74.9  74.0  66.0  64.9
6PM-7PM    66.7  73.5  75.1  74.6  73.5  65.8  64.8
7PM-8PM    67.2  73.4  74.0  73.4  72.5  65.7  64.8
8PM-9PM    67.8  73.4  73.0  72.6  71.7  65.4  64.7
9PM-10PM   68.1  73.3  72.2  71.7  71.1  65.5  64.9
10PM-11PM  68.3  73.2  71.8  71.3  70.9  66.3  65.5
11PM-MID   68.6  73.0  71.5  70.9  70.8  66.6  65.7 

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
