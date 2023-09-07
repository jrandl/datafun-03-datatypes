"""
Author: Josiah Randleman
Date: 9/8/2023
"""

import math
import statistics

# TODO: import from local util_datafun_logger.py 
# import from local files
from util_datafun_logger import setup_logger

# Set up logging .............................................

# TODO: Call the setup_logger function to create a logger and get the log file name
# Call the setup_logger function
logger, logname = setup_logger(__file__)


# TODO: Create some shared data lists if you like - or just create them in your functions

list1 = [3,7,12,19,24,31,36,42,49,53,58,63,70,76,82,88,92,97,103,110]
listx = [0,1,2,3,4,5,6,7,8,9]
listy =  [2,4,6,8,11,14,17,19,21,24]

# TODO: define some custom functions

def calculate_statistics():
    #List 1 -> List Statistics
    mean_value1 = statistics.mean(list1)
    mean_valuex = statistics.mean(listx)
    mean_valuey = statistics.mean(listy)

    median_value1 = statistics.median(list1)
    median_valuex = statistics.median(listx)
    median_valuey = statistics.median(listy)

    try:
        mode_value1 = statistics.mode(list1)
        mode_valuex = statistics.mode(listx)
        mode_valuey = statistics.mode(listy)
    except statistics.StatisticsError:
        mode_value1 = "No unique mode"
        mode_valuex = "No unique mode"
        mode_valuey = "No unique mode"

    std_dev_value1 = statistics.stdev(list1)
    std_dev_valuex = statistics.stdev(listx)
    std_dev_valuey = statistics.stdev(listy)

    variance_value1 = statistics.variance(list1)
    variance_valuex = statistics.variance(listx)
    variance_valuey = statistics.variance(listy)

    logger.info("---------------------------------")
    logger.info(f"List1 Mean: {mean_value1}")
    logger.info(f"ListX Mean: {mean_valuex}")
    logger.info(f"ListY Mean: {mean_valuey}")
    logger.info("---------------------------------")
    logger.info(f"List1 Median: {median_value1}")
    logger.info(f"ListX Median: {median_valuex}")
    logger.info(f"ListY Median: {median_valuey}")
    logger.info("---------------------------------")
    logger.info(f"List1 Mode: {mode_value1}")
    logger.info(f"ListX Mode: {mode_valuex}")
    logger.info(f"ListY Mode: {mode_valuey}")
    logger.info("---------------------------------")
    logger.info(f"List1 Standard Deviation: {std_dev_value1}")
    logger.info(f"ListX Standard Deviation: {std_dev_valuex}")
    logger.info(f"ListY Standard Deviation: {std_dev_valuey}")
    logger.info("---------------------------------")
    logger.info(f"List1 Variance: {variance_value1}")
    logger.info(f"ListX Variance: {variance_valuex}")
    logger.info(f"ListY Variance: {variance_valuey}")
    logger.info("---------------------------------")


def calculate_correlation_and_prediction():
    # Lists 2 -> Lists - Correlation and Prediction 
    correlation = statistics.correlation(listx, listy)
    slope, intercept = statistics.linear_regression(listx, listy)

    # Choose an x value off in the future (future x)
    future_x = 15

    # Extend the line out into the unknown future
    # and read the value (of future y)
    future_y = round(slope * future_x + intercept)

    logger.info("---------------------------------")
    logger.info(f"ListX: {listx}")
    logger.info(f"ListY:{listy}")
    logger.info(f"Correlation between ListX and ListY = {correlation:.2f}")
    logger.info("---------------------------------")
    logger.info(f"Slope of ListX and ListY: {slope}")
    logger.info(f"Intercept of ListX and ListY:{intercept}")
    logger.info("---------------------------------")
    logger.info("Let's use our best fit line to PREDICT a future value.")
    logger.info(f"At future x = {future_x:d},")
    logger.info(f"We predict the value of y will be { future_y:d}.")
    logger.info("---------------------------------")

