#  this program explains functions in python

#  in python we no need to write any return type to the function
#  functions accepts arguments


# a function without return type and without arguments
# def display():
#     print("Hi I'm a function")
#
#
# # a function without return type and with arguments
# def add(a, b):
#     print(f'sum is {a+b}')
#
#
# # a function with return type and without argumnets
# def multiply():
#     return 10 * 20
#
#
# # a function with return type and with argumnets
# def sub(a, b):
#     return a - b
#
#
# display()
# add(10, 20)
#
# c = multiply()
# print(f'product of 10 and 20 is {c}')
#
# s = sub(10, 20)
# print(s)
#
#
# # create a method which accepts details of a person and print them and also verify if that person is eligible to vote or not
# def personal_details(name, address, age, gender):
#     print(f'name : {name}\naddress : {address}\nage : {age}\ngender : {gender}')
#     if age >= 18:
#         print('eligible to vote')
#     else:
#         print(f'apply after {18 - age} years')
#
#
# personal_details('lakshmi', 'ligampally', 35, 'female')
# personal_details('teja', 'kphb', 15, 'male')


# create a function to find area of a circle
# def area_of_cirle(radius):
#     area = 3.14 * radius ** 2
#     return area
#
# print(f'area = {area_of_cirle(5)}')


# create a function to find out given number is palindrome or not
def palindrome_number(num):
    r = 0
    temp = num
    while num//10 != 0:
       c = num % 10
       r = r*10 + c
       num //= 10
    c = num % 10
    r = r * 10 + c
    if r == temp:
        return True
    else:
        return False

result = palindrome_number(12324)
print(result)