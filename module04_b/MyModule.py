"""
This module contains 3 functions.
Function 1 get_a_list_of_numbers asks for numbers from the user and creates a list
Function 2 find_min(list_of_numbers) returns the minimum number in the list, return None if empty list
Function 3 find_max(list_of_numbers) returns the maximum number in the list, return None if empty list
"""

#Function 1
def get_a_list_of_numbers():
    numbers = []
    x=None
    while x != 'end':
        x = input('Please enter a number to add to the list, or type end to finish the list: ')
        if x == 'end':
            break
        try:
            numbers += [float(x)]
        except ValueError:
            print(f"Warning: '{x}' is not a valid entry")
    return numbers    

#Optional task to add multiple numbers separated by a space - then you would have to split this as in the word count task
#andthen add these to the list. How to make them floats
def get_a_list_of_numbers_at_once():
    numbers = []

    user_numbers = (input('Please enter a list of numbers to add to the list, each separated with a space')).split()
    for i in user_numbers:
        try:
            numbers += [float(i)]
        except ValueError:
            print(f"Warning: '{i}' is not a valid entry")

    return numbers    


#code to test optional task
"""
numbers = get_a_list_of_numbers_at_once()
print(numbers)
"""
"""
code to test function1
numbers = get_a_list_of_numbers()
print(numbers)
"""


#Function 2
def find_min(list_of_numbers):
    min_number = None
    for number in list_of_numbers:
        if min_number == None:
            min_number = number
        elif number <= min_number:
            min_number = number

    return min_number
"""
testing code
print(find_min(numbers))
"""



#Function 2
def find_max(list_of_numbers):
    max_number = None
    for number in list_of_numbers:
        if max_number == None:
            max_number = number
        elif number >= max_number:
            max_number = number

    return max_number

"""
testing code
print(find_max(numbers))
"""

#Optional task to add a function sorting the list of numbers
def sort_numbers(list_of_numbers,ascending=True):
    for number in range(len(list_of_numbers)):
        if ascending == True:
            for i in range(len(list_of_numbers)-1):
                if list_of_numbers[i]>list_of_numbers[i+1]:
                    list_of_numbers[i],list_of_numbers[i+1] = list_of_numbers[i+1], list_of_numbers[i]
        if ascending == False:
            for i in range(len(list_of_numbers)-1):
                if list_of_numbers[i]>list_of_numbers[i+1]:
                    list_of_numbers[i],list_of_numbers[i+1] = list_of_numbers[i+1], list_of_numbers[i]
    return list_of_numbers



"""
testing code
print(sort_numbers(numbers))
"""