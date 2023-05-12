# Write a function that takes an unknown number of arguments and returns their sum.
def sum_number(*numbers):
    sum=0
    for num in numbers:
        sum+=num
    return sum
print(sum_number(1,2,3,4,5))
# Write a function that takes two arguments, the first being a string and the second
#  being an unknown number of integers. The function should return 
# a new string where the integers have been added to the original string.

# Write a function that takes an unknown number of keyword arguments and returns a 
# dictionary where the keys are the argument names and the values are the argument values.
def student_names(**names):
    # for key,value in names.items():
    #     print(f"{key}:{value}")
    print(names)
student_names(names="Angeth",age=30,height=178,weight=52)

# Write a function that takes a function and an unknown number of arguments, and returns 
# the result of calling the function with the arguments.
# def remainder(num1,num2):
    

# Write a function that takes a list of integers and an unknown number of keyword arguments. 
# The function should return a new list where each integer in the original list has been 
# multiplied by the value of the corresponding keyword argument.

# Write a function that takes a list of integers and an unknown number of additional integers 
# as arguments. The function should return the index of the first occurrence of the sum 
# of the list and the additional integers
# def occurrence(numbers):


# Write a function that takes an unknown number of keyword arguments, each with a string value. 
# The function should concatenate all the strings and return the resulting string.
def concatenate_string(**words):
    for key,value in words.items():
        print(f"{key}:{value}")
concatenate_string(greeting="Hello",message="I am learning Python")
    

