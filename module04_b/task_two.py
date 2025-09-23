"""
Module04 Task2

"""
import string

def count_words(filename):
    #using try and except to raise an error if we can't find the file
    try:
        with open(filename) as f:
            Alltext = f.read()
            translator = str.maketrans('','', string.punctuation)
            clean_text = Alltext.translate(translator)
        # used this just to test above code print(clean_text)
        #adding a variable 'counter' that starts as 0
        counter = 0

#iterating through the string to count the words by adding 1 each time to the counter. Using split to split the text to words
        for word in clean_text.split():
            counter += 1
        print(counter)

    except FileNotFoundError:
        print("Warning: file does not exist")
    
    
filename = 'Assignments_46W38\module04_b\The_Zen_of_Python.txt'
count_words(filename)