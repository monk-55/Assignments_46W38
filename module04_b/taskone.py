"""
Module4 Task one - code to use the functions in the module created
"""
#importing the module already created
import MyModule

#The next 3 lines use each of the functions in Mymodule
numbers = MyModule.get_a_list_of_numbers()

numbers_min = MyModule.find_min(numbers)
numbers_max = MyModule.find_max(numbers)

sorted_numbers = MyModule.sort_numbers(numbers)


print(f'The list of number is: {numbers}')    
print(f'The minimal number is: {numbers_min}')
print(f'The maximal number is: {numbers_max}')