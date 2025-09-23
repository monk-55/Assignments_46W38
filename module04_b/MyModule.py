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
            numbers += [int(x)]
        except ValueError:
            print(f"Warning: '{x}' is not a valid entry")
    return numbers    


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
print(find_max(numbers))
"""

