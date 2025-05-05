# while loop 
# total_iteration_number = 5
# first_iteration_number = 0

# while (first_iteration_number <= total_iteration_number):
#   first_iteration_number = first_iteration_number + 1
#   if first_iteration_number == 3:
#     continue
#   print(first_iteration_number)


# while (first_iteration_number <= total_iteration_number):
#   first_iteration_number = first_iteration_number + 1
#   if first_iteration_number == 3:
#     break
#   print(first_iteration_number)

# reddish_fruits = ["Straberry", "cherry", "blackberry", "pomegranat"]
# non_radish_fruits = ["pineapple", "appricot", "nectarin", "papaya"]

# for fruit in range(0,6):
#   print(fruit)

# for letter in fruits[0]:
#   if letter == "p":
#     continue
#   print(letter)


# reddish_fruits = ["Straberry", "cherry", "blackberry", "pomegranat"]
# non_radish_fruits = ["pineapple", "appricot", "nectarin", "papaya"]


# for red_fruit in reddish_fruits:
#   for non_reddish_fruit in non_radish_fruits:
#     print(red_fruit, non_reddish_fruit)

# function 


#  call function based unknown arguments
# def calculate_sum_number (*number):
#   total_number = number[0] + number[1]
#   return total_number

# result_sum_numbers = calculate_sum_number(16,16)
# print(result_sum_numbers)

# def calculate_sum_number (number1, number2):
#   total_number = number1 + number2
#   return total_number

# result_sum_numbers = calculate_sum_number(number2 = 8, number1= 12)
# print(result_sum_numbers)


# call function based unknown number of key-value pair argument
# def calculate_sum_number (number1, number2 = 16):
#   total_number = number1 + number2
#   return total_number

# result_sum_numbers = calculate_sum_number(8,8)
# print(result_sum_numbers)

# #### function 
# def addition_numbers (*arg):
#   sum_number = arg[0] + arg[1] + arg[2]
#   return sum_number

# total_number = addition_numbers(16,24, 25)
# print(total_number)

# def addition_numbers (number1 = 16, number2 = 24):
#   sum_number = number1 + number2
#   return sum_number

# total_number1 = addition_numbers()
# total_number2 = addition_numbers(number2 = 20)
# total_number3 = addition_numbers(number1 = 80)
# total_number4 = addition_numbers(200)
# total_number5 = addition_numbers(200,400)
# total_number6 = addition_numbers(number2 = 20, number1 = 80)
# print(total_number1)
# print(total_number2)
# print(total_number3)
# print(total_number4)
# print(total_number5)
# print(total_number6)


# def print_fruit (fruits):
#   fruits_collection = []

#   for fruit in fruits:
#       fruits_collection.append(fruit)
#   return fruits_collection

# print(print_fruit(["peach", "nectarin","pineapple","pear"]))


# def addition_numbers (number1, number2,/):
#   sum_number = number1 + number2
#   return sum_number

# # total_number1 = addition_numbers()
# # total_number2 = addition_numbers(number2 = 20)
# # total_number3 = addition_numbers(number1 = 80)
# # total_number4 = addition_numbers(200)
# total_number5 = addition_numbers(200,400)
# # total_number6 = addition_numbers(number2 = 20, number1 = 80)
# # print(total_number1)
# # print(total_number2)
# # print(total_number3)
# # print(total_number4)
# print(total_number5)
# # print(total_number6)


# keyword only argument 
# def addition_numbers (*, number1, number2):
#   sum_number = number1 + number2
#   return sum_number

# # total_number1 = addition_numbers()
# # total_number2 = addition_numbers(number2 = 20)
# # total_number3 = addition_numbers(number1 = 80)
# # total_number4 = addition_numbers(200)
# # total_number5 = addition_numbers(200,400)
# total_number6 = addition_numbers(number2 = 20, number1 = 80)
# # total_number7 = addition_numbers(20, number1 = 80)
# # print(total_number1)
# # print(total_number2)
# # print(total_number3)
# # print(total_number4)
# # print(total_number5)
# print(total_number6)
# # print(total_number7)


# recursion 
# fruits = ["peach", "nectarin","pineapple","pear", "cherry"]

# def find_fruit(fruits):
#   for fruit in range(len(fruits)):
#     if  fruits[fruit] == "cherry" and fruit != 0:
#       print(fruits[fruit])
#       return find_fruit(fruits)
    

# print(find_fruit(fruits))