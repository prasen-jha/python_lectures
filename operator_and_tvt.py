# =,+,-,/,% Airthmetic operators
# >,<,>,=<,<=,== #Truth Value Testing Operators
# >>,<<, ^,|,& Bitwise Operators

# and,in,is,or not


print(12>11)
print(13<12)
print(type('q')== str)
print(() != tuple)
print(11 <= 11)

lis = []
for i in range(10):
    if len(lis) != 8:
        lis.append(i)
print(lis)


Flag = True

if Flag:
    print('Hello World')

print(True or False)
print(True and False)

print('ll' in 'Hello')
print(type(12) is int)

a =2
b =3
c =2 

print(a is c)
print(type(a) is type(b))

# OPERATORS

### STRING OPERATORS :

#1. + --> it merges two strings
#2. * --> it multiples the string the no. of times given for example

### AIRTHMETIC OPERATORS


#Integer Operators
# +,-,*,/,%

#COMPOUND OPERATORS

a = 2

# a = a+1
a += 1
print(a)
a -= 2
# a = a-2
print(a)
a /= 2
print(a)
a *= 2
print(a)

print(('-=--'*20))

# Constants
     
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