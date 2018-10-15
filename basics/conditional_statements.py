"""
This program explains conditional statement
"""
# ctrl + alt + l to format the with proper indentation

# if statement : which will say given number is positive

num = int(input('enter a number'))

if num > 0:
    print(f'{num} is positive number')

# if else statement : which will say a given number is odd or even

if num % 2 == 0:
    print(f'{num} is even number')
else:
    print(f'{num} is odd number')

# else if ladder and nested if : grade of a student based on marks

marks = int(input('enter marks'))

if 100 >= marks >= 0:
    if marks >= 70:
        print('distinction')
    elif marks >= 60:
        print('first class')
    elif marks >= 50:
        print('second class')
    elif marks >= 40:
        print('third class')
    else:
        print('failed')
else:
    print('enter proper marks')
