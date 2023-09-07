"""
Author: Josiah Randleman
Date: 9/8/2023

"""

from util_datafun_logger import setup_logger
import collections

# Call the setup_logger function to create a logger and get the log file name
logger, logname = setup_logger(__file__)

# Tuples to represent programming languages and their features
def illustrate_tuples():
    lang_tuple = ("Python", "Dynamically Typed", "Interpreted")
    db_tuple = ("MySQL", "RDBMS", "Open Source")
    framework_tuple = ("Django", "Python", "Web Development")

    logger.info(f"Programming Language: {lang_tuple}")
    logger.info(f"Database: {db_tuple}")
    logger.info(f"Framework: {framework_tuple}")
    logger.info("---------------------------------")

# Sets to represent libraries in different programming languages
def illustrate_sets():
    python_libs = {"Numpy", "Pandas", "Django"}
    js_libs = {"React", "Angular", "Vue"}

    intersection = python_libs & js_libs
    union = python_libs | js_libs

    logger.info(f"Python Libraries: {python_libs}")
    logger.info(f"JavaScript Libraries: {js_libs}")
    logger.info(f"Common Libraries: {intersection}")
    logger.info(f"All Libraries: {union}")
    logger.info("---------------------------------")

# Dictionary to represent word frequency in a text file
def illustrate_dictionaries():
    with open('text_simple.txt', 'r') as f:
        text = f.read()
        words = text.split()

    # Using dictionary comprehension to count the frequency of each word
    word_count = {word: words.count(word) for word in set(words)}

    # Sorting dictionary by value
    sorted_word_count = {k: v for k, v in sorted(word_count.items(), key=lambda item: item[1], reverse=True)}

    logger.info(f"Word Frequency: {sorted_word_count}")
    logger.info("---------------------------------")

def show_log():
    """Read log file and print it to the terminal"""
    with open(logname, "r") as file_wrapper:
        print(file_wrapper.read())

if __name__ == "__main__":
    illustrate_tuples()
    illustrate_sets()
    illustrate_dictionaries()
    show_log()