def use_builtin_functions():
    # Lists 3 -> Lists - Using Python Built-in Functions 
    minimun1 = min(list1)
    minimunx = min(listx)
    minimuny = min(listy)

    maximum1 = max(list1)
    maximumx = max(listx)
    maximumy = max(listy)

    length1 = len(list1)
    lengthx = len(listx)
    lengthy = len(listy)

    sum1 = sum(list1)
    sumx = sum(listx)
    sumy = sum(listy)

    average1 = sum(list1) / len(list1)
    averagex = sum(listx) / len(listx)
    averagey = sum(listy) / len(listy)

    unique_set1 = set(list1)
    unique_setx = set(listx)
    unique_sety = set(listy)

    sorted_list1 = sorted(list1)
    sorted_listx = sorted(listx)
    sorted_listy = sorted(listy)

    sorted_desc_list1 = sorted(list1, reverse=True)
    sorted_desc_listx = sorted(listx, reverse=True)
    sorted_desc_listy = sorted(listy, reverse=True)

    logger.info(f"Minimum of List1 = {minimun1:d},")
    logger.info(f"Minimum of ListX = {minimunx:d},")
    logger.info(f"Minimum of ListY = {minimuny:d},")
    logger.info("---------------------------------")
    logger.info(f"Maximum of List1 = {maximum1:d},")
    logger.info(f"Maximum of ListX = {maximumx:d},")
    logger.info(f"Maximum of ListY = {maximumy:d},")
    logger.info("---------------------------------")
    logger.info(f"Length of List1 = {length1:d},")
    logger.info(f"Length of ListX = {lengthx:d},")
    logger.info(f"Length of ListY = {lengthy:d},")
    logger.info("---------------------------------")
    logger.info(f"Sum of List1 = {sum1:d},")
    logger.info(f"Sum of ListX = {sumx:d},")
    logger.info(f"Sum of ListY = {sumy:d},")
    logger.info("---------------------------------")
    logger.info(f"Average of List1 = {average1:.2f},")
    logger.info(f"Average of ListX = {averagex:.2f},")
    logger.info(f"Average of ListY = {averagey:.2f},")
    logger.info("---------------------------------")
    logger.info(f"Unique Elements of List1 = {unique_set1},")
    logger.info(f"Unique Elements of ListX = {unique_setx},")
    logger.info(f"Unique Elements of ListY = {unique_sety},")
    logger.info("---------------------------------")
    logger.info(f"Sorted List1 = {sorted_list1},")
    logger.info(f"Sorted ListX = {sorted_listx},")
    logger.info(f"Sorted ListY = {sorted_listy},")
    logger.info("---------------------------------")
    logger.info(f"Sorted in Descending List1 = {sorted_desc_list1},")
    logger.info(f"Sorted in Descending ListX = {sorted_desc_listx},")
    logger.info(f"Sorted in Descending ListY = {sorted_desc_listy},")
    logger.info("---------------------------------")

def explore_list_methods():
    # Lists 4 -> List Methods
    # Creating a new short list named lst
    lst = [5, 2, 3, 4, 1]

    logger.info(f"Lst = {lst},")

    # Using append() to add a single value to the list
    lst.append(6)
    logger.info(f"After append(6), List = {lst},")

    # Using extend() to extend the list with a new list
    lst.extend([7, 8, 9])
    logger.info(f"After extend([7, 8, 9]), List = {lst},")

    # Using insert() to insert a value at a specific index (inserting 15 at index 1)
    lst.insert(1, 15)
    logger.info(f"After insert(1, 15), List = {lst},")

    # Using remove() to remove the number 5 from the list
    lst.remove(5)
    logger.info(f"After remove(5), List = {lst},")

    # Using count() to count how many times 2 appears in the list
    count_2 = lst.count(2)
    logger.info(f"Count of 2 in List = {count_2},")

    # Using sort() to sort the list in ascending order
    lst.sort()
    logger.info(f"After sort(), List = {lst},")

    # Using sort() with reverse=True to sort the list in descending order
    lst.sort(reverse=True)
    logger.info(f"After sort(reverse=True), List = {lst},")

    # Using copy() to create a copy of the list
    lst_copy = lst.copy()
    logger.info(f"Copy of List = {lst_copy},")

    # Using pop() to remove the first item from the list
    first_item_popped = lst.pop(0)
    logger.info(f"After pop(0), List = {lst}, Popped Item = {first_item_popped},")

    # Using pop() to remove the last item from the list
    last_item_popped = lst.pop()
    logger.info(f"After pop(), List = {lst}, Popped Item = {last_item_popped},")

    logger.info("---------------------------------")

def apply_filter_and_map():
    # Lists 5 -> List Transformations - Using filter() and map()

    # Using filter() to keep elements less than 4
    filtered_list = list(filter(lambda x: x < 4, listx))

    # Using map() to calculate the cube root of each element
    cube_root_list = list(map(lambda x: math.pow(x, 1/3), listx))

    # Using map() to calculate the volume of a cube for each side length in the list
    cube_volume_list = list(map(lambda x: x * x * x, listx))

    logger.info(f"Demo List: {listx},")
    logger.info(f"Filtered List (x < 4): {filtered_list},")
    logger.info(f"Cube Root List: {cube_root_list},")
    logger.info(f"Cube Volume List: {cube_volume_list},")
    logger.info("---------------------------------")

def use_list_comprehensions():
   # Lists 6 -> List Transformations - Using List Comprehension 

    # Using list comprehension to filter elements less than 4
    filtered_list_comprehension = [x for x in list1 if x < 4]

    # Using list comprehension to triple each element
    tripled_list_comprehension = [x * 3 for x in list1]

    # Using list comprehension for a custom transformation (subtracting 2 from each element)
    custom_transformed_list = [x - 2 for x in list1]

    logger.info(f"Filtered List via Comprehension (x < 4): {filtered_list_comprehension},")
    logger.info(f"Tripled List via Comprehension: {tripled_list_comprehension},")
    logger.info(f"Custom Transformed List via Comprehension (x - 2): {custom_transformed_list},")
    logger.info("---------------------------------")


def show_log():
    """Read log file and print it to the terminal"""
    with open(logname, "r") as file_wrapper:
        print(file_wrapper.read())

# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
# Literally: "if this module name == the name of the main module"

if __name__ == "__main__":
    calculate_statistics()
    calculate_correlation_and_prediction()
    use_builtin_functions()
    explore_list_methods()
    apply_filter_and_map()
    use_list_comprehensions()
    
    show_log()
