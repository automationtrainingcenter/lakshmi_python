"""
    This program explains how to print some text on the console and
    also how to read some data from the console
"""

# read student details like name, course, address phone number from the  console and print on the console


name = input("enter student name:\t")
course = input("enter course name:\t")
address = input("enter student address:\t")
phone_number = int(input("enter phone number:\t"))

print(f'name = {name}\ncourse = {course}\naddress = {address}\nphone number = {phone_number}')