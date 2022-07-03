# =============================================================================
# print("One, 'two', \"three\", four,\n\\five\\once, 'I' caught a \n\t fish '//alive\\\\'")
# 
# user_input = int(input('How many apples do you have? \n=> '))
# =============================================================================

# =============================================================================
# pi = 3.14159
# radius = int(input('What is the radius of the circle?\n>>> '))
# area = pi * radius**2
# 
# print('You entered the radius ', radius, ' The Area is ', area)
# =============================================================================

# =============================================================================
# Farenheit = float(input('What is the Temperature in Farenheit?\n>>> '))
# Celsius = (Farenheit - 32)* 5/9
# 
# print(Farenheit,' Farenheit is equivalent to ', Celsius, 'Celsius')
# =============================================================================

# =============================================================================
# num1 = int(input('What is the 1st number?\n>>> '))
# num2 = int(input('What is the 2nd number?\n>>> '))
# answer = num1 + num2
# 
# print('The sum of the 2 numbers is ', answer)
# =============================================================================

# =============================================================================
# NumOfPeople = int(input('How many people are there?\n>>> '))
# SlicesInEachPizza = int(input('How many slices are there in each Pizza?\n>>> '))
# EachPersonEat = int(input('How many slices did each person eat?\n>>> '))
# 
# TotalSlicesNeeded = NumOfPeople * EachPersonEat
# NumOfPizzaNeeded = (TotalSlicesNeeded // SlicesInEachPizza ) + 1
# SlicesRemaining = (NumOfPizzaNeeded * SlicesInEachPizza ) - TotalSlicesNeeded
# 
# 
# print('For', NumOfPeople,' number of people', 'and each eat ', EachPersonEat, '.')
# print('The total number of Pizzas needed is ', NumOfPizzaNeeded)
# print('There will be ', SlicesRemaining,' slices remaining.')
# =============================================================================


# =============================================================================
# num1 = int(input('Please enter an integer between 1-5: >>> '))
# 
# if num1 == 1:
#     print('One')
# elif num1 == 2:
#     print('Two')
# elif num1 == 3:
#     print('Three')
# elif num1 == 4:
#     print('four')
# elif num1 == 5:
#     print('five')
# else:
#     print('Invalid Input')
# =============================================================================

# =============================================================================
# CorrectNumber = 5
# 
# GuessedNumber = input('What number do you think is correct? >>> ')
# 
# if GuessedNumber.isdigit():
#     GuessedNumber = int(GuessedNumber)
# 
#     if CorrectNumber == GuessedNumber:
#         print('You have Won!')
#     elif CorrectNumber > GuessedNumber:
#         print('Your number is too low')
#     elif CorrectNumber < GuessedNumber:
#         print('Your number is too high')
#     else:
#         print('You are Incorrect!')
# 
# else:
#     print('That is not an Integer')
# =============================================================================

# =============================================================================
# name = input('Please input your name. >>> ')
# 
# if len(name) > 5:
#     print('Number of characters in name is ', len(name))
# else:
#     print('Your name is too short')
# =============================================================================

# =============================================================================
# num1 = int(input('Enter 1st number: >>> '))
# num2 = int(input('Enter 2nd number: >>> '))
# 
# if (num1 < 1 or num1 > 20) or (num2 < 1 or num2 > 20):
#     print('Out of Range')
# 
# else:
#    
#     if (num1 > 15 and num1 < 21) and (num2 >15 and num2 < 21):
#         print(num1 * num2)
#     
#     elif (num1 > 15 and num1 < 21) or (num2 >15 and num2 < 21):
#         print(num1 + num2)
#         
#     elif (num1 > 0 and num1 < 16) and (num2 >0 and num2 < 16):
#         print(0)
#     else:
#         print('Out of Range')
# =============================================================================

data = [1,3,7,4,9,5,8,2,6,11]
max = 0

print(data)
for num in data:
    if num > max:
        max = num
        print(num, end=' ')

print('Max Value is ', max)
print('This is just a test statement')
print('Is this new statement only happening on the new branch?')



























































