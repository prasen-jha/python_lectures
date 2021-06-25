'''
while making logical decisions we do a lot of comparison and following
code helps us in understanding the comaprison logic between variables
'''

value = True
no_value = None
false_value = False

if value or no_value:
   print('Hello World')

if value and false_value:
   print('the o/p was False')

if not no_value:
   print('The output was true')
else:
   print('The o/p was False')


a = 23
b =32

if a < b:
    print('Hello World !')
else:
    print('Yellow World!')

if a > b:
    print('Hello World !')
else:
    print('Yellow World!')

if a != b:
    print('Hello World !')
else:
    print('Yellow World!')

c = 23

if a >= c:
    print('Hello World !')
else:
    print('Yellow World!')
