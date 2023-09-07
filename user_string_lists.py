"""
Author: Josiah Randleman
Date: 9/8/2023
"""
import random
from util_datafun_logger import setup_logger

# Set up logging .............................................

logger, logname = setup_logger(__file__)

# String Lists
listA = ["Python", "Java", "C++", "JavaScript", "Ruby"]
listB = ["Numpy", "Pandas", "React", "TensorFlow", "Scikit-learn"]
listC = ["VSCode", "PyCharm", "Eclipse", "Sublime", "Atom"]
listD = ["MySQL", "PostgreSQL", "MongoDB", "SQLite", "Cassandra"]
listE = ["Agile", "Scrum", "Waterfall", "Kanban", "Lean"]

def step1():
    lenA = len(listA)
    lenB = len(listB)
    uniqueA = set(listA)
    uniqueB = set(listB)
    combined_lists = list(zip(listA, listB))

    logger.info(f"Length of listA: {lenA}")
    logger.info(f"Unique elements in listA: {uniqueA}")
    logger.info(f"Length of listB: {lenB}")
    logger.info(f"Unique elements in listB: {uniqueB}")
    logger.info(f"Combined lists into tuples: {combined_lists}")
    logger.info("---------------------------------")


def step2():
    random_lang = random.choice(listA)
    random_lib = random.choice(listB)
    random_editor = random.choice(listC)
    random_db = random.choice(listD)
    random_method = random.choice(listE)

    sentence = f"For developing a machine learning application, one might use {random_lang} with {random_lib}, code it in {random_editor}, store data in {random_db}, and follow a {random_method} methodology."
    logger.info(f"Generated sentence: {sentence}")
    logger.info("---------------------------------")

def step3():
    try:
         with open("text_names_in.txt", 'r') as file:
                text = file.read()
                words = text.split()
                unique_words = set(words)
                sorted_unique_words = sorted(unique_words)
                unique_word_count = len(sorted_unique_words)

                logger.info(f"Unique words from the text file: {sorted_unique_words}")
                logger.info(f"Number of unique words: {unique_word_count}")
                logger.info(f"How good is your list? Well, it has {unique_word_count} unique words.")   
    except Exception as e:
        logger.error(f"An error occurred: {e}")
    logger.info("---------------------------------")

def show_log():
    """Read log file and print it to the terminal"""
    with open(logname, "r") as file_wrapper:
        print(file_wrapper.read())

if __name__ == "__main__":
    step1()
    step2()
    step3()
    show_log()
