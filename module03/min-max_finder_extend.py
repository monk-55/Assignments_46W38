"""
Module 3 Task03 optiona extra - sorting the list
writing a script to find the minimal and maximum of a list of numbers
List fo numbers is user input and user decides when to end by typing end
"""

#crate an empty list and an empty variable x
numbers = []
x= None

# have used a while loop but also a break on the same condition which perhaps is not necessary, but allows to break before trying to add 'end'
# to the list or variables
while x != 'end':
    x = input('Please enter a number to add to the list, or type end to finish the list: ')
    if x == 'end':
        break
#next line initiates the min and max as the first number entered, once the list is populated this won't run as list length>0
    if len(numbers) == 0:
        min_num = x
        max_num = x
#checking if the new number added is lower or higher than existing min and max
    if x >= max_num:
        max_num = x
    if x<= min_num:
        min_num = x
    numbers += [int(x)]

#sorting?? first iterate through the amount of numbers, determined by the length of the list
#check ecah one against all others in the list. Had to look up the internet to know how to swap locations in the list however
#had no idea how to do this
for number in range(len(numbers)):
    for i in range(len(numbers)-1):
        if numbers[i]>numbers[i+1]:
            numbers[i],numbers[i+1] = numbers[i+1], numbers[i]




#print statements as specified
print(f'The list of number is: {numbers}')    
print(f'The minimal number is: {min_num}')
print(f'The maximal number is: {max_num}')