'''
    this program explains loops and break, continue statements
'''


# range(start, end, step)
# implementing for loop to print factorial of a given number
num = int(input('enter a numeber'))
fact = 1

for i in range(1, num + 1):
    fact *= i
#
# print(f'factorial of {num} is {fact}')

# write a while loop to print number of vowels in a string
# data = input('enter a string')
# i = 0
# count = 0
# d = ''
# while i < len(data):
#     if data[i] not in d:
#         d += data[i]
#     i += 1
#
# i = 0
# while i < len(d):
#     if d[i] == 'a' or d[i] == 'e' or d[i] == 'i' or d[i] == 'o' or d[i] == 'u':
#         count += 1
#     i += 1
#
# print(f'number of vowel in {data} is {count}')
# print(f'{data} without duplicates {d}')


# deleting duplicates in a string using for loop
# d = ''
# for c in data:
#     if c not in d:
#         d += c
#
# print(f'{data} after deletion of duplicates = {d}')


# this game to explain break and continue statement
#
# while True:
#     value = input('enter a string\n')
#     if 'a' in value or 'e' in value or 'i' in value or 'u' in value or 'o' in value:
#         continue  # it will skip the current iteration
#     else:
#         break  # it will terminate the loop

#  this game explains inner loops with break and continue statements
# while True:
#     flag = False
#     number = int(input('enter a number:\t'))
#     for i in range(0, 3):
#         mul1 = int(input(f'enter multiple {i+1}: '))
#         if mul1 % number != 0:
#             flag = True
#             print('Failed')
#             break
#         else:
#             continue
#     if flag:
#         break


# increment range by 2 or some other value
for i in range(0, 10, 2):
    print(i)
