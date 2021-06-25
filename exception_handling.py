# print('herllo world'!)


# # if 'y' in 'yes':
# #     print('y')

# 1/0

# try:
#     age = abs(int(input('What\'s your age: ')))
#     print('Hmm! i see you are %d years old' %age)
# except ValueError:
#     print('The input was probably not an int')

# try:
#     dividend = int(input('Enter the value of dividend: '))
#     divisor = int(input('Enter the value of divisor: '))
#     print('the  value of operation on %d/%d is %f'%(dividend,divisor,dividend/divisor))
# except(ValueError,ZeroDivisionError):
#     print('something went wrong')

try:
    age = int(input('What\'s your age: '))   
except ValueError:
    print('Value is not what was required')
else:
    print(f'so you are {age} years old')
finally:
    print('we are stopping the execution')

